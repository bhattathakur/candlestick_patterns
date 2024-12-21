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
type=df_info['type'].unique()
pattern=df_info['pattern_name'].unique()

pattern_name=[x.removeprefix("CDL") for x in pattern]   

#choose the candlestick pattern
selected_pattern=st.sidebar.selectbox("Select Candlestick Pattern",pattern_name,index=None,key='pattern')


#also give the option for sma condition, rsi,volume
#sma5abovesma10=st.sidebar.checkbox("SMA5 > SMA10",value=False,key='sma5abovesma10')
#sma5belowsma10=st.sidebar.checkbox("SMA5 < SMA10",value=False,key='sma5belowma10')
close_above_sma=st.sidebar.checkbox("(CLOSE > SMA50) & (CLOSE > SMA200)",value=False,key='closeaobovesma200')
if debug:st.write(f'close_above_sma:',close_above_sma)
close_below_sma=st.sidebar.checkbox("(CLOSE < SMA200) & (CLOSE < SMA200)",value=False,key='closebelowsma200')
rsi=st.sidebar.slider("RSI",0,100,50,1,key='rsi')

if not selected_pattern:
    st.warning("Please select a candlestick pattern",icon="⚠️")
    st.stop()

#selected columns
selected_columns=['ticker','date','open','high','low','close','volume','VOL20','SMA5','SMA10','SMA21','SMA50','SMA200','RSI','ATR',f'CDL{selected_pattern}']
#selected pattern name
temp_df=df[selected_columns]

#upper case the column names
temp_df.columns=temp_df.columns.str.upper()

#the desired dataframe with the condition !=0
plot_df=temp_df[temp_df[f'CDL{selected_pattern}']!=0]

if debug:st.write(f'Selected Pattern:',selected_pattern)
if debug:st.write(f'temp_df:',temp_df.head(5))
if debug:st.write(f'plot_df:',plot_df.head(5))

#if dataframe is empty give warning and stop
if plot_df.empty:
    st.warning(f"No tickers in {selected_market} for pattern: {selected_pattern}",icon="⚠️")
    st.stop()
#st.write(f"Types of Candlestick Patterns: {type}")
#st.write(f"Types of Candlestick Patterns: {pattern}")
#radio or similar with the desired pattern
result_ticker_list=plot_df['TICKER'].unique()
st.sidebar.markdown(f"<h3 style='text-align:center;color:magenta'> RESULTANT TICKERS ARE BELOW</h3>",unsafe_allow_html=True)
st.sidebar.markdown(f"<h3 style='text-align:center;color:red'>TICKERS WITH {selected_pattern} PATTERN</h3>",unsafe_allow_html=True)
selected_ticker=st.sidebar.radio(f"SELECT A TICKER FOR CHART",result_ticker_list,index=0,key='ticker')
if debug:
    st.write(f"Selected Market: {selected_market}")
    #st.write(df.head(10))
    st.write(df_info.head(1))

#two containers


#container1: pattern_name, pattern_type, pattern_description
pattern_info=df_info[df_info['pattern_name']==f'CDL{selected_pattern}']
pattern_name=pattern_info['pattern_name'].values[0].removeprefix("CDL")
pattern_type=pattern_info['type'].values[0]
pattern_description=pattern_info['description'].values[0]
#if debug:st.write(f'pattern_info:',pattern_info)
if debug:st.write(f'pattern_name:',pattern_name)
if debug:st.write(f'pattern_type:',pattern_type)
if debug:st.write(f'pattern_description:',pattern_description)