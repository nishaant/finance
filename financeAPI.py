from bottle import run, get
import requests
import datetime



#Api for getting the stock details
@get('/stock/<stockName>')
def getAll(stockName):
    apiEndPoint = "https://www.alphavantage.co/query"
    index = "Time Series (Daily)"
    PARAMS = {'function':'TIME_SERIES_DAILY',
              'interval':'1min',
              'apikey':'Y42E8E55N7TIQ2UZ',
              'symbol':'NSE:' + str(stockName)}
    response = requests.get(url = apiEndPoint, params = PARAMS)
    data = response.json()
    todayDate = datetime.date.today()
    lastActiveMarketDate = todayDate;
    weekday = todayDate.weekday()
    if weekday == 5 or weekday == 6:
        delta = datetime.timedelta(days = (weekday - 4))
        lastActiveMarketDate = todayDate - delta;
    print lastActiveMarketDate
    return data[index][str(lastActiveMarketDate)]


run(reloader=True, debug=True)

