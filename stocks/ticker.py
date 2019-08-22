from . import app
import requests
from . import redis_store
import json


HOST = 'http://www.pse.com.ph/stockMarket/home.html'
HEADERS = {'Referer': HOST}

def retrieve_stocks():
    print("Getting new stocks")
    try:
        r = requests.get(HOST + '?method=getSecuritiesAndIndicesForPublic&ajax=true', headers=HEADERS, timeout=5)
        stocks = r.json()
        if len(stocks) !=  0:
            price_as_of = stocks[0]['securityAlias']
            for stock in stocks:
                stock['priceAsOf'] = price_as_of
                redis_store.set('stocks:' + stock['securitySymbol'], json.dumps(stock))

        stocks = json.dumps(stocks[1:])
        redis_store.set('stocks:all', stocks)
    except requests.exceptions.Timeout as err:
         print(err)    