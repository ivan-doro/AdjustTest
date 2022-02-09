import sqlite3 as sl
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(r'/Users/ivandorofeev/Documents/Programming/AdjustTest/dataset.csv')
    df = pd.DataFrame(data)
    print(df)
    con = sl.connect('AdjustTest.db')
    print('Connected')
    with con:
        con.execute('''
            CREATE TABLE dataset (
                date date,
                channel varchar(20),
                country varchar(10),
                os varchar(20),
                impressions integer,
                clicks integer,
                installs integer,
                spend float,
                revenue float
                )
        ''')
        print(len(df.index))
        print(type(int(df.iloc[1]['impressions'])))
        for row in range(0, len(df.index)):

            new_row = (df.iloc[row]['date'],
                       df.iloc[row]['channel'],
                       df.iloc[row]['country'],
                       df.iloc[row]['os'],
                       int(df.iloc[row]['impressions']),
                       int(df.iloc[row]['clicks']),
                       int(df.iloc[row]['installs']),
                       df.iloc[row]['spend'],
                       df.iloc[row]['revenue'],)

            con.execute('''
                INSERT INTO dataset (date, channel, country, os, impressions, clicks, installs, spend, revenue)
                VALUES (?,?,?,?,?,?,?,?,?)
                ''',
                        new_row
                        )
