from flask import Flask, request, jsonify
import sqlite3
from werkzeug.serving import run_simple

app = Flask(__name__)
DATABASE = 'tasks.db'

def get_db():
    return sqlite3.connect(DATABASE)

def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    db.commit()
    db.close()

init_db()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cursor = db.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    db.close()
    tasks = [
        {"id": row[0], "title": row[1], "description": row[2], "done": bool(row[3])}
        for row in rows
    ]
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    db = get_db()
    cursor = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    db.close()
    if row is None:
        return jsonify({"error": "Task not found"}), 404
    task = {"id": row[0], "title": row[1], "description": row[2], "done": bool(row[3])}
    return jsonify(task), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    title       = data['title']
    description = data.get('description', '')
    done        = data.get('done', False)
    db = get_db()
    cursor = db.execute(
        'INSERT INTO tasks (title, description, done) VALUES (?, ?, ?)',
        (title, description, int(done))
    )
    db.commit()
    new_id = cursor.lastrowid
    db.close()
    return jsonify({"id": new_id, "title": title, "description": description, "done": done}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    db = get_db()
    cursor = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    if row is None:
        db.close()
        return jsonify({"error": "Task not found"}), 404
    title       = data.get('title',       row[1])
    description = data.get('description', row[2])
    done        = data.get('done',        bool(row[3]))
    db.execute(
        'UPDATE tasks SET title = ?, description = ?, done = ? WHERE id = ?',
        (title, description, int(done), task_id)
    )
    db.commit()
    db.close()
    return jsonify({"id": task_id, "title": title, "description": description, "done": done}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = get_db()
    cursor = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    if row is None:
        db.close()
        return jsonify({"error": "Task not found"}), 404
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    db.close()
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    run_simple("localhost", 5000, app)
