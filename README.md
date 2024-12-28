# Project Documentation: Flask & PyTorch Web Application

## **Project Overview**
This document tracks the development of a Flask-based web application integrated with PyTorch for deep learning functionalities. The application is deployed on Render and will be incrementally improved to include UI, database integration, security measures, containerization, and Kubernetes deployment.

### **Initial Goals**
1. Create and deploy a basic Flask web application.
2. Develop APIs to manage tasks (GET/POST operations).
3. Deploy the application to Render for live access.
4. Plan further development to include UI, integration with a deep learning model, and other features.

---

## **Development Phases**

### **Phase 1: Setting Up the Basic Web Application**
- **Tasks Completed:**
  - Built a basic Flask application with APIs for task management.
  - Added endpoints:
    - `/`: Displays a "Welcome" message.
    - `/tasks` (GET): Returns a list of tasks in JSON format.
    - `/tasks` (POST): Accepts a JSON object to create a new task.
  - Deployed the application to Render for live access.

- **Code Example:**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build an API", "done": False}
]

@app.route('/')
def home():
    return "Welcome", 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def create_tasks():
    new_task = request.json
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201
```

### **Phase 2: Troubleshooting Deployment Issues**
- **Challenges Faced:**
  1. **`url_quote` ImportError:**
     - Cause: Deprecated `url_quote` function in Werkzeug.
     - Solution: Updated Flask and Werkzeug dependencies to compatible versions.
  2. **Port Binding Error on Render:**
     - Cause: Render failed to detect the correct port.
     - Solution: Explicitly specified the port using the `PORT` environment variable in the `app.run()` method during development.

- **Outcome:**
  - Successfully deployed the web application with the "Welcome" message accessible via the live URL.

### **Phase 3: Planning Advanced Features**
- **Planned Features:**
  1. **User Interface (UI):**
     - Design using Figma.
     - Implement with React or a similar framework.
  2. **Deep Learning Model Integration:**
     - Build and train a PyTorch model.
     - Provide access to the model via API endpoints.
  3. **Database Integration:**
     - Use PostgreSQL or MongoDB for persistent data storage.
  4. **Security Improvements:**
     - Add authentication and role-based access control.
  5. **Containerization:**
     - Use Docker for packaging the application.
  6. **Kubernetes Deployment:**
     - Deploy the containerized application using Kubernetes.
  7. **Monitoring and Logging:**
     - Implement Prometheus and Grafana for performance monitoring.

---

## **Challenges and Solutions**
### **1. Import Errors**
- **Issue:** Deprecated `url_quote` function caused ImportError.
- **Solution:** Updated `Flask` and `Werkzeug` to compatible versions and locked dependency versions in `requirements.txt`.

### **2. Deployment Errors**
- **Issue:** Render failed to bind to the correct port during deployment.
- **Solution:** Configured the `PORT` environment variable in Render settings and ensured the application read this variable.

### **3. Testing API Functionality**
- **Issue:** Testing POST requests to the `/tasks` endpoint initially failed.
- **Solution:** Created a separate `app_request.py` script for testing the API endpoints locally using `requests` library.

---

## **Next Steps**
1. Begin designing the UI with Figma.
2. Implement the UI with React and integrate it with the Flask backend.
3. Develop and train the PyTorch model to introduce deep learning functionalities.
4. Plan database integration and security enhancements.
5. Incrementally document each feature and update this document.

---

### **Document Maintenance**
This document will be regularly updated to include progress, challenges, and solutions, serving as a comprehensive guide for the project and its repository.
