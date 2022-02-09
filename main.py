from flask import Flask, jsonify, request
import sqlite3 as sl
from tabulate import tabulate

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
            len_without_cpi = len(request_data['select']) - (1 if 'cpi' in request_data['select'] else 0)
            for i in range(0, len_without_cpi):
                select_query += request_data['select'][i] + ', '
            if 'cpi' in request_data['select']:
                select_query += 'spend/installs AS cpi, '

            # remove the last ', '
            select_query = select_query[:-2]

        if 'filter' in request_data and len(request_data['filter']) != 0:
            filter_query = ' WHERE '
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
            filter_query = filter_query[:-4]

        if 'groupby' in request_data and len(request_data['groupby']) != 0:
            groupby_query = ' GROUP BY '
            for column in request_data['groupby']:
                groupby_query += column + ', '

            # remove the last ', '
            groupby_query = groupby_query[:-2]

        if 'sort' in request_data and len(request_data['sort']) == 2:
            sort_query = ' ORDER BY ' + request_data['sort']['column']
            if request_data['sort']['asc'] == "false":
                sort_query += ' DESC'

    final_query = select_query + ' FROM dataset \n' + filter_query + groupby_query + sort_query
    conn = sl.connect('AdjustTest.db')
    cursor = conn.cursor()
    cursor.execute(final_query)

    print(final_query)
    return tabulate(cursor.fetchall(), tablefmt='html')


if __name__ == '__main__':
    app.run()
