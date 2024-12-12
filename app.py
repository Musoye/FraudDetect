from flask import Flask, request, jsonify, render_template
from load_model import predict

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def get_predict():
    return render_template('land.html')

@app.route('/predict', methods=['POST'])
def post_predict():
    if request.method == 'POST':
        dat = request.form
        payment_type = dat['payment_type']
        oldbalance = dat['obalance']
        newbalance = dat['nbalance']
        withdraw = dat['withdraw']
        ans = predict(payment_type, oldbalance, newbalance, withdraw)
    return jsonify({'isFraud': ans})

@app.route('/api/predict', methods=['POST'])
def post_api_predict():
    if request.method == 'POST':
        dat = request.get_json()
        payment_type = dat['payment_type']
        oldbalance = dat['obalance']
        newbalance = dat['nbalance']
        withdraw = dat['withdraw']
        ans = predict(payment_type, oldbalance, newbalance, withdraw)
    return jsonify({'isFraud': ans})
    

if __name__ == '__main__':
    app.run(debug=True)