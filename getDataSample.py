import tushare as ts
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplfinance as mpf


ts.set_token('cf7adafe0ad77a7ec4e868d6bf70d545c1d13b21428bd7326fa34b28')

pro = ts.pro_api()


kwargs = dict(
	type='candle', 
	mav=(7, 30, 60), 
	volume=True, 
	title='\nA_stock %s candle_line' % (symbol),    
	ylabel='OHLC Candles', 
	ylabel_lower='Shares\nTraded Volume', 
	figratio=(15, 10), 
	figscale=5)

mc = mpf.make_marketcolors(
	up='red', 
	down='green', 
	edge='i', 
	wick='i', 
	volume='in', 
	inherit=True)

s = mpf.make_mpf_style(
	gridaxis='both', 
	gridstyle='-.', 
	y_on_right=False, 
	marketcolors=mc)

mpl.rcParams['axes.prop_cycle'] = cycler(
    color=['dodgerblue', 'deeppink', 
    'navy', 'teal', 'maroon', 'darkorange', 
    'indigo'])

mpl.rcParams['lines.linewidth'] = .5

ds = pro.daily(ts_code='600104.SH', start_date='20200101', end_date='2020231')


mpf.plot(df, 
	**kwargs, 
	style=s, 
	show_nontrading=False,
	savefig='A_stock-%s %s_candle_line'
	 % (symbol, period) + '.jpg')
plt.show()