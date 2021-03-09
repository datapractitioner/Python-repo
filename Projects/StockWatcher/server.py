from typing import Optional
from fastapi import FastAPI
import pandas_datareader as pdr

'''
    The Backend will be supported with FastAPI
'''

def fetch_data(ticker):
    '''
        Fetch data of a particular ticker
    '''
    return

def create_graph():
    '''
        Create and return graph components
    '''
    return

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello' : 'World'}

