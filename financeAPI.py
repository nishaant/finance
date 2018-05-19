from bottle import run, get
from flask import Flask
import requests
import datetime
from flask_cors import  CORS, cross_origin
import json

app = Flask(__name__)

@app.route('/stock/<stockName>', methods = ['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def getAll(stockName):

    apiEndPoint = "https://www.alphavantage.co/query"
    #return "nishaant"
    index = "Time Series (Daily)"
    PARAMS = {'function':'TIME_SERIES_DAILY',
              'interval':'1min',
              'apikey':'Y42E8E55N7TIQ2UZ',
              'symbol':'NSE:' + str(stockName)}
    print stockName
    response = requests.get(url=apiEndPoint, params=PARAMS)
    #return response
    jsonData = response.json()
    todayDate = datetime.date.today()
    lastActiveMarketDate = todayDate;
    weekday = todayDate.weekday()
    if weekday == 5 or weekday == 6:
        delta = datetime.timedelta(days=(weekday - 4))
        lastActiveMarketDate = todayDate - delta
    print lastActiveMarketDate
    dailyData = jsonData[index]
    keys = dailyData.keys()
    keys.sort(reverse = True)
    latestStockDetails = dailyData[keys[0]]
    text = json.dumps(latestStockDetails, separators=(',',':'))
    return text


if __name__ == '__main__':
    port = 9001
    app.run(host='127.0.0.1', port=port)

