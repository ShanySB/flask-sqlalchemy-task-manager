from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    tasks = Task.query.all()
    return render_template("task.html", tasks=tasks)