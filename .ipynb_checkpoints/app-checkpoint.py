# Equity Information App - Jordan Grose
# path to streamlit app.py
# C:\Users\jorda\Documents\GitHub\equity_information


import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
from sklearn.metrics import mean_squared_error


# title and intro
st.write("""
# Equity Information App
Welcome to my first app using Streamlit.io! The purpose of this application is to provide company and stock information for a given input company ticker. The app is designed to show information for US-based public companies. To get started, type a company ticker in the text box below and hit enter.
""")


# ticker input
text = st.text_input(label='Enter a stock ticker here (use all caps!): ', value='MSFT')


# data
tic = yf.Ticker(text)
hist = tic.history(period='max')
close = hist[['Close']]
volume = hist[['Volume']]
recs = tic.recommendations[-5:]
recs = recs[['Firm', 'To Grade']]
recs = recs.rename(columns={'To Grade': 'Grade'})
name = tic.info['shortName']
summary = tic.info['longBusinessSummary']
industry = tic.info['industry']
cityhq = tic.info['city']
statehq = tic.info['state']
currentPrice = str(tic.info['currentPrice'])



if tic.info['earningsGrowth'] != None:
    y_earningsGrowth = str(round(tic.info['earningsGrowth']*100,3)) + '%'
else:
    y_earningsGrowth = 'Sorry, no data on this'


if tic.info['returnOnEquity'] != None:
    y_returnOnEquity = str(round(tic.info['returnOnEquity']*100,3)) + '%'
else:
    y_returnOnEquity = "Sorry, no data on this"

    
if tic.info['currentRatio'] != None:
    currentRatio = str(tic.info['currentRatio'])
else:
    currentRatio = 'Sorry, no data on this'

    
if tic.info['returnOnAssets'] != None:
    y_returnOnAssets = str(round(tic.info['returnOnAssets']*100,3)) + '%'
else:
    y_returnOnAssets = 'Sorry, no data on this'


if tic.info['revenueGrowth'] != None:
    y_revenueGrowth = str(round(tic.info['revenueGrowth']*100,3)) + '%'
else:
    y_revenueGrowth = 'Sorry, no data on this'


if tic.info['profitMargins'] != None:
    y_profitMargins = str(round(tic.info['profitMargins']*100,3)) + '%'
else:
    y_profitMargins = 'Sorry, no data on this'


if tic.info['averageVolume10days'] != None:
    avg_10_volume = str(tic.info['averageVolume10days'])
else:
    avg_10_volume = 'Sorry, no data on this'


if tic.info['debtToEquity'] != None:
    debtToEquity = str(round(tic.info['debtToEquity'],3))
else:
    debtToEquity = 'Sorry, no data on this'



at_high = str(hist.High.max().round(3))
at_high_d = hist.index[hist['High'] == hist.High.max()].tolist()
at_high_d = at_high_d[0]
at_high_d = at_high_d.strftime('%A %B %d, %Y')

at_low = str(hist.Low.min().round(3))
at_low_d = hist.index[hist['Low'] == hist.Low.min()].tolist()
at_low_d = at_low_d[0]
at_low_d = at_low_d.strftime('%A %B %d, %Y')



# moving average model
hist_yr = tic.history(period='1y')
hist_yr = hist_yr[['Close']]
lookback = []
error = []
for index in range(2,30):
    lookback.append(index)
    error.append(mean_squared_error(hist_yr.Close[30:], 
                                    hist_yr["Close"].rolling(index).mean()[28:251]))
tab = np.array((lookback, error)).T
df = pd.DataFrame(tab, columns = ['lookback', 'error'])
lb = df.loc[df.error == df.error.min(), 'lookback'].values[0].astype('int')
pred = hist_yr[-lb:]['Close'].values.mean().round(3)



# body
st.write('**Company name:   **', name)
st.write('**Headquarters:   **', cityhq+','+' '+statehq)
st.write('**Industry:   **', industry)
summary
st.text("")


st.markdown('### **Latest Company Financial Information**')
st.write('**Current Ratio:   **', currentRatio)
st.write('**Annual Return on Assets:   **', y_returnOnAssets)
st.write('**Annual Revenue Growth:   **', y_revenueGrowth)
st.write('**Annual Profit Margin:   **', y_profitMargins)
st.write('**Debt to Equity Ratio:   **', debtToEquity)
st.text("")


st.markdown('### **Company Stock Information**')
st.write('**Current Stock Price:   **', currentPrice)
st.write('**10 Day Average Volume:   **', avg_10_volume)
st.write('**YoY Change in Earnings:   **', y_earningsGrowth)
st.write('**YoY Return on Equity:   **', y_returnOnEquity)
st.text("")


st.markdown('### **All-Time Closing Stock Prices**')
st.write('This is an interactive graph showing the all-time close prices for the chosen stock. Zoom in/out, move the chart and hover over a specific date for more detailed information.')
st.line_chart(data=close)
st.write('**All-Time High:   **', at_high_d, " -- ", at_high)
st.write('**All-Time Low:   **', at_low_d, " -- ", at_low)
st.text("")


st.markdown('### **All-Time Stock Trade Volume**')
st.write('This is an interactive graph showing the all-time trade volume for the chosen stock.')
st.bar_chart(data=volume)
st.text("")


st.markdown('### **Latest Analyst Recommendations**')
st.dataframe(recs)
st.text("")

st.markdown('### **Predicted Close Price**')
st.write("Predicting stock prices is a very difficult task due to the many outside factors that can affect a company's performance and outlook. This prediction uses the prior year's closing prices to determine an optimal moving average lookback period that minimizes error (MSE). The optimal lookback period is then used to predict the stock's closing price for the next trading day, based on a moving average.")
st.write('**Lookback period used for moving average prediction:   **')
lb
st.write('**Predicted closing price for next trading day:  **')
pred
st.text("")
