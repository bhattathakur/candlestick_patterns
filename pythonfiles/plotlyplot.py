from plotly.subplots import make_subplots
import plotly.graph_objects as go

def get_respective_pattern(temp_df,pattern_name):
  '''
  get related candlestick pattern of a given ticker
  '''
  ticker=temp_df['ticker'].values[0]
  print(f'ticker: {ticker}')

  #two plot columns one for a pattern  and second for 20 day plot
  fig=make_subplots(rows=1,cols=2,subplot_titles=[f'TICKER: {ticker}',f'PATTERN: {pattern_name.removeprefix("CDL")}'])

  #main chart
  main_chart= go.Candlestick(x=temp_df['date'],
                  open=temp_df['open'],
                  high=temp_df['high'],
                  low=temp_df['low'],
                  close=temp_df['close'])#])

  #pattern chart
  temp_df=temp_df.tail(5)
  pattern_chart= go.Candlestick(x=temp_df['date'],
                  open=temp_df['open'],
                  high=temp_df['high'],
                  low=temp_df['low'],
                  close=temp_df['close'],name='1 YEAR CHART')#])

  fig.add_trace(main_chart,row=1,col=1)
  fig.add_trace(pattern_chart,row=1,col=2)
  fig.update_layout(xaxis_rangeslider_visible=False,
                    xaxis2_rangeslider_visible=False,
                    xaxis=dict(domain=[0,0.75]),
                    xaxis2=dict(domain=[0.77,1]),
                    showlegend=False,
                    yaxis_title='Price [$]',
                    width=1400,
                    height=500,
                    title_x=0.5,

                    )
  rangebreaks=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(values=["2024-12-25", "2025-01-01"])  # hide Christmas and New Year's
    ]
  fig.update_xaxes(rangebreaks=rangebreaks,row=1,col=1)
  fig.update_xaxes(rangebreaks=rangebreaks,row=1,col=2)

  return fig