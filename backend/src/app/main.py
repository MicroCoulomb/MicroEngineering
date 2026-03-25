"""FastAPI application entrypoint."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import FRONTEND_DIST_DIR
from app.db import reset_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Initialize application state on startup."""
    reset_database()
    yield


app = FastAPI(title="MicroPrelegal", lifespan=lifespan)


@app.get("/api/health")
async def healthcheck() -> dict[str, str]:
    """Return a basic service health payload."""
    return {"status": "ok"}


if FRONTEND_DIST_DIR.exists():
    app.mount("/_next", StaticFiles(directory=FRONTEND_DIST_DIR / "_next"), name="next-assets")

    @app.get("/{full_path:path}")
    async def frontend_app(full_path: str) -> FileResponse:
        """Serve static frontend files with HTML fallback for app routes."""
        requested_path = FRONTEND_DIST_DIR / full_path

        if full_path and requested_path.is_file():
            return FileResponse(requested_path)

        if full_path:
            nested_index = FRONTEND_DIST_DIR / full_path / "index.html"
            if nested_index.exists():
                return FileResponse(nested_index)

        return FileResponse(FRONTEND_DIST_DIR / "index.html")
