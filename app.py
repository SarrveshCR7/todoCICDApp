from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            # Get the input from the form
            calculation = request.form["calculation"]
            # Evaluate the expression and calculate the result
            result = eval(calculation)
        except Exception as e:
            result = "Error: " + str(e)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
