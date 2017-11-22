from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())

  # FETCH THE CRYPTO NAME
  crypto_name = data['conversation']['memory']['crypto']['value']
  
  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
