import os
import pytest
from hog_server import create_app, database


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "DATABASE": os.path.join(app.instance_path, "test-db.sqlite3"),
        }
    )
    with app.app_context():
        database.init_db()

    yield app

    os.remove(os.path.join(app.instance_path, "test-db.sqlite3"))


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()