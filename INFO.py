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

st.markdown("""
### Candlestick Pattern Screener Features:

1. **Pattern Identification:**  
   This screener identifies candlestick patterns in stock data from the most recent trading day.  
   
2. **Market Filtering:**  
   Allows filtering the market based on criteria such as:
   - S&P 500
   - DOW 30
   - NASDAQ 100
   - IPOs from 2020 onwards

3. **Pattern Selection:**  
   Users can select candlestick patterns from a list of **61 options** or choose based on the following candlestick types:
   - **Bullish Reversal**
   - **Bullish Continuation**
   - **Bearish Reversal**
   - **Bearish Continuation**
   - Reversal
   - Continuation
   - Reversal or Continuation
   - Indecision
   - Trend Continuation

4. **Chart Viewing:**  
   View the **yearly candlestick chart** and a **zoomed-in view** of the candlestick pattern for the most recent trading day.

5. **Stock Data Table:**  
   The screener provides an information table with key stock data:
   - **CLOSE**, **CHANGE, CHANGE%** , **VOLUME** , **SMAs** , **RSI**, **ATR**

6. **Pattern Descriptions:**  
   Each candlestick pattern is accompanied by a brief description and its characteristics.

7. **Trading Insights:**  
   Candlestick patterns may suggest potential pullbacks, making them a valuable tool for traders who rely on **technical analysis** for decision-making.
""")
