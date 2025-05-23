import twstock
stock = twstock.Stock('2059')  # 以鴻海的股票代號建立 Stock 物件


###### 利用 fetch, fetch_31, fetch_from 指令抓取不同日期的股價
stock.fetch(2020,1) # 取得 2020 年 1 月的資料
# stock.date
# '''
# [datetime.datetime(2020, 1, 2, 0, 0),
#  datetime.datetime(2020, 1, 3, 0, 0),
#  datetime.datetime(2020, 1, 6, 0, 0),
#  datetime.datetime(2020, 1, 7, 0, 0),
#  datetime.datetime(2020, 1, 8, 0, 0),
#  datetime.datetime(2020, 1, 9, 0, 0),
#  datetime.datetime(2020, 1, 10, 0, 0),
#  datetime.datetime(2020, 1, 13, 0, 0),
#  datetime.datetime(2020, 1, 14, 0, 0),
#  datetime.datetime(2020, 1, 15, 0, 0),
#  datetime.datetime(2020, 1, 16, 0, 0),
#  datetime.datetime(2020, 1, 17, 0, 0),
#  datetime.datetime(2020, 1, 20, 0, 0),
#  datetime.datetime(2020, 1, 30, 0, 0),
#  datetime.datetime(2020, 1, 31, 0, 0)]
# '''

stock.fetch_from(2022,1) # 取得 2022 年 1 月至今的資料
stock.fetch_31()    # 取得最近 31 日的資料

###### 股票近31個收盤價
stock.fetch_31()    # 取得最近 31 日的資料
print('近31個收盤價：')
print(stock.price)   #近31個收盤價
print('近6個收盤價：')
print(stock.price[-6:])   #近6日之收盤價

###### 股票即時(最近一筆)交易資訊
real = twstock.realtime.get('2059') # 鴻海股票即時交易資訊.  'best_bid_price': 下五檔. 'best_ask_price': 上五檔.
# type(real)  ## dict
if real['success']:  #如果讀取成功
    print('股票名稱、即時(最近一筆)股票資料：')
    print('股票名稱：',real['info']['name'])     
    print('開盤價：',real['realtime']['open'])
    print('最高價：',real['realtime']['high'])  
    print('最低價：',real['realtime']['low'])
    print('目前股價：',real['realtime']['latest_trade_price'])   
else:
    print('錯誤：' + real['rtmessage'])  
