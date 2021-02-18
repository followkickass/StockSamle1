import tushare as ts
import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
import mplfinance as mpf

# StockCode = '600104.SH'
# period = '1 Year'
# set tushare user token
ts.set_token('cf7adafe0ad77a7ec4e868d6bf70d545c1d13b21428bd7326fa34b28')

#initial interface
pro = ts.pro_api()

#fetch date 
df = pro.daily(ts_code= StockCode, start_date='20200101', end_date='2020231')

#sort data
#remove redundant column 
df.drop(['ts_code', 'pre_close', 'change', 'pct_chg', 'amount'], axis = 1, inplace = True)
#modify the column name
df.columns=['Date','Open', 'High', 'Low', 'Close','Volume']
#convert date format
df['Date'] = pd.to_datetime(df['Date'])
#set index by Date
df.set_index(['Date'], inplace=True)
# print(df)

mpf.plot(df, type='candle', mav =(5,10,20), volume = True)
# kwargs = dict(
# 	type='candle', 
# 	mav=(7, 30, 60), 
# 	volume=True, 
# 	title='\nA_stock %s candle_line' % (StockCode),    
# 	ylabel='OHLC Candles', 
# 	ylabel_lower='Shares\nTraded Volume', 
# 	figratio=(15, 10), 
# 	figscale=5)

# mc = mpf.make_marketcolors(
# 	up='red', 
# 	down='green', 
# 	edge='i', 
# 	wick='i', 
# 	volume='in', 
# 	inherit=True)

# s = mpf.make_mpf_style(
# 	gridaxis='both', 
# 	gridstyle='-.', 
# 	y_on_right=False, 
# 	marketcolors=mc)

# mpl.rcParams['axes.prop_cycle'] = cycle(
#     color=['dodgerblue', 'deeppink', 
#     'navy', 'teal', 'maroon', 'darkorange', 
#     'indigo'])

# mpl.rcParams['lines.linewidth'] = .5



# mpf.plot(df, 
# 	**kwargs, 
# 	style=s, 
# 	show_nontrading=False,
# 	savefig='A_stock-%s %s_candle_line'
# 	 % (StockCode, period) + '.jpg')
# plt.show()