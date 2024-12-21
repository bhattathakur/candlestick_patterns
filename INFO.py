import streamlit as st

st.set_page_config(page_title="INFO PAGE", page_icon="📈", layout="wide")

st.markdown(f"<h1 style='text-align:center;color:red'> INFO PAGE </h1>",unsafe_allow_html=True)

#disclaimer
disclaimer_text="""
Disclaimer:
The information provided by this stock screener is for informational purposes only and should not be considered as financial advice, investment advice, or trading suggestions. All data and analysis are provided "as is" and without any guarantees of accuracy or completeness. Users are solely responsible for their investment decisions. Always conduct your own research and consult with a licensed financial advisor before making any investment decisions.
"""
st.warning(disclaimer_text,icon="⚠️")


# About

st.markdown(f""" 
<div style="text-align:left;">
            1. This is a simple stock screener that identifies candlestick patterns in stock data for the last trading day. <br>
            2. It allows to filter the market based on SNP500, DOW30, NASDAQ100, IPOS>=2020 <br>
            3. It also allows the user to filter stocks based on Closing Price, Simple Moving Average (SMA), and Relative Strength Index (RSI).<br>
            4. Candlestick pattern might hint the possible pullbacks and is very useful for traders who use technical analysis to make trading decisions. <br>
            </div>
            """,unsafe_allow_html=True)
