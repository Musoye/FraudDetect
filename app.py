from flask import Flask, request, jsonify, render_template
from load_model import predict
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s'
)


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
        ipaddr = dat['ipaddr'].replace('.', '')
        uacc = dat['uacc']
        dacc = dat['dacc']
        age = dat['age']
        tdate = dat['tdate']
        payment_type = dat['payment_type']
        oldbalance = dat['obalance']
        newbalance = dat['nbalance']
        withdraw = dat['withdraw']
        print(withdraw)
        ans = predict(ipaddr, uacc, dacc, age, tdate, payment_type, oldbalance, newbalance, withdraw)
        print(ans)
        message_format = F'{ipaddr} {uacc} {dacc} {age} {tdate} {payment_type} {oldbalance} {newbalance}\
            {withdraw} {ans}'
        app.logger.info(message_format)
        return jsonify({'isFraud': ans})

@app.route('/api/predict', methods=['POST'])
def post_api_predict():
    if request.method == 'POST':
        dat = request.get_json()
        ipaddr = dat['ipaddr'].replace('.', '')
        uacc = dat['uacc']
        dacc = dat['uacc']
        age = dat['age']
        tdate = dat['tdate']
        payment_type = dat['payment_type']
        oldbalance = dat['obalance']
        newbalance = dat['nbalance']
        withdraw = dat['withdraw']
        ans = predict(ipaddr, uacc, dacc, age, tdate, payment_type, oldbalance, newbalance, withdraw)
        print(ans)
        message_format = F'{ipaddr} {uacc} {dacc} {age} {tdate} {payment_type} {oldbalance} {newbalance}\
            {withdraw} {ans}'
        app.logger.info(message_format)
    return jsonify({'isFraud': ans})
    

if __name__ == '__main__':
    app.run(debug=True)