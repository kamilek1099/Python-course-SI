import requests as r
a=0
def data1():
    response1 = r.get('https://bitbay.net/API/Public/BTC/ticker.json')
    return response1.json()

def data2():
    response2 = r.get('https://blockchain.info/ticker')
    return response2.json()

def order():
    response = r.get('https://bitbay.net/API/Public/BTC/orderbook.json')
    return response.json()

orderbook=order()

for i in range(5):
    print(orderbook['bids'][i],'\n')
    print(orderbook['asks'][i],'\n')

def info():
    bitbay=data1()
    blockchain=data2()
    sale1=bitbay['ask']
    sale2=blockchain["USD"]['sell']
    buy1=bitbay['bid']
    buy2=blockchain["USD"]['buy']
    if sale1<sale2:
        print("Buy on Bitbay")
    else:
        print("Buy on blockchain")
    if buy1>buy2:
        print("Sell on Bitbay")
    else:
        print("Sell on blockchain")    
    
info()