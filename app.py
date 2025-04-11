from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            calculation = request.form["calculation"]
            result = eval(calculation)
        except Exception as e:
            result = "Error: " + str(e)
    return render_template("index.html", result=result)

@app.route("/calculate", methods=["GET"])
def calculate():
    expression = request.args.get("expression", "")
    try:
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    return result

if __name__ == "__main__":
    app.run(debug=True)
