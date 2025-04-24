from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route("/")
def home():
    return render_template_string("""
        <h1>To-Do App</h1>
        <p><a href="{{ url_for('tasks_view') }}">View tasks</a></p>
        <p><a href="{{ url_for('about') }}">About application</a></p>
    """)

@app.route("/about")
def about():
    return "<h1>About: </h1><p>Simple (and classic :v ) To-do List application, created in flask</p>"

@app.route("/tasks", methods=['GET', 'POST'])
def tasks_view():
    global task_id_counter
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            tasks.append({"id": task_id_counter, "title": title, "done": False})
            task_id_counter += 1
        return redirect(url_for("tasks_view"))
    return render_template_string("""
        <h1>Tasks list</h1>
        <form method="post">
            <input type="text" name="title" placeholder="New Task" required>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for task in tasks %}
                <li>
                    {% if task.done %}
                        <s>{{ task.title }}</s>
                    {% else %}
                        {{ task.title }}
                        <a href="{{ url_for('mark_done', task_id=task.id) }}">[Done]</a>
                    {% endif %}
                    <a href="{{ url_for('delete_task', task_id=task.id) }}">[Delete]</a>
                </li>
            {% endfor %}
        </ul>
        <a href="{{ url_for('home') }}">Home Page</a>
    """, tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    return redirect(url_for("tasks_view"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("tasks_view"))

if __name__ == "__main__":
    app.run(debug=True)