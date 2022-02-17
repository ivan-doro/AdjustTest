Python(Flask) HTTP API.

This API (main.py) is taking the data from the sample database and capable of filtering, grouping and sorting it.

It listens to POST requests on 'http://127.0.0.1:5000/dataset'. The input parameters are received from a POST body as a 
JSON file in a certain format:

{

    "select" : list, 
    "filter" : {
        "date_from" : string in format YYYY-MM-DD,
        "date_to" : string in format YYYY-MM-DD,
        "channels": string,
        "countries" : string,
        "os" : string
    },
    "groupby" : list,
    "sort" : {
        "column" : string,
        "asc" : string ("true" of "false")
    }
}

There are also additional URLs for 4 examples:
http://127.0.0.1:5000/dataset/case1
http://127.0.0.1:5000/dataset/case2
http://127.0.0.1:5000/dataset/case3
http://127.0.0.1:5000/dataset/case4

