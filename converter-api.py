from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_conversion(in_cur, out_cur):
    url = f'https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&ammount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])

    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1><p><small>API Endpoint Example: <em>/api/v1/eur_cny</em></small></p>'

@app.route('/api/v1/<in_cur>_<out_cur>')
def api(in_cur, out_cur):
    conversion = get_conversion(in_cur, out_cur)
    response ={'input_currency': in_cur, 'output_currency': out_cur, 'conversion_rate': conversion}

    return jsonify(response)


app.run(host='0.0.0.0')
