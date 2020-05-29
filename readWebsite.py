from lxml import html
import requests, time

stocks = [['S&P', 'https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC'], ['DOW', 'https://finance.yahoo.com/quote/%5EDJI?p=^DJI'], ['NASDAQ', 'https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC'], ['Gold', 'https://finance.yahoo.com/quote/GC=F?p=GC=F']]


for stock in stocks:
    page = requests.get(stock[1])

    tree = html.fromstring(page.content)
    st = str(page.content)
    findStr = '"regularMarketPrice":{"raw":'
    i0 = st.find(findStr)
    startI = len(findStr) + i0
    endI = st.find(",", startI)

    print(stock[0], st[startI:endI])