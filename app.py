from flask import Flask, jsonify, request

app = Flask(__name__)

#TempDataToSaveTasks
tasks = [
    {"id":1, "title":"Learning Flask", "completed": False},
    {"id":2, "title":"Practicing Docker", "completed": False},
]

#Homepage
@app.route('/')
def home():
    return "Welcome", 200

#ToLearnAPI
@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

#ToCreateNewAPI
@app.route('/tasks',methods=['POST'])
def create_tasks():
    new_task= request.json
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

#Execute
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')