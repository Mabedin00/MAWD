import sqlite3

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()


def is_valid_login(username: str, password: str) -> bool:
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?;", (username, password))
    return not c.fetchone() is None


def create_account(username: str, password: str):
    print("asd");
    c.execute("INSERT INTO users(username, password, balance) VALUES (?, ?, 0)", (username, password))
    db.commit()


def close_db():
    db.close()