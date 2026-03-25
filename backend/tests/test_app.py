import sqlite3

from fastapi.testclient import TestClient

from app.config import DATABASE_PATH
from app.main import app


def test_healthcheck_returns_ok():
    with TestClient(app) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_startup_resets_database_with_users_table():
    with TestClient(app):
        pass

    assert DATABASE_PATH.exists()

    with sqlite3.connect(DATABASE_PATH) as connection:
        row = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users'"
        ).fetchone()

    assert row == ("users",)


def test_workspace_route_falls_back_to_frontend_html_when_static_build_exists(tmp_path, monkeypatch):
    static_dir = tmp_path / "static"
    static_dir.mkdir()
    (static_dir / "index.html").write_text("<html><body>workspace shell</body></html>", encoding="utf-8")

    monkeypatch.setattr("app.main.FRONTEND_DIST_DIR", static_dir)

    fallback_app = TestClient(app)
    response = fallback_app.get("/workspace")

    assert response.status_code == 200
    assert "workspace shell" in response.text
