from typing import Optional
from fastapi import FastAPI, Request
import pandas_datareader as pdr
from pandas_datareader.iex.ref import SymbolsReader
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

'''
    The Backend will be supported with FastAPI
'''

def get_tickers():
    '''
        List of all available tickers
    '''
    symbols = SymbolsReader().read()
    symbols = symbols['symbol'].values.tolist()
    symbols = ','.join(symbols)
    return symbols

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
app.mount("/static", StaticFiles(directory = 'static'), name = 'static')
templates = Jinja2Templates(directory = 'templates')

@app.get('/')
async def main_page(request: Request):

    # fetch tickers
    simboli = get_tickers()

    return templates.TemplateResponse('index.html', {'request' : request, 'tickers' : simboli})

