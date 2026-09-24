# SkillExa — Python FastAPI Backend

Enterprise-grade educational backend for **SkillExa** built with **Python 3.12**, **FastAPI**, **SQLAlchemy ORM**, **Pydantic v2**, **JWT Authentication**, and **Alembic migrations**.

---

## 🚀 Quick Windows PowerShell Startup (Reliable Method)

No global `uvicorn` or global `py` command is needed. The virtual environment is located inside `backend/venv` (and `backend/.venv`).

### 1. Open PowerShell and Navigate to the `backend` Folder
```powershell
cd C:\Users\Ganesh\.antigravity\skillexa-app\backend
```

### 2. Install Requirements (If Setting Up Fresh)
```powershell
# If needed, create and install into venv:
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Start the FastAPI Backend Server
```powershell
.\venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🔍 Verification & Health Check

### 1. Test Health Endpoint
In PowerShell or your browser:
- **URL**: `http://localhost:8000/api/health`
- **Response**:
```json
{
  "status": "ok",
  "message": "SkillExa backend is running"
}
```

### 2. Interactive Swagger Documentation
Open in your browser:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 3. Run Automated Tests
```powershell
.\venv\Scripts\python.exe -m pytest tests -v
```

---

## 📱 Connecting Expo Frontend on Phone / Wi-Fi

When testing on an Android or iOS physical device running Expo Go over local Wi-Fi:

### 1. Find Your PC's Local IPv4 Address
In PowerShell:
```powershell
ipconfig
```
Look for `IPv4 Address` under your active Wi-Fi adapter (e.g., `192.168.1.15`).

### 2. Configure Frontend URL
In your project `.env` or `app.json`, set:
```env
EXPO_PUBLIC_API_URL=http://192.168.1.15:8000
```
Or the app will automatically use:
- **Android Emulator**: `http://10.0.2.2:8000/api`
- **iOS Simulator / Web**: `http://localhost:8000/api`

---

## 🏗️ Architecture & Features

1. **Authentication & Roles**:
   - Students & Faculty registration and login via JWT bearer tokens.
   - Faculty approval verification (`PENDING`, `APPROVED`, `REJECTED`).

2. **College Connection & Audience Targeting**:
   - Linked via `college_id`.
   - Content targeting based on `[college_id + department + academic_year + section]`.

3. **Faculty Authoring & PDF Notes**:
   - Topic notes with theory, important concepts, and quick revision points.
   - Secure PDF upload, download, and in-place replacement with automatic version increment (`v1 -> v2`).

4. **Quizzes & Scoring Engine**:
   - Multi-question quizzes with topic isolation.
   - Answer leak prevention on start; full evaluation with accuracy %, negative marks, and topic progress on submit.

5. **Isolated Code Execution Sandbox**:
   - Sandboxed execution for **Python**, **C**, **C++**, **Java**, and **JavaScript** with process limits, timeout limits, sanitized environment variables, and automatic scratch cleanup.

6. **Viva & Video Interviews with WebRTC**:
   - Scheduling, multi-criterion evaluation, and WebSocket-based SDP/ICE signaling for real-time video calls.

7. **SkillExa Community Discovery Feed**:
   - Public multi-filtered educational feed for verified faculty content (`GET /api/community/content`).
