from DB_Config import get_connection

def fetch_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, is_done FROM tasks ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_task(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    conn.close()

def update_status(task_id, is_done):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET is_done=%s WHERE id=%s", (is_done, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
