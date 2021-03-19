import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date
from datetime import timedelta 


def main():
    end_date = date.today() - timedelta(days = 1) 
    #start_date = date.today() - timedelta(years = 10) 
    #name = st.text_input('Enter a Ticker Symbol')
    
    #tickerName = st.text_input('Enter the Ticker for a company')
    st.sidebar.header('User Input Features')
    tickerName = st.sidebar.text_input('Enter the Ticker for a company')
    start_date = st.sidebar.date_input('Select a starting date')
    #Define Ticker Symbol
    if not tickerName:
        tickerName='ATVI'
    if start_date >= end_date:
        start_date= end_date - timedelta(years = 3)
        
    #get ticker data for this Ticker
    ticker_data = yf.Ticker(tickerName)
    #get historical prices
    ticker_df = ticker_data.history(period="1d", start=start_date, ends=end_date)
    st.write(f"""
    # Simple Stock Price App 
    
    Shown is the stock **closing price** and ***volume*** for {ticker_data.info['longName']} since {start_date}.
    
    """)
    #Define Ticker Symbol
    #get ticker data for this Ticker
    ticker_data = yf.Ticker(tickerName)
    #get historical prices
    ticker_df = ticker_data.history(period="1d", start=start_date, ends=end_date)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.line_chart(ticker_df.Close)
    st.line_chart(ticker_df.Volume)


if __name__ == "__main__":
    main()
