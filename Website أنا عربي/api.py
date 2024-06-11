# api.py
from flask import Flask, request, jsonify
from preprocessing import predict_label

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    predicted_label = predict_label(text)
    return jsonify({'predicted_label': predicted_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
