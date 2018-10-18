from flask import Flask, render_template, request, redirect

app = Flask(__name__)


tasks = {
	1 : {
		"id": 1,
		"name": "Get milk",
		"description": "Make sure it's low fat",
		"is_urgent": False
	},
	2 : {
		"id": 2,
		"name": "Get tea",
		"description": "Make sure it's Barry's",
		"is_urgent": True
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
    		"is_urgent": "is_request" in request.form
        }
        
        tasks[next_id] = new_item
        next_id += 1
        return redirect("/")
    else:
         return render_template("todo_form.html")     



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)