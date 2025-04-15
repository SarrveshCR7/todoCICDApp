from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            calculation = request.form["calculation"]
            result = eval(calculation)
        except Exception:
            result = "Invalid input. Please enter a valid mathematical expression."
    return render_template("index.html", result=result)

@app.route("/calculate")
def calculate():
    expression = request.args.get("expression", "")
    user_answer = request.args.get("answer", "")
    try:
        actual_answer = str(eval(expression))
        if user_answer == actual_answer:
            return "Correct"
        else:
            return f"Incorrect. The correct answer is: {actual_answer}"
    except Exception:
        return "Invalid input. Please enter a valid mathematical expression."
