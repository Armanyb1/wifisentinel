import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "license.db"

def _db():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS licenses(
        device_id TEXT PRIMARY KEY,
        plan TEXT NOT NULL,
        expires_at TEXT
    )""")
    return con

def get_license(device_id):
    con = _db()
    row = con.execute(
        "SELECT plan, expires_at FROM licenses WHERE device_id=?",
        (device_id,)
    ).fetchone()
    con.close()
    return row

def set_license(device_id, plan, expires_at):
    con = _db()
    con.execute(
        "INSERT OR REPLACE INTO licenses(device_id,plan,expires_at) VALUES(?,?,?)",
        (device_id, plan, expires_at)
    )
    con.commit()
    con.close()

def revoke(device_id):
    con = _db()
    con.execute("DELETE FROM licenses WHERE device_id=?", (device_id,))
    con.commit()
    con.close()
