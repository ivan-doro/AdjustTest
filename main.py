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

    select_query = ''
    filter_query = ''
    groupby_query = ''
    sort_query = ''

    if request_data:
        if 'select' in request_data and len(request_data['select']) != 0:
            select_query = 'SELECT '
            for column in request_data['select']:
                select_query += column + ', '

            # remove the last ', '
            select_query = select_query[:-2]

        if 'filter' in request_data and len(request_data['filter']) != 0:
            filter_query = 'WHERE '
            # json array with all the filter parameters
            filter_received = request_data['filter']
            # adding all the filters to the query
            if 'date_from' in filter_received:
                filter_query += 'date > ' + filter_received['date_from'] + ' AND '
            if 'date_to' in filter_received:
                filter_query += 'date < ' + filter_received['date_from'] + ' AND '
            if 'country' in filter_received:
                filter_query += 'country is ' + filter_received['date_from'] + ' AND '
            if 'os' in filter_received:
                filter_query += 'os is ' + filter_received['date_from'] + ' AND '

            # remove the last 'AND '
            groupby_query = filter_query[:-4]

        if 'groupby' in request_data and len(request_data['groupby']) != 0:
            groupby_query = 'GROUP BY '
            for column in request_data['groupby']:
                select_query += column + ', '

            # remove the last ', '
            groupby_query = select_query[:-2]

        if 'sort' in request_data and len(request_data['sort']) == 2:
            sort_query = 'ORDER BY ' + request_data['sort']['column']
            if request_data['sort']['asc'] == "false":
                sort_query += ' DESC'

    return ''.join(str(sort_query))


if __name__ == '__main__':
    app.run()
