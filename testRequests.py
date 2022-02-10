request1 = {
    "select": ["channel", "country", "impressions", "clicks"],
    "filter": {
        "date_to": "2017-06-01"

    },
    "groupby": ["channel", "country"],
    "sort": {
        "column": "clicks",
        "asc": "false"
    }
}

request2 = {
    "select": ["date", "installs"],
    "filter": {
        "date_from": "2017-05-01",
        "date_to": "2017-05-30",
        "os": "ios"
    },
    "groupby": ["date"],
    "sort": {
        "column": "date",
        "asc": "true"
    }
}

request3 = {
    "select": ["os", "revenue"],
    "filter": {
        "date_from": "2017-06-01",
        "country": "US"
    },
    "groupby": ["os"],
    "sort": {
        "column": "revenue",
        "asc": "false"
    }
}

request4 = {
    "select": ["channel", "spend", "cpi"],
    "filter": {
        "country": "CA"
    },
    "groupby": ["channel"],
    "sort": {
        "column": "cpi",
        "asc": "false"
    }

}
