from flask import Flask, render_template, request, redirect

app = Flask(__name__)


tasks = {
	1 : {
		"id": 1,
		"name": "Get milk",
		"description": "Make sure it's low fat",
		"is_urgent": False,
		"is_done": False
	},
	2 : {
		"id": 2,
		"name": "Get tea",
		"description": "Make sure it's Barry's",
		"is_urgent": True,
		"is_done": True
	},
}

next_id = 3

@app.route("/")
def show_index():
    return render_template("index.html", tasks=tasks.values())


@app.route("/add", methods=["GET", "POST"])
def show_form():
    if request.method == "POST":
        global next_id # Bit hacky, but required in Python3.
        new_item = {
            "id": next_id,
    		"name": request.form["add_name"],
    		"description": request.form["add_description"],
    		"is_urgent": "add_urgent" in request.form,
    		"is_done": "add_done" in request.form
        }
        
        tasks[next_id] = new_item
        next_id += 1
        return redirect("/")
    else:
         return render_template("add_task_form.html")     


@app.route("/edit/<int:task_num>", methods=["GET", "POST"])
def show_edit_form(task_num):
    if request.method == "POST":
        edited_item = {
            "id": task_num,
    		"name": request.form["edit_name"],
    		"description": request.form["edit_description"],
    		"is_urgent": "edit_urgent" in request.form,
    		"is_done": "edit_done" in request.form
        }
        
        tasks[task_num] = edited_item
        return redirect("/")
    else:    
        return render_template("edit_task_form.html", tasks=tasks[task_num])


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)