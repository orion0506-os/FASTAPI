from fastapi import FastAPI

import sqlite3

app=FastAPI()

db=sqlite3.connect("test.db",check_same_thread=False)

curr=db.cursor()

curr.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100)
);
""")

db.commit()

