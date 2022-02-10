import flask
from flask import Flask, jsonify, request
import sqlite3 as sl
from tabulate import tabulate

import testRequests

app = Flask(__name__)


@app.route('/hello/')
def welcome():
    return "Hello World!"


@app.route('/dataset/', methods=['POST'])
def regular_filter():
    request_data = request.get_json()
    return filter_data(request_data)


@app.route('/dataset/case1', methods=['GET'])
def filter_data_case1():
    return filter_data(testRequests.request1)


@app.route('/dataset/case2', methods=['GET'])
def filter_data_case2():
    return filter_data(testRequests.request2)


@app.route('/dataset/case3', methods=['GET'])
def filter_data_case3():
    return filter_data(testRequests.request3)


@app.route('/dataset/case4', methods=['GET'])
def filter_data_case4():
    return filter_data(testRequests.request4)


@app.errorhandler(404)
def page_not_found(e):
    return "Aborted. Check your request"


def filter_data(request_data):

    select_query = ''
    filter_query = ''
    groupby_query = ''
    sort_query = ''

    if request_data:
        if 'select' in request_data and len(request_data['select']) != 0:
            select_query = 'SELECT '
            for i in range(0, len(request_data['select'])):
                select_query += request_data['select'][i] + ', '

            if 'groupby' in request_data and len(request_data['groupby']) != 0:
                if 'impressions' in select_query:
                    select_query = select_query.replace('impressions', 'sum(impressions) AS impressions')
                    print(select_query)
                if 'clicks' in request_data['select']:
                    select_query = select_query.replace('clicks', 'sum(clicks) AS clicks')
                if 'installs' in request_data['select']:
                    select_query = select_query.replace('installs', 'sum(installs) AS installs')
                if 'spend' in request_data['select']:
                    select_query = select_query.replace('spend', 'sum(spend) AS spend')
                if 'revenue' in request_data['select']:
                    select_query = select_query.replace('revenue', 'sum(revenue) AS revenue')
                if 'cpi' in request_data['select']:
                    select_query = select_query.replace('cpi', 'sum(spend)/sum(installs) AS cpi')

            elif 'cpi' in select_query:
                select_query = select_query.replace('cpi', 'spend/installs AS cpi, ')
            # remove the last ', '
            select_query = select_query[:-2]
        else:
            flask.abort(404)

        if 'filter' in request_data and len(request_data['filter']) != 0:
            filter_query = ' WHERE '
            # json array with all the filter parameters
            filter_received = request_data['filter']
            # adding all the filters to the query
            if 'date_from' in filter_received:
                filter_query += 'date >= \'' + filter_received['date_from'] + '\' AND '
            if 'date_to' in filter_received:
                filter_query += 'date <= \'' + filter_received['date_to'] + '\' AND '
            if 'country' in filter_received:
                filter_query += 'country is \'' + filter_received['country'] + '\' AND '
            if 'os' in filter_received:
                filter_query += 'os is \'' + filter_received['os'] + '\' AND '

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

    result = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    result.insert(0, field_names)

    print(final_query)
    return tabulate(result, tablefmt='html')


if __name__ == '__main__':
    app.run()
