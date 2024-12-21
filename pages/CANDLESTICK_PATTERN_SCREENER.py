import streamlit as st
import pandas as pd

from  pythonfiles.plotlyplot import get_respective_pattern # plotly chart function


st.set_page_config(page_title="Candlestick Pattern Screener", page_icon="📈", layout="wide")

#get_respective_pattern(temp_df,pattern_name)


#map the dataframes for the candlestick patterns
files_map={
'SNP500':'df_snp_pattern.csv',
'DOW30':'df_dow_pattern.csv',
'NASDAQ100':'df_nasdaq100_pattern.csv',
'IPOS>=2020':'df_nasdaqipo_pattern.csv'
}

#user input in the side bar
debug=True
#st.sidebar.markdown(f"<h1 style='text-align:center;color:red'> PLEASE CHOOSE</h1>",unsafe_allow_html=True)
selected_market=st.sidebar.selectbox("Select Market",['SNP500','DOW30','NASDAQ100','IPOS>=2020'],index=0,key='market')


#dataframe for the selected market
df=pd.read_csv(files_map[selected_market])

#candlestick pattern information file
df_info=pd.read_csv('info_dict.csv')

#nature of the candlestick pattern

if debug:
    st.write(f"Selected Market: {selected_market}")
    st.write(df.head(10))
    st.write(df_info.head(10))