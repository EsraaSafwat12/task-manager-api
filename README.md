# Task Manager API

A lightweight RESTful API built with **Flask** and **SQLite** for managing tasks. Supports full CRUD operations via HTTP endpoints.

## Tech Stack

- Python 3.8+
- Flask
- SQLite
- Werkzeug

## Features

- Create, retrieve, update, and delete tasks
- Persistent storage using SQLite
- JSON responses
- Input validation with proper error messages
- HTTP status codes (200, 201, 400, 404)

## Project Structure

```
task-manager-api/
│
├── app.py          # Main application file
├── tasks.db        # SQLite database (auto-created on first run)
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2. Install dependencies

```bash
pip install flask werkzeug
```

### 3. Run the application

```bash
python app.py
```

The API will be running at `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get a single task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update an existing task |
| DELETE | `/tasks/<id>` | Delete a task |

## Task Schema

```json
{
  "id": 1,
  "title": "Learn Flask",
  "description": "Build a REST API with Flask and SQLite",
  "done": false
}
```

## Usage Examples

### Get all tasks
```bash
curl http://localhost:5000/tasks
```

### Create a task
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a REST API"}'
```

### Update a task
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

### Delete a task
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

## Error Responses

| Status Code | Meaning |
|-------------|---------|
| 200 | Success |
| 201 | Created successfully |
| 400 | Bad request (e.g. missing title) |
| 404 | Task not found |
