# database.py

import sqlite3

def create_database():
    conn = sqlite3.connect('../data/robot_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS motor_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        speed REAL)''')
    conn.commit()
    conn.close()

def insert_data(speed):
    conn = sqlite3.connect('../data/robot_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO motor_data (speed) VALUES (?)', (speed,))
    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect('../data/robot_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motor_data')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    create_database()
    insert_data(0.5)
    fetch_data()
