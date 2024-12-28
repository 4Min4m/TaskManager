import requests

response = requests.get("https://taskmanager-app-kjk3.onrender.com/tasks")
print(response.json())

new_task = {"title":"Learn Flask","Description":"Study Flask"}
response = requests.post("https://taskmanager-app-kjk3.onrender.com/tasks", json=new_task)
print(response.json())