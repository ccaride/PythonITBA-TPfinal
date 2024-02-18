from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd

def summary():
    engine = create_engine('sqlite:///Database.db')  
    print("Database opened")

    conn = engine.connect()

    ddbb = pd.read_sql_table("main", conn)
    ddbb_res = ddbb.groupby('Ticker').Date.agg(['min', 'max'])
    print(ddbb_res)

    engine.dispose()
    print("Database closed")


def request(tick, SD, ED):

    engine = create_engine('sqlite:///Database.db')  
    print("Database opened")

    conn = engine.connect()

    data = yf.download(tick, start=SD, end=ED)
    print("Data downloaded")

    data.insert(0, "Ticker", tick)
    data.to_sql('main', engine, if_exists='append', index=True)
    print("Data saved in the Database")

    check_dupli = pd.read_sql_table("main", conn)
    check_dupli.drop_duplicates(inplace=True)
    check_dupli.to_sql('main', engine, if_exists='replace', index=False)

    engine.dispose()
    print("Database closed")

