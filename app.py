from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

CATEGORIES = {
    'work': {'name': 'Work', 'color': '#3b82f6'},
    'personal': {'name': 'Personal', 'color': '#10b981'},
    'shopping': {'name': 'Shopping', 'color': '#f59e0b'},
    'health': {'name': 'Health', 'color': '#ef4444'},
    'learning': {'name': 'Learning', 'color': '#8b5cf6'},
    'general': {'name': 'General', 'color': '#6b7280'}
}


def load_tasks():
    """Load tasks from JSON file with backward compatibility"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            # Add default category to existing tasks
            for task in tasks:
                if 'category' not in task:
                    task['category'] = 'general'
            return tasks
    return []


def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


@app.route('/')
def index():
    """Main web interface with category filtering"""
    all_tasks = load_tasks()
    selected_category = request.args.get('category', 'all')

    # Filter tasks by category if specified
    if selected_category != 'all':
        tasks = [t for t in all_tasks if t.get('category', 'general') == selected_category]
    else:
        tasks = all_tasks

    return render_template(
        'index.html',
        tasks=tasks,
        all_tasks=all_tasks,
        categories=CATEGORIES,
        selected_category=selected_category
    )


@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task with category"""
    task_text = request.form.get('task')
    category = request.form.get('category', 'general')

    # Validate category
    if category not in CATEGORIES:
        category = 'general'

    if task_text:
        tasks = load_tasks()
        new_task = {
            'id': len(tasks) + 1,
            'text': task_text,
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'category': category
        }
        tasks.append(new_task)
        save_tasks(tasks)

    # Preserve category filter after adding
    selected_category = request.args.get('category', 'all')
    return redirect(url_for('index', category=selected_category))


@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)

    # Preserve category filter
    selected_category = request.args.get('category', 'all')
    return redirect(url_for('index', category=selected_category))


@app.route('/delete/<int:task_id>', methods=['POST', 'DELETE'])
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)

    # Preserve category filter
    selected_category = request.args.get('category', 'all')
    return redirect(url_for('index', category=selected_category))


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks as JSON"""
    tasks = load_tasks()
    return jsonify(tasks)


if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 to make the server accessible externally
    app.run(host='0.0.0.0', port=port, debug=False)
