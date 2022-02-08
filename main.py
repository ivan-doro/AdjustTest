from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/hello/')
def welcome():
    return "Hello World!"


# @app.route('/dataset', methods=['GET'])
# def filter_data():
#
#     filter = None
#     groupby = None
#     sort = None
#
#     if 'filter' in request.args:
#         filter = request.args['filter']
#
#     if 'groupby' in request.args:


if __name__ == 'main':
    app.run()
