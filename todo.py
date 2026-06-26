from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Todo Pro</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Segoe UI, sans-serif;
}

body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#0f172a,#1e293b);
}

.container{
    width:700px;
    background:#111827;
    padding:30px;
    border-radius:20px;
    box-shadow:0 0 40px rgba(0,0,0,.5);
}

h1{
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.stats{
    display:flex;
    justify-content:space-between;
    color:#94a3b8;
    margin-bottom:20px;
}

form{
    display:flex;
    gap:10px;
}

input{
    flex:1;
    padding:15px;
    border:none;
    border-radius:10px;
    background:#1e293b;
    color:white;
}

button{
    padding:15px 25px;
    border:none;
    border-radius:10px;
    background:#3b82f6;
    color:white;
    cursor:pointer;
}

button:hover{
    opacity:.9;
}

ul{
    list-style:none;
    margin-top:20px;
}

li{
    background:#1e293b;
    margin-top:10px;
    padding:15px;
    border-radius:10px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.task{
    color:white;
}

.done{
    text-decoration:line-through;
    color:gray;
}

.actions{
    display:flex;
    gap:10px;
}

a{
    text-decoration:none;
}

.complete{
    color:#22c55e;
}

.delete{
    color:#ef4444;
}

</style>
</head>

<body>

<div class="container">

<h1>🚀 to do list </h1>

<div class="stats">
    <span>مجموع کار  ها : {{ total }}</span>
    <span>completed : {{ completed  }}</span>
</div>

<form action="/add" method="POST">
    <input
        type="text"
        name="task"
        placeholder="Enter a task..."
        required
    >
    <button>اضافه </button>
</form>

<ul>

{% for task in tasks %}

<li>

<span class="{% if task.done %}done{% endif %}">
{{ task.text }}
</span>

<div class="actions">

<a class="complete" href="/toggle/{{ loop.index0 }}">
✅
</a>

<a class="delete" href="/delete/{{ loop.index0 }}">
❌
</a>

</div>

</li>

{% endfor %}

</ul>

</div>

</body>
</html>
"""

@app.route("/")
def home():

    completed = sum(1 for t in tasks if t["done"])

    return render_template_string(
        HTML,
        tasks=tasks,
        total=len(tasks),
        completed=completed
    )


@app.route("/add", methods=["POST"])
def add():

    task = request.form.get("task")

    tasks.append({
        "text": task,
        "done": False
    })

    return redirect("/")


@app.route("/toggle/<int:index>")
def toggle(index):

    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]

    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):

    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    #  وقتی که میخاوم کد رو راه بندازیم باید  
    # python todo.py
    #  رو اجرا کنیم بعد کار میکنه 






    