# equity_information
Jordan Grose

Personal project that harnesses Yahoo Finance python data package and Streamlit.io to display stock information for a given input ticker.

yfinance: https://aroussi.com/post/python-yahoo-finance 

streamlit: https://streamlit.io/

Use the deployed app with this link:
https://share.streamlit.io/jpgrose/equity_information/main/app.py 

------------------------------

For my BA890 practicum, I chose to build a small web-application that harnesses open source python packages to display information about stocks in a clean, responsive web page. My goal is to display as much relevant information about the company's current stock price and financial standing, as well as show graphs of price and volume for the equity's lifetime on the public market to give the user a better sense of the stock's performance today relative to other periods of time. Lastly, the site uses a moving average model to predict the closing price for the next trading day.


The goal behind this project was to learn the capabilites and syntax of two python packages (yfinance and streamlit). yfinance is the latest open source python package dedicated to sourcing live equity data from Yahoo Finance. It allows users to easily grab company, financial, and historical information about a given ticker in commonly used python data structures (dictionaries and dataframes). This is convenient because it allows users to bring data into variables and create visualizations or make calculations.


Streamlit is a broader python package that allows users to build responsive and clean web apps, without diving into the HTML/CSS/Javascript that you would normally need, right from a python script.


The entire project is located in this GitHub Repository. The code for the app can be found in the app.py file, and the test code for model training and visualizations is in the test_code.ipynb python notebook. The project is deployed via GitHub and Streamlit Sharing, click the link above to visit and start using the app. Enjoy!
