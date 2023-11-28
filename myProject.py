import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib_inline as plt

st.set_page_config(layout="wide")


def sp500(spy):
    st.write("   ")
    expander = st.expander(f"S&P 500 Price Chart")
    spTicker = yf.Ticker(spy)
    tab1, tab2 = expander.tabs(["1 Year", "5 Years"])
    with tab1:
        price_close2 = spTicker.history(period="1y")['Close']
        tab1.subheader("1 Year")
        tab1.line_chart(price_close2, width=250)  # NEW METHOD
    with tab2:

        price_close3 = spTicker.history(period="5y")['Close']
        tab2.subheader("5 Years")
        tab2.line_chart(price_close3)


def dow(dowj):
    st.write("   ")
    st.write("   ")
    expander = st.expander(f"Dow Jones Price Chart")
    dTicker = yf.Ticker(dowj)
    tab1, tab2 = expander.tabs(["1 Year", "5 Years"])  # NEW METHOD
    with tab1:
        price_close2 = dTicker.history(period="1y")['Close']
        tab1.subheader("1 Year")
        tab1.line_chart(price_close2, width=250)  # NEW METHOD
    with tab2:

        price_close3 = dTicker.history(period="5y")['Close']
        tab2.subheader("5 Years")
        tab2.line_chart(price_close3)


# NEW METHOD
name = st.text_input(label="Enter a ticker", key=str,
                     max_chars=8, placeholder="Ticker")

tickerNames = []
tickerNames.append(name)
st.title(f"{name} Stock Information")  # NEW METHOD
st.write("---")


def price_chart(name):
    tickerN = yf.Ticker(name)

    st.header(f"{name} Price Chart")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["30 Days", "100 Days", "1 Year", "5 Years"])
    with tab1:
        price_close = tickerN.history(period="30d")['Close']
        st.line_chart(price_close)
    with tab2:
        price_close = tickerN.history(period="100d")['Close']
        st.line_chart(price_close)
    with tab3:
        price_close = tickerN.history(period="1y")['Close']
        st.line_chart(price_close)
    with tab4:
        price_close = tickerN.history(period="5y")['Close']
        st.line_chart(price_close)


def price_table(name):
    tickerN = yf.ticker(name)
    st.header


col1, col2 = st.columns(2, gap="medium")  # NEW METHOD
with col1:
    sp500("SPY")
    dow("DJIA")
with col2:
    price_chart(name)
