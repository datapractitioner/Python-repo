from typing import Optional
from fastapi import FastAPI, Request, Form
import pandas_datareader as pdr
from pandas_datareader.iex.ref import SymbolsReader
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas_datareader.data as web

from bokeh.plotting import figure
from bokeh.embed import components


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
    fetched = web.DataReader(ticker, 'yahoo')
    return fetched

def create_graph():
    '''
        Create and return graph components
    '''
    return

app = FastAPI()
app.mount("/static", StaticFiles(directory = 'app/static'), name = 'static')
templates = Jinja2Templates(directory = 'app/templates')

simboli = get_tickers()

@app.get('/')
async def main_page(request: Request):
    # fetch tickers
    #simboli = get_tickers()
    #print('dakdakhdadhakdhas')
    return templates.TemplateResponse('index.html', {'request' : request, 'tickers' : simboli})

@app.post('/')
async def selected_ticker(request : Request, myCountry : str = Form(...)):
    print(myCountry)
    print('Retrieving data ...')

    data = fetch_data(myCountry).reset_index()

    print(data.head())

    inc = data.Close > data.Open
    dec = data.Open > data.Close
    w = 12*60*60*1000 # half day in ms

    # create candlestick
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    p = figure(x_axis_type = 'datetime', tools = TOOLS,
               plot_width = 1000, title = "{} Candlestick".format(myCountry))
    p.xaxis.major_label_orientation = 3.14/4
    p.grid.grid_line_alpha=0.3

    p.segment(data.Date, data.High, data.Date, data.Low, color="black")
    p.vbar(data.Date[inc], w, data.Open[inc], data.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(data.Date[dec], w, data.Open[dec], data.Close[dec], fill_color="#F2583E", line_color="black")

    script, div = components(p)

    return templates.TemplateResponse('index.html', {'request' : request, 'tickers' : simboli,
                                      'div_image' : div, 'script_image' : script})
