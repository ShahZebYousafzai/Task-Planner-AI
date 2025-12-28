# Simple Task Manager Web App

A beautiful and functional task manager built with Python Flask

## Features

* Add New Task
* Mark task as complete/incomplete
* Delete Task
* Persistent storage (JSON file)
* Modern and Responsive UI
* Task statistics
* RESTful API Endpoints

## Project Structure

```
D:\Projects\Dhruv\
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template
├── requirements.txt    # Python dependencies
├── tasks.json          # Task storage (created automatically)
└── README.md          # This file
```

## Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Storage**: JSON file (can be easily upgraded to SQLite or Supabase PostgreSQL)

## Installation

1. Make sure you have Python 3 installed on your system

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Start managing your tasks!

## API Endpoints

* `GET /` - Main web interface
* `POST /add` - Add a new task
* `POST /toggle/<task-id>` - Toggle task completion
* `DELETE /delete/<task-id>` - Delete a task
* `GET /api/tasks` - Get all tasks as JSON

## Usage

### Adding a Task
1. Type your task in the input field
2. Click "Add Task" or press Enter

### Completing a Task
- Click the checkbox next to a task to mark it as complete
- Click again to mark it as incomplete

### Deleting a Task
- Click the "Delete" button next to the task you want to remove

### Viewing Statistics
- The dashboard shows:
  - Total number of tasks
  - Number of completed tasks
  - Number of pending tasks

## Future Enhancements

- Add task categories/tags
- Set due dates and reminders
- User authentication
- Upgrade to SQLite or PostgreSQL database
- Add task priority levels
- Search and filter functionality
- Dark mode toggle

## License

MIT License
