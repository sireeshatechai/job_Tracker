# db.py - all database functions
import sqlite3
from datetime import date

DB_NAME = "jobs.db"
STATUSES = ["applied","screening","interview","offer","rejected","withdrawn"]

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    conn.execute("""
                  CREATE TABLE IF NOT EXISTS applications(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  company TEXT NOT NULL,
                  role TEXT NOT NULL,
                  link TEXT,
                  status TEXT DEFAULT 'applied',
                  applied_date TEXT,
                  last_update TEXT,
                  notes TEXT
                  )""")
    conn.commit()
    conn.close()


def add_application(company, role, link = None, notes = None):
    today = date.today().isoformat()
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO applications "
        "(company, role, link, status, applied_date, last_update,  notes) "
        "VALUES(?,?,?,'applied',?,?,?)",
        (company,role,link,today,today,notes),
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def list_applications(status = None):
    conn = get_connection()
    if status:
        cur = conn.execute("SELECT * FROM applications WHERE status = ? ORDER BY id", (status,),
                            )
    else:
        cur = conn.execute("SELECT * FROM applications ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows
    
