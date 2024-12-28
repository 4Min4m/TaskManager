from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for tasks
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Deploy on Render", "completed": True}
]

# Homepage
@app.route('/')
def home():
    return "Welcome to the Task Manager API!", 200

# Fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Invalid input"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')