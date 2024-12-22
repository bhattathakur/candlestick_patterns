from plotly.subplots import make_subplots
import plotly.graph_objects as go

def get_respective_pattern(temp_df,pattern_name):
  '''
  get related candlestick pattern of a given ticker
  '''
  ticker=temp_df['ticker'].values[0]
  print(f'ticker: {ticker}')

  #two plot columns one for a patte
  subplot_titles=[f'TICKER: {ticker}',f'PATTERN: {pattern_name.removeprefix("CDL")}']#subplot names

  fig=make_subplots(rows=1,cols=2, horizontal_spacing=0.3 )

  
  #main chart
  
  main_chart= go.Candlestick(x=temp_df['date'],
                  
                  open=temp_df['open'],
                  
                  high=temp_df['high'],
                  
                  low=temp_df['low'],
                  
                  close=temp_df['close'],name='')#])

  
  #pattern chart
  sma50_scatter=go.Scatter(x=temp_df['date'],y=temp_df['sma50'],mode='lines',name='SMA50',line=dict(color='blue',width=1))
  sma200_scatter=go.Scatter(x=temp_df['date'],y=temp_df['sma200'],mode='lines',name='SMA200',line=dict(color='red',width=1))
  
  temp_df=temp_df.tail(5)
  
  pattern_chart= go.Candlestick(x=temp_df['date'],
                  
                  open=temp_df['open'],
                  
                  high=temp_df['high'],
                  low=temp_df['low'],
                  close=temp_df['close'],name='')#])

  fig.add_trace(sma50_scatter,row=1,col=1)
  fig.add_trace(sma200_scatter,row=1,col=1)
  fig.add_trace(main_chart,row=1,col=1)
  fig.add_trace(pattern_chart,row=1,col=2)
  fig.update_layout(xaxis_rangeslider_visible=False,
                    xaxis2_rangeslider_visible=False,
                    xaxis=dict(domain=[0,0.75]),
                    xaxis2=dict(domain=[0.80,1]),
                    showlegend=False,
                    yaxis_title='Price [$]',
                    width=1400,
                    height=600,
                    )
  rangebreaks=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(values=["2024-12-25", "2025-01-01"])  # hide Christmas and New Year's
    ]
  fig.update_xaxes(rangebreaks=rangebreaks,row=1,col=1)
  fig.update_xaxes(rangebreaks=rangebreaks,row=1,col=2)

  # Update layout to center each subplot title
  fig.update_layout(
    annotations=[
        dict(
            text=subplot_titles[0],
            x=0.35,  # Adjust x position for centering
            y=1.1,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=20)
        ),
        dict(
            text=subplot_titles[1],
            x=0.97,  # Adjust x position for centering
            y=1.1,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=20)
        )
    ]
    )
#fig update
  fig.update_layout(showlegend=True)

  return fig