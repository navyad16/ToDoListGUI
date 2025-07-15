"""#POSTGRE SQL Setup
CREATE DATABASE todo_db;
\c todo_db

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_done BOOLEAN DEFAULT FALSE
);
"""

import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="user",
        password="Aa@12345",
        dbname="todo_db"
    )


