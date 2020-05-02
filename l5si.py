import requests
import numpy
import time


def BTC_stats():

    response1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
    return response1.json()

def LTC_stats():
   
    response2 = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd/")
    return response2.json()

def BCH_stats():
   
    response3 = requests.get("https://www.bitstamp.net/api/v2/ticker/bchusd/")
    return response3.json()

def XRP_stats():
   
    response4 = requests.get("https://www.bitstamp.net/api/v2/ticker/xrpusd/")
    return response4.json()

def ETH_stats():

    response5 = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd/")
    return response5.json()

def sort(f_BTC, f_LTC, f_BCH, f_XRP, f_ETH):
   
    value = []
    name = []
   
    value.append(f_BTC)
    value.append(f_LTC)
    value.append(f_BCH)
    value.append(f_XRP)
    value.append(f_ETH)
   
    name.append("BTC")
    name.append("LTC")
    name.append("BCH")
    name.append("XRP")
    name.append("ETH")
   
    for i in range(4):
        for i in range(4):
            if value[i]<value[i+1]:
               
                a=value[i]
                value[i]=value[i+1]
                value[i+1]=a
               
                b=name[i]
                name[i]=name[i+1]
                name[i+1]=b
   
    return value, name


def stats():


    while True:
       
        BTC = BTC_stats()
        h_BTC = float(BTC["high"])
        l_BTC = float(BTC["low"])
        f_BTC = ((h_BTC/l_BTC)-1)*100

        LTC = LTC_stats()
        h_LTC = float(LTC["high"])
        l_LTC = float(LTC["low"])
        f_LTC = ((h_LTC/l_LTC)-1)*100
       
        BCH = BCH_stats()
        h_BCH = float(BCH["high"])
        l_BCH = float(BCH["low"])
        f_BCH = ((h_BCH/l_BCH)-1)*100
       
        XRP = XRP_stats()
        h_XRP = float(XRP["high"])
        l_XRP = float(XRP["low"])
        f_XRP = ((h_XRP/l_XRP)-1)*100
        
        ETH = ETH_stats()
        h_ETH = float(ETH["high"])
        l_ETH = float(ETH["low"])
        f_ETH = ((h_ETH/l_ETH)-1)*100
       
        x = sort(f_BTC, f_LTC, f_BCH, f_XRP, f_ETH)
       
        for i in range(5):
            if x[0][i]>0:
                print(x[1][i],"+",x[0][i],"%")
            else:
                print(x[1][i],"-",x[0][i],"%")
       
        time.sleep(300)

stats()