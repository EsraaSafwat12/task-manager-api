Task Manager API
A lightweight RESTful API built with Flask and SQLite for managing tasks. Supports full CRUD operations via HTTP endpoints.
Tech Stack

Python 3.8+
Flask
SQLite
Werkzeug

Features

Create, retrieve, update, and delete tasks
Persistent storage using SQLite
JSON responses
Input validation with proper error messages
HTTP status codes (200, 201, 400, 404)

Project Structure
task-manager-api/
│
├── app.py          # Main application file
├── tasks.db        # SQLite database (auto-created on first run)
└── README.md
Getting Started
1. Clone the repository
bashgit clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
2. Install dependencies
bashpip install flask werkzeug
3. Run the application
bashpython app.py
The API will be running at http://localhost:5000
API Endpoints
MethodEndpointDescriptionGET/tasksGet all tasksGET/tasks/<id>Get a single task by IDPOST/tasksCreate a new taskPUT/tasks/<id>Update an existing taskDELETE/tasks/<id>Delete a task
Task Schema
json{
  "id": 1,
  "title": "Learn Flask",
  "description": "Build a REST API with Flask and SQLite",
  "done": false
}
Usage Examples
Get all tasks
bashcurl http://localhost:5000/tasks
Create a task
bashcurl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a REST API"}'
Update a task
bashcurl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
Delete a task
bashcurl -X DELETE http://localhost:5000/tasks/1
Error Responses
Status CodeMeaning200Success201Created successfully400Bad request (e.g. missing title)404Task not found
