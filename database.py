import sqlite3
from datetime import datetime,timedelta
import os

DATABASE = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn,conn.cursor()

def get_all_desks():
    conn, cursor = get_db()

    cursor.execute("""
    SELECT *
    FROM desks
    ORDER BY id
    """)

    desks = cursor.fetchall()

    conn.close()

    return desks

def get_desk(desk_id):
    conn, cursor = get_db()

    cursor.execute("""
    SELECT *
    FROM desks
    WHERE id = ?
    """, (desk_id,))

    desk = cursor.fetchone()

    conn.close()

    return desk

def check_in(desk_id,occupant):
    conn, cursor = get_db()

    check_in_time = datetime.now().isoformat()

    cursor.execute("""
    UPDATE desks
    SET occupant = ?,
        status = 'occupied',
        away_until = NULL,
        checkin_time = ?
    WHERE id = ?
    """, (occupant, check_in_time ,desk_id))

    conn.commit()
    conn.close()

def mark_away(desk_id):
    conn, cursor = get_db()

    away_until = (datetime.now() + timedelta(minutes=20)).isoformat()


    cursor.execute("""
    UPDATE desks
    SET status = 'away',
    away_until = ?
    WHERE id = ?
    """, (away_until, desk_id))

    conn.commit()
    conn.close()

def leave_desk(desk_id):
    conn, cursor = get_db()

    cursor.execute("""
    UPDATE desks
    SET occupant = NULL,
        status = 'free',
        checkin_time = NULL,
        away_until = NULL
    WHERE id = ?
    """, (desk_id,))

    conn.commit()
    conn.close()

def return_from_away(desk_id):
    conn, cursor = get_db()

    cursor.execute("""
    UPDATE desks
    SET status = 'occupied',
    away_until = NULL
    WHERE id = ?
    """, (desk_id, ))

    conn.commit()
    conn.close()

def check_expired_desks():
    conn, cursor = get_db()

    cursor.execute("""
    SELECT id, away_until
    FROM desks
    WHERE status = 'away'
    """)

    desks = cursor.fetchall()

    now = datetime.now()

    for desk in desks:

        if not desk["away_until"]:
            continue

        away_until = datetime.fromisoformat(
            desk["away_until"]
        )
        if now >= away_until:

            cursor.execute("""
            UPDATE desks
            SET occupant = NULL,
                status = 'free',
                checkin_time = NULL,
                away_until = NULL
            WHERE id = ?
            """, (desk["id"],))

    conn.commit()
    conn.close()