import requests as r
import time as t
bud=1000
while True:
    def data1():
        response1 = r.get('https://bitbay.net/API/Public/BTC/ticker.json')
        return response1.json()

    def data2():
        response2 = r.get('https://blockchain.info/ticker')
        return response2.json()

    def data3():
        response3 = r.get('https://www.bitstamp.net/api/ticker')
        return response3.json()

    def data4():
        response4 = r.get('https://cex.io/api/ticker/BTC/USD')
        return response4.json()

    bitbay=data1()
    sell1=bitbay['ask']
    buy1=bitbay['bid']
    blockchain=data2()
    sell2=blockchain["USD"]['sell']
    buy2=blockchain["USD"]['buy']
    bitstamp=data3()
    sell3=bitstamp['ask']
    buy3=bitstamp['bid']
    cex=data4()
    sell4=cex['ask']
    buy4=cex['bid']

    def comparison_buy():
        x=float(buy1)*0.0025
        y=float(buy2)*0.0027
        z=float(buy3)*0.0024
        w=float(buy4)*0.0025
        o=max(x,y,z,w)
        if o==x:
            v='bitbay'
            k=buy1
        elif o==y:
            v='blockchain'
            k=buy2
        elif o==z:
            v='bitstamp'
            k=buy3
        else:
            v='cex'
            k=buy4
        return o,v,t,k

    def comparison_sell():
        x=float(sell1)*0.0025
        y=float(sell2)*0.0027
        z=float(sell3)*0.0024
        w=float(sell4)*0.0025
        o=min(x,y,z,w)
        if o==x:
            v='bitbay'
            k=sell1
        elif o==y:
            v='blockchain'
            k=sell2
        elif o==z:
            v='bitstamp'
            k=sell3
        else:
            v='cex'
            k=sell4
        return o,v,t,k
    
    p=bud/b[3]

    b=comparison_buy()
    c=comparison_sell()

    print('Najlepiej kupić w',c[1],'po kursie',c[3],'i sprzedać w',b[1],'po kursie',b[3],'\n','z profitem wynoszącym na',p,'BTC',p*(b[0]-c[0]))
    bud=bud+p*(b[0]-c[0])
    print(bud,p)
    t.sleep(5)


