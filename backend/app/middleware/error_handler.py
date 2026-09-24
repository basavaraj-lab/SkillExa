import logging
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from backend.app.config import settings

logger = logging.getLogger("skillexa.errors")


def register_error_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        # Derive standardized error code
        code_map = {
            400: "BAD_REQUEST",
            401: "UNAUTHORIZED",
            403: "FORBIDDEN",
            404: "NOT_FOUND",
            409: "CONFLICT",
            422: "UNPROCESSABLE_ENTITY",
            500: "INTERNAL_SERVER_ERROR",
        }
        error_code = code_map.get(exc.status_code, "ERROR")

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.detail if isinstance(exc.detail, str) else str(exc.detail),
                "code": error_code,
                "data": None,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # Extract first readable validation error
        errors = exc.errors()
        message = "Validation error"
        if errors:
            loc = " -> ".join([str(l) for l in errors[0].get("loc", []) if l != "body"])
            msg = errors[0].get("msg", "Invalid value")
            message = f"{loc}: {msg}" if loc else msg

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "success": False,
                "message": message,
                "code": "VALIDATION_ERROR",
                "details": errors if settings.DEBUG else None,
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled server exception: {exc}", exc_info=True)
        message = "An unexpected internal server error occurred."
        if settings.DEBUG:
            message = f"Internal Error: {str(exc)}"

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": message,
                "code": "INTERNAL_SERVER_ERROR",
                "data": None,
            },
        )
