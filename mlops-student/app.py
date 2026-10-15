from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            margin: 40px auto;
            max-width: 550px;
            padding: 25px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 12px #cccccc;
        }
        input, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin: 8px 0 16px;
        }
        button {
            background: #1769aa;
            color: white;
            border: none;
            cursor: pointer;
        }
        .result {
            font-size: 22px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Student Result Predictor</h1>
        <p>Enter the student's details to predict Pass or Fail.</p>

        <form method="POST">
            <label>Study Hours per Day</label>
            <input type="number" name="hours" min="0" max="24"
                   step="0.5" required>

            <label>Attendance (%)</label>
            <input type="number" name="attendance" min="0" max="100"
                   step="1" required>

            <label>Internal Marks (out of 100)</label>
            <input type="number" name="marks" min="0" max="100"
                   step="1" required>

            <button type="submit">Predict Result</button>
        </form>

        {% if prediction %}
            <p class="result">Prediction: {{ prediction }}</p>
        {% endif %}

        <hr>
        <p>Model Version: 1.0</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])

        result = model.predict([[hours, attendance, marks]])[0]
        prediction = "Pass" if result == 1 else "Fail"

    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)