from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    review_text = request.form['review']

    # Make a request to the FastAPI service
    api_url = 'http://127.0.0.1:8000//make_predictions'
    payload = {'input': review_text}
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        prediction = response.json()['prediction']
        return render_template('result.html', review=review_text, prediction=prediction)
    else:
        return 'Error making prediction'

if __name__ == '__main__':
    app.run(debug=True)
