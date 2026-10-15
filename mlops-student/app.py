```python
from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

# Load the trained ML model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Result Predictor</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            margin: 0;
            padding: 30px 15px;
        }

        .card {
            background: white;
            max-width: 550px;
            margin: 20px auto;
            padding: 28px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        }

        h1 {
            color: #1769aa;
            text-align: center;
            font-size: 28px;
        }

        .description {
            text-align: center;
            color: #555;
            line-height: 1.5;
        }

        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #333;
        }

        input,
        button {
            width: 100%;
            padding: 12px;
            margin-top: 8px;
            border-radius: 6px;
            font-size: 16px;
        }

        input {
            border: 1px solid #ccc;
        }

        input:focus {
            outline: 2px solid #1769aa;
            border-color: #1769aa;
        }

        button {
            background: #1769aa;
            color: white;
            border: none;
            cursor: pointer;
            margin-top: 24px;
            font-weight: bold;
        }

        button:hover {
            background: #0d4f85;
        }

        .result {
            margin-top: 22px;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            border-radius: 8px;
            background: #e8f3ff;
            color: #1769aa;
        }

        .version {
            text-align: center;
            margin-top: 22px;
            color: #666;
            font-size: 14px;
        }

        hr {
            border: 0;
            border-top: 1px solid #eee;
            margin-top: 24px;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1>Student Result Predictor</h1>

        <p class="description">
            Enter the student's details to predict Pass or Fail
            using a Machine Learning model.
        </p>

        <form method="POST">
            <label for="hours">Study Hours per Day</label>
            <input
                type="number"
                id="hours"
                name="hours"
                min="0"
                max="24"
                step="0.5"
                required
            >

            <label for="attendance">Attendance (%)</label>
            <input
                type="number"
                id="attendance"
                name="attendance"
                min="0"
                max="100"
                step="1"
                required
            >

            <label for="marks">Internal Marks (out of 100)</label>
            <input
                type="number"
                id="marks"
                name="marks"
                min="0"
                max="100"
                step="1"
                required
            >

            <button type="submit">Predict Result</button>
        </form>

        {% if prediction %}
            <div class="result">
                Prediction: {{ prediction }}
            </div>
        {% endif %}

        <hr>

        <p class="version">
            Model Version: 2.0
        </p>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            attendance = float(request.form["attendance"])
            marks = float(request.form["marks"])

            # Validate input values
            if not 0 <= hours <= 24:
                raise ValueError("Study hours must be between 0 and 24.")

            if not 0 <= attendance <= 100:
                raise ValueError("Attendance must be between 0 and 100.")

            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            # Predict student result
            result = model.predict([[hours, attendance, marks]])[0]
            prediction = "Pass" if result == 1 else "Fail"

        except (ValueError, KeyError):
            prediction = "Please enter valid student details."

    return render_template_string(HTML, prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
```
