from flask import Flask, render_template, request, flash, url_for
import json
import requests

api = 'f89fed0d4d207b879a2d'

byn = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_BYN&compact=ultra&apiKey={api}')
rub = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_RUB&compact=ultra&apiKey={api}')
usd = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_USD&compact=ultra&apiKey={api}')

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route('/')
def index():
    info_bun = byn.json()['UAH_BYN']
    info_rub = rub.json()['UAH_RUB']
    info_usd = usd.json()['UAH_USD']
    return render_template('main.html', byn=(int((info_bun * 40) * 100) / 100), rub=(int((info_rub * 40) * 100) / 100),
                           usd=(int((info_usd * 40) * 100) / 100))

@app.errorhandler(404)
def page_not_found(e):
    # вывод html
    return render_template('404.html'), 404

if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5007)
    app.run()
