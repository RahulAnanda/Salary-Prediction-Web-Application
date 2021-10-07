from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/predict_salary', methods=['POST'])
def predict_salary():
    total_exp = float(request.form['total_exp'])

    response = jsonify({
        'estimated_salary': util.get_estimated_salary(total_exp)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Salary Prediction...")
    util.load_saved_artifacts()
    app.run()
