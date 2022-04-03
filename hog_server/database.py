import sqlite3
from flask import g, current_app


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def get_type_id(type):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT ID FROM MEASUREMENT_TYPE WHERE NAME = ?", (type,))
    row = cur.fetchone()
    if row:
        return row["id"]
    else:
        return None


def get_device_id(device):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT ID FROM DEVICE WHERE TECHNICAL_NAME = ?", (device,))
    row = cur.fetchone()
    if row:
        return row["id"]
    else:
        cur.execute("INSERT INTO DEVICE (TECHNICAL_NAME) VALUES (?)", (device,))
        db.commit()
        return cur.lastrowid


def update_custom_device_name(device_id, custom_name):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "UPDATE DEVICE SET CUSTOM_NAME = ? WHERE ID = ?",
        (
            custom_name,
            device_id,
        ),
    )
    db.commit()


def add_measurement(type_id, device_id, data_value):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO MEASUREMENT(INSERTED_BY, TYPE, VALUE) VALUES(?, ?, ?)",
        (
            device_id,
            type_id,
            data_value,
        ),
    )
    db.commit()