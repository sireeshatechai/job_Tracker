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
