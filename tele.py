#!/usr/bin/env python
# coding: utf-8

# In[25]:


pip install python-telegram-bot --upgrade # 텔레그램 연동 툴 
pip install -U pybithumb ##코인정보 얻어오는 툴 (빗썸)
pip install pyupbit #(업비트)
pip install ccxt #바이낸스
pip install python-kucoin#쿠코인
pip install currencyconverter #환율
#invalid syntax 뜬다면 이미 설치했는데 또 설치하라고해서 그럽니다.


# In[26]:


import ccxt #라이브러리 바이낸스 임포트 
import math
import pyupbit 
import pybithumb
import json
import requests
import telegram
import time
import threading 
from currency_converter import CurrencyConverter
import os
from multiprocessing import Process


# In[27]:


# 이코드는 실행되지않습니다. # 뒤에쓰면 컴퓨터가 읽지못합니다.

# 함수만들기를 원하신다면,
# def 아무거나():
#       bot = telegram.Bot(token='aa') #본인 코튼입력
#       chat_id = aaa #본인id 입력


    
#     while True:
        
#         빗섬을 원한다면
        
#         tickers = pybithumb.get_tickers() 
#         Bithumb = pybithumb.get_current_price("XRP")
        
#         쿠코인을 원한다면
        
#         d = CurrencyConverter()
#         base_url ='https://api.kucoin.com'
#         path='/api/v1/market/orderbook/level1'
#         r= requests.get(base_url+path,params={'symbol':'XRP-USDT'}) 
#         a=r.json()['data']['price']
#         KUCOIN = round(d.convert(a,'USD','KRW')) #환율위해
        
#         업비트를 원한다면
         
#         Upbit=round(pyupbit.get_current_price("USDT-XRP")) ## BTC자리에 다른 코인이름
#         Upbit_Exchange = CurrencyConverter()
#         UPBTI=round(Upbit_Exchange.convert(Upbit,'USD','KRW'))
        
#         바이낸스를 원한다면
        
        
#         binance = ccxt.binance() #바이낸스 객체 생성
#         ticker = binance.fetch_ticker('XRP/USDT')
#         binance_Exchange = CurrencyConverter() #환율을 위해
#         BINANCE=round(binance_Exchange.convert(ticker['last'],'USD','KRW'))
        
#         저 4개중에(Bithumb,KUCOIN,UPBTI,BINANCE) 2개 고른후 price1에는 기준으로 삼고싶은거 적으시고 price2에는 비교대상 적으세요
#         코인종류는  위에적혀있는 티커만 적으시면됩니다.
        
        
#         price1 = Bithumb
#         price2 = KUCOIN 
    
#         c=abs(math.floor((price1-price2)/price1 *10000)/100)
#         d=abs(math.floor((price2-price1)/price2 *10000)/100)
#         mid=round(((c+d)/2),2)
        
       
    
#         if price1>=price2:    
#             minus  = mid
#             if 1<minus: 여기 1적혀있는곳에 원하는 기준 적고여 ex)3<minus
#                 msg= "(XRP)\n빗썸  {}$. \n쿠코인{}$. \n + {}%.".format(format(price1,','),(format(price2,',')),minus)
#                 bot.sendMessage(chat_id=chat_id, text=msg)
#                 break
#                  msg= "(XRP)\n빗썸  {}$. \n쿠코인{}$. \n + {}%." 여기서도 xrp대신 원하는 티커명 적으세요. 밑에 코드도 마찬가지.
                
            
#         else:
#             minus  = mid
#             if 1<minus:여기 1적혀있는곳에 원하는 기준 적고여 ex)3<minus
#                 msg= "(XRP)\n빗썸  {}. \n쿠코인 {}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
#                 bot.sendMessage(chat_id=chat_id, text=msg)
              
#                 break

        
        


# In[28]:


#빗섬 쿠코인
def bit_cu():
    bot = telegram.Bot(token='aa') #본인 코튼입력
    chat_id = aaa #본인id 입력

    while True: 
        #빗섬
        tickers = pybithumb.get_tickers() 
        Bithumb = pybithumb.get_current_price("BTC")
        #빗섬
    
        #쿠코인
        d = CurrencyConverter()
        base_url ='https://api.kucoin.com'
        path='/api/v1/market/orderbook/level1'
        r= requests.get(base_url+path,params={'symbol':'BTC-USDT'}) 
        a=r.json()['data']['price']
        KUCOIN = round(d.convert(a,'USD','KRW')) #환율위해
        #쿠코인
    
        price1 = Bithumb
        price2 = KUCOIN 
    
        c=abs(math.floor((price1-price2)/price1 *10000)/100)
        d=abs(math.floor((price2-price1)/price2 *10000)/100)
        mid=round(((c+d)/2),2)
        
       
    
        if price1>=price2:    
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n빗썸  {}$. \n쿠코인{}$. \n + {}%.".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                
                break
                
            
        else:
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n빗썸  {}. \n쿠코인 {}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
              
                break
                


# In[29]:


#업비트 쿠코인

def upbit_cu():
    bot = telegram.Bot(token='aa') #본인 코튼입력
    chat_id = aaa #본인id 입력
    while True:
        #업비트
        Upbit=round(pyupbit.get_current_price("USDT-BTC")) ## BTC자리에 다른 코인이름
        Upbit_Exchange = CurrencyConverter()
        UPBTI=round(Upbit_Exchange.convert(Upbit,'USD','KRW'))
        # 업비트
        
        #쿠코인
        d = CurrencyConverter()
        base_url ='https://api.kucoin.com'
        path='/api/v1/market/orderbook/level1'
        r= requests.get(base_url+path,params={'symbol':'BTC-USDT'}) 
        a=r.json()['data']['price']
        KUCOIN = round(d.convert(a,'USD','KRW')) #환율위해
        #쿠코인
        
        price1 = UPBTI
        price2 = KUCOIN
        c=abs(math.floor((price1-price2)/price1 *10000)/100)
        d=abs(math.floor((price2-price1)/price2 *10000)/100)
        mid=round(((c+d)/2),2)
        
        if price1>=price2:    
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n업비트  {}$. \n쿠코인{}$. \n + {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                
                break
                
            
        else:
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n업비트  {}. \n쿠코인 {}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                break
    





# In[30]:


#빗섬 업비트


def bit_up():
    bot = telegram.Bot(token='aa') #본인 코튼입력
    chat_id = aaa #본인id 입력


    while True:
    
        #업비트
        Upbit=pyupbit.get_current_price("USDT-BTC") ## BTC자리에 다른 코인이름
        Upbit_Exchange = CurrencyConverter()
        UPBTI=round(Upbit_Exchange.convert(Upbit,'USD','KRW'))
        # 업비트
    
        #빗섬
        tickers = pybithumb.get_tickers() 
        Bithumb = pybithumb.get_current_price("BTC")
        #빗섬
        
        price1 = UPBTI
        price2 = Bithumb 
    
        c=abs(math.floor((price1-price2)/price1 *10000)/100)
        d=abs(math.floor((price2-price1)/price2 *10000)/100)
        mid=round(((c+d)/2),2)
       

        if price1>=price2:    
            minus  = mid
            if 1<minus:
                msg= "(BTC)\  {}$. \n빗섬{}$. \n + {}%.".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                
                break
                
            
        else:
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n빗썸  {}. \n빗섬{}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
               
                break
                


# In[31]:


#바이낸스 업비트


def bi_up():
    bot = telegram.Bot(token='aa') #본인 코튼입력
    chat_id = aaa #본인id 입력
    while True:
        #바이낸스
        binance = ccxt.binance() #바이낸스 객체 생성
        ticker = binance.fetch_ticker('BTC/USDT')
        binance_Exchange = CurrencyConverter() #환율을 위해
        BINANCE=round(binance_Exchange.convert(ticker['last'],'USD','KRW'))
        #바이낸스
    
        #업비트
        Upbit=round(pyupbit.get_current_price("USDT-BTC")) ## BTC자리에 다른 코인이름
        Upbit_Exchange = CurrencyConverter()
        UPBTI=round(Upbit_Exchange.convert(Upbit,'USD','KRW'))
        # 업비트
    
        price1 = BINANCE
        price2 = UPBTI
    
        c=abs(math.floor((price1-price2)/price1 *10000)/100)
        d=abs(math.floor((price2-price1)/price2 *10000)/100)
        mid=round(((c+d)/2),2)
       
        if price1>=price2:    
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n바이낸스  {}$. \n업비트{}$. \n + {}%.".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                
                break
                
            
        else:
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n바이낸스  {}. \n업비트 {}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                
                break
                


# In[32]:


#바이낸스 쿠코인

def bi_cu():
    bot = telegram.Bot(token='aa') #본인 코튼입력
    chat_id = aaa #본인id 입력
    

    while True:
        #바이낸스
        binance = ccxt.binance() #바이낸스 객체 생성
        ticker = binance.fetch_ticker('BTC/USDT')
        binance_Exchange = CurrencyConverter() #환율을 위해
        BINANCE=round(binance_Exchange.convert(ticker['last'],'USD','KRW'))
        #바이낸스
     
        #쿠코인
        d = CurrencyConverter()
        base_url ='https://api.kucoin.com'
        path='/api/v1/market/orderbook/level1'
        r= requests.get(base_url+path,params={'symbol':'BTC-USDT'}) 
        a=r.json()['data']['price']
        KUCOIN = round(d.convert(a,'USD','KRW')) #환율위해
        #쿠코인
    
        price1 = BINANCE
        price2 = KUCOIN 
    
        c=abs(math.floor((price1-price2)/price1 *10000)/100)
        d=abs(math.floor((price2-price1)/price2 *10000)/100)
        mid=round(((c+d)/2),2)
       
        if price1>=price2:    
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n바이낸스  {}$. \n쿠코인{}$. \n + {}%.".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                break
                
            
        else:
            minus  = mid
            if 1<minus:
                msg= "(BTC)\n바이낸스  {}. \n쿠코인 {}. \n- {}%".format(format(price1,','),(format(price2,',')),minus)
                bot.sendMessage(chat_id=chat_id, text=msg)
                break
                 
                


# In[34]:


while True:
    bit_cu()#빗섬 쿠코인
    bit_up()#빗섬 업비트
    upbit_cu()#업비트 쿠코인
    bi_up()#바이낸스 업비트
    bi_cu()#바이낸스 쿠코인
    time.sleep(5)


# In[1]:


#바이낸스
# binance = ccxt.binance() #바이낸스 객체 생성
# ticker = binance.fetch_ticker('BASIC/USDT')
# binance_Exchange = CurrencyConverter() #환율을 위해
# BINANCE=round(binance_Exchange.convert(ticker['last'],'USD','KRW'))
# # #바이낸스
# # print(BINANCE)
     
#쿠코인
# d = CurrencyConverter()
# base_url ='https://api.kucoin.com'
# path='/api/v1/market/orderbook/level1'
# r= requests.get(base_url+path,params={'symbol':'BASIC-USDT'}) 
# a=r.json()['data']['price']
# KUCOIN = round(d.convert(a,'USD','KRW')) #환율위해
# #쿠코인
# print(KUCOIN)

#업비트
# Upbit=round(pyupbit.get_current_price("USDT-BASIC")) ## BTC자리에 다른 코인이름
# Upbit_Exchange = CurrencyConverter()
# UPBTI=round(Upbit_Exchange.convert(Upbit,'USD','KRW'))
# # 업비트
# print(UPBTI)

#빗섬
# tickers = pybithumb.get_tickers() 
# Bithumb = pybithumb.get_current_price("XPR")
# #빗섬
# print(Bithumb)

