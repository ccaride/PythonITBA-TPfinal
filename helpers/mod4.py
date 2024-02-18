import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def filter(inpts):
    engine = create_engine('sqlite:///Database.db')  
    print("Database opened")

    conn = engine.connect()

    ddbb = pd.read_sql_table("main", conn)
    ddbb_fil = ddbb[(ddbb["Ticker"] == inpts[0]) & (ddbb["Date"] >= inpts[1]) & (ddbb["Date"] <= inpts[2])]
    
    engine.dispose() 
    print("Database closed")

    return ddbb_fil

def report(ddbb_fil):
    if ddbb_fil.empty:
        print('DataFrame is empty!') 
    else:
        print(ddbb_fil)

def graphic(ddbb_fil):
    if ddbb_fil.empty:
        print('DataFrame is empty!') 
    else:
        fig = px.line(ddbb_fil, x= 'Date',
              y='Close',
              color='Ticker',
              title="Stock Performance")
        fig.show()
