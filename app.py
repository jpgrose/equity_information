# path for streamlit .py script
# C:\Users\jorda\Documents\GitHub\equity_information

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st

st.write("""
# Hello world
this is example
""")


text = st.text_input(label='enter ticker here (use all caps!): ', value='')

tic = yf.Ticker(text)
hist = tic.history(period='1y')
# hist.reset_index(inplace = True)

st.write("""
Company Description:
""")

tic.info['longBusinessSummary']

# st.write("""
# **Closing prices for the last year graphed:**
# """)

st.dataframe(hist)

# x = hist.Date
# y = hist.Close
# fig = plt.plot(x, y)

# def graph_close(data):
#     fig, ax = plt.subplots()
#     ax = sns.lineplot(data=data, x='Date', y='Close')
#     return fig


sns.lineplot(data=hist, x='Date', y='Close')    
st.pyplot()

close = hist[['Close']]
st.line_chart(data=close)




