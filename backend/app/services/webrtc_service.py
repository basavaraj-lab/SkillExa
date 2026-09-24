from datetime import datetime
from typing import Dict, List, Optional
from fastapi import HTTPException, WebSocket, status
from sqlalchemy.orm import Session
from backend.app.models.interview import VideoSession


class WebRTCSignalingManager:
    """In-memory active WebSocket connections per room for WebRTC SDP offer/answer/ICE exchange."""

    def __init__(self):
        # Mapping: room_id -> list of active WebSocket connections
        self.active_rooms: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        if room_id not in self.active_rooms:
            self.active_rooms[room_id] = []
        self.active_rooms[room_id].append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        if room_id in self.active_rooms:
            if websocket in self.active_rooms[room_id]:
                self.active_rooms[room_id].remove(websocket)
            if len(self.active_rooms[room_id]) == 0:
                del self.active_rooms[room_id]

    async def broadcast_to_room(self, room_id: str, message: dict, sender: WebSocket):
        """Forward signaling message (offer/answer/candidate) to peer in the room."""
        if room_id in self.active_rooms:
            for connection in self.active_rooms[room_id]:
                if connection != sender:
                    await connection.send_json(message)

    @staticmethod
    def update_session_state(
        db: Session,
        room_id: str,
        user_id: str,
        joined: bool,
    ) -> VideoSession:
        session = db.query(VideoSession).filter(VideoSession.room_id == room_id).first()
        if not session:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video session room not found.")

        if user_id == session.faculty_id:
            session.faculty_joined = joined
        elif user_id == session.student_id:
            session.student_joined = joined

        if session.faculty_joined and session.student_joined:
            session.session_status = "ACTIVE"
            if not session.started_at:
                session.started_at = datetime.utcnow()
        elif not session.faculty_joined and not session.student_joined:
            session.session_status = "ENDED"
            session.ended_at = datetime.utcnow()

        db.commit()
        db.refresh(session)
        return session


signaling_manager = WebRTCSignalingManager()
