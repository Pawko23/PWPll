from flask import Flask, render_template_string

app = Flask(__name__)

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route("/")
def home():
    return render_template_string("""
        <h1>Welcome in my mini portal</h1>
        <p><a href="/about">About</a></p>
        <p><a href="/users">Users</a></p>
    """)

@app.route("/about")
def about():
    return "<h1>About</h1><p>Simple mini portal created in flask, that we created with learning purpose</p>"

@app.route("/users")
def user_list():
    user_links = "".join(
        f'<li><a href="/user/{user_id}">{data["name"]}</a></li>'
        for user_id, data in users.items()
    )
    return f"<h1>Users</h1><ul>{user_links}</ul>"

@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return f"<h1>{user['name']}, {user['age']} yo</h1>"
    else:
        return "<h1>User does not exist</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)