import streamlit as st
import pandas as pd

from  pythonfiles.plotlyplot import get_respective_pattern # plotly chart function


st.set_page_config(page_title="Candlestick Pattern Screener", page_icon="📈", layout="wide")
# CSS to style the table
table_style = """
    <style>
        .styled-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Courier New', Courier,monospace;
            font-size: 14px;
            background-color: #f9f9f9;
        }
        .styled-table th {
            font-size: 16px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .styled-table td {
            text-align: center;
            padding: 8px;
            color: black;
        }
        .styled-table tr:nth-child(odd) {
            background-color: #f2f2f2;
        }
        .styled-table tr:hover {
            background-color: #ddd;
        }
    </style>
"""

#get_respective_pattern(temp_df,pattern_name)


#map the dataframes for the candlestick patterns
files_map={
'SNP500':'df_snp_pattern.csv',
'DOW30':'df_dow_pattern.csv',
'NASDAQ100':'df_nasdaq100_pattern.csv',
'IPOS>=2020':'df_nasdaqipo_pattern.csv'
}

#user input in the side bar
debug=False #True
#st.sidebar.markdown(f"<h1 style='text-align:center;color:red'> PLEASE CHOOSE</h1>",unsafe_allow_html=True)
selected_market=st.sidebar.selectbox("Select a Market",['SNP500','DOW30','NASDAQ100','IPOS>=2020'],index=0,key='market')


#dataframe for the selected market
df=pd.read_csv(files_map[selected_market])

#candlestick pattern information file
df_info=pd.read_csv('info_dict.csv')

#nature of the candlestick pattern
candle_type=list(df_info['type'].unique())

if debug:st.write(f'type:',candle_type)

#st.write(f'length of df_info:',len(df_info))

#allow to chose the type of candlestick pattern
selected_type=st.sidebar.selectbox("Select a Candlestick Pattern Type",['ALL']+candle_type,index=0,key='type')

if debug:st.write(f'selected_type:',selected_type)
pattern=df_info['pattern_name'].unique()

#distinguish the patterns based on the selected type
if selected_type!='ALL':
    pattern=[x for x in pattern if df_info[df_info['pattern_name']==x]['type'].values[0]==selected_type]
pattern_name=[x.removeprefix("CDL") for x in pattern]   

#choose the candlestick pattern
selected_pattern=st.sidebar.selectbox("Select a Candlestick Pattern",pattern_name,index=None,key='pattern')


#also give the option for sma condition, rsi,volume
#sma5abovesma10=st.sidebar.checkbox("SMA5 > SMA10",value=False,key='sma5abovesma10')
#sma5belowsma10=st.sidebar.checkbox("SMA5 < SMA10",value=False,key='sma5belowma10')
# close_above_sma=st.sidebar.checkbox("(CLOSE > SMA50) & (CLOSE > SMA200)",value=False,key='closeaobovesma200')
# if debug:st.write(f'close_above_sma:',close_above_sma)
# close_below_sma=st.sidebar.checkbox("(CLOSE < SMA200) & (CLOSE < SMA200)",value=False,key='closebelowsma200')
# rsi=st.sidebar.slider("RSI",0,100,50,1,key='rsi')

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
pattern_df=temp_df[temp_df[f'CDL{selected_pattern}']!=0]

if debug:st.write(f"Selected Market: {selected_market}")
if debug:st.write(f'market_df:',temp_df.head(5))
if debug:st.write(f'Selected Pattern:',selected_pattern)
if debug:st.write(f'pattern_df:',pattern_df.head(5))

#if dataframe is empty give warning and stop
if pattern_df.empty:
    st.warning(f"No tickers in {selected_market} for pattern: {selected_pattern}",icon="⚠️")
    st.stop()
#st.write(f"Types of Candlestick Patterns: {type}")
#st.write(f"Types of Candlestick Patterns: {pattern}")
#radio or similar with the desired pattern
result_ticker_list=pattern_df['TICKER'].unique()
#st.sidebar.markdown(f"<h3 style='text-align:center;color:magenta'> RESULTANT TICKERS ARE BELOW</h3>",unsafe_allow_html=True)
st.sidebar.markdown(f"<h4 style='text-align:center;color:red;background:yellow'>️TICKERS WITH <span style='color:blue;'>{selected_pattern} </span>PATTERN BELOW ️</h4>",unsafe_allow_html=True)
st.sidebar.markdown("<br>",unsafe_allow_html=True)
st.sidebar.markdown(f"<h4 style='text-align:center;color:black;background:lightblue'>SELECT A TICKER FOR A PLOT 👇</h4>",unsafe_allow_html=True)
#tickers are selected here
selected_ticker=st.sidebar.radio(f"CHOOSE ONE",result_ticker_list,index=0,key='ticker')

#if debug:st.write(f'info_df',df_info.head(1))

#two containers


#container1: pattern_name, pattern_type, pattern_description
pattern_info=df_info[df_info['pattern_name']==f'CDL{selected_pattern}'].reset_index(drop=True)
if debug:st.write(f'pattern_info:',pattern_info)
pattern_name=pattern_info['pattern_name'].values[0].removeprefix("CDL")
pattern_type=pattern_info['type'].values[0]
pattern_description=pattern_info['description'].values[0]
#if debug:st.write(f'pattern_info:',pattern_info)
if debug:st.write(f'pattern_name:',pattern_name)
if debug:st.write(f'pattern_type:',pattern_type)
if debug:st.write(f'pattern_description:',pattern_description)

#get the related year data for ticker selected for the pattern

plot_df=pd.read_csv('df_combined.csv').query(f'ticker=="{selected_ticker}"').sort_values('Date',ascending=True).reset_index(drop=True)

#get sma50 and sma200 in the plot_df
plot_df['SMA50']=plot_df['Close'].rolling(window=50).mean().round(2)
plot_df['SMA200']=plot_df['Close'].rolling(window=200).mean().round(2)



if debug:st.write(f'plot_df:',plot_df.tail(10))

#get some useful information 
ticker=plot_df['ticker'].values[-1]
last_trade_date=plot_df['Date'].values[-1]
last_trade_close=plot_df['Close'].values[-1]
second_last_close=plot_df['Close'].values[-2]
last_volume=round(plot_df['Volume'].values[-1],2)
last_rsi=round(pattern_df[pattern_df['TICKER']==selected_ticker]['RSI'].values[-1],2)
last_atr=round(pattern_df[pattern_df['TICKER']==selected_ticker]['ATR'].values[-1],2)
last_volume20=round(pattern_df[pattern_df['TICKER']==selected_ticker]['VOL20'].values[-1],2)

#get sma50 and sma200 values
sma50=round(plot_df['SMA50'].values[-1],2)
sma200=round(plot_df['SMA200'].values[-1],2)

#calculate the percentage change and net change
percentage_change=round(((last_trade_close-second_last_close)/second_last_close)*100,2)
net_change=round(last_trade_close-second_last_close,2)

st.markdown(f"<h4 style='text-align:center;color:magenta'> CANDLESTICK PATTERN INFO AND PLOT BASED ON {last_trade_date}</h4>",unsafe_allow_html=True)

if debug:st.write(f'ticker:',ticker)
if debug:st.write(f'last_trade_date:',last_trade_date)
if debug:st.write(f'last_trade_close:',last_trade_close)
if debug:st.write(f'second_last_close:',second_last_close)
if debug:st.write(f'percentage_change:',percentage_change)
if debug:st.write(f'net_change:',net_change)
if debug:st.write(f'last_volume:',last_volume)
if debug:st.write(f'last_rsi:',last_rsi)
if debug:st.write(f'last_atr:',last_atr)
if debug:st.write(f'last_volume20:',last_volume20)
if debug:st.write(f'sma50:',sma50)
if debug:st.write(f'sma200:',sma200)

#display dict creation
dislay_dict={
"Ticker":ticker,
"Last Trade Date":last_trade_date,
"Close":last_trade_close,
"Net Change":net_change,
"Change%":percentage_change,
"Last Volume (M)":f"{last_volume}",
"20DAY_AVG_VOLUME (M)":f'{last_volume20}',
"RSI":last_rsi,
"ATR":last_atr,
"SMA 50":sma50,
"SMA 200":sma200,
}

#display the dict
#df=pd.DataFrame(dislay_dict.items(),columns=['Metric','Value'])
df=pd.DataFrame([dislay_dict])
df.index+=1
#df.index.name='S.N.'
#the function is using the lower case for the column names
plot_df.columns=plot_df.columns.str.lower()


# Custom HTML to add a background color and border
container_html =f"""
<div style="background-color: #f0f8ff; border: 4px solid black; padding: 10px; border-radius: 5px;">
    <h6 style='text-align:center;color:blue'> {pattern_name}</h6>
    <h6 style='text-align:center;color:black'> {pattern_type}</h6>
   <div style="text-align:center;font-size: 18px;color:brown">
        <strong>Pattern Description:</strong><br>
        {pattern_description}
    </div>
</div>
"""#.format(pattern_name, pattern_type, pattern_description)

# Render the container with background color and border using custom HTML
st.markdown(container_html, unsafe_allow_html=True)


#plot container
with st.container():
    fig=get_respective_pattern(plot_df,f'CDL{selected_pattern}')
    st.plotly_chart(fig)

#table container
with st.container(border=False):
    #st.markdown(f"<h3 style='text-align:center;color:magenta'> {selected_ticker} </h3>",unsafe_allow_html=True)
    def style_table(val):
        try:
        # Apply color based on value
         color = "green" if val > 0 else "red"
         return f"color: {color}"
        except:
            return None

    # Style the DataFrame
    styled_df = (
    df.style.format("{:.2f}", subset=df.select_dtypes(include=["float64", "int64"]).columns)
    .apply(lambda row:row.apply(style_table), subset=["Change%", "Net Change"],axis=1)
    )

# Display the table in Streamlit
    html_table = styled_df.to_html(classes='styled-table', index=False)
    st.markdown(table_style, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)

    #st.dataframe(styled_df,use_container_width=True,hide_index=True)