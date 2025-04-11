from flask import Flask, request

app = Flask(__name__)

# Add a route for calculating
@app.route('/calculate')
def calculate():
    expression = request.args.get('expression')
    try:
        # Evaluate the expression safely
        result = str(eval(expression))  # Make sure to sanitize input in production!
    except Exception as e:
        result = str(e)
    return result

if __name__ == '__main__':
    app.run(debug=True)
