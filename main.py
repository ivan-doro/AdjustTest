from flask import Flask
from flask import request, jsonify
import json

app = Flask(__name__)


@app.route('/hello/')
def welcome():
    return "Hello World!"


@app.route('/dataset/', methods=['GET', 'POST'])
def filter_data():
    request_data = request.get_json()

    select = [None]*9
    filter = [None]*9
    groupby = [None]*9
    sort = [None]*9

    if request_data:
        if 'select' in request_data:
            select_received = request_data['select']
            if 'date' in select_received:
                select[0] = select_received['date']
            if 'chanel' in select_received:
                select[1] = select_received['chanel']
            if 'country' in select_received:
                select[2] = select_received['country']
            if 'os' in select_received:
                select[3] = select_received['os']
            if 'impressions' in select_received:
                select[4] = select_received['impressions']
            if 'clicks' in select_received:
                select[5] = select_received['clicks']
            if 'installs' in select_received:
                select[6] = select_received['installs']
            if 'spend' in select_received:
                select[7] = select_received['spend']
            if 'revenue' in select_received:
                select[8] = select_received['revenue']

    return ''.join(str(select))


if __name__ == '__main__':
    app.run()
