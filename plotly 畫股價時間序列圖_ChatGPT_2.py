import pandas as pd
import csv, os, time, twstock

from plotly.graph_objs import Scatter, Layout
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'  # 強制在瀏覽器中顯示互動圖形

# 若你有需要匯出圖片，仍可選擇使用 kaleido（選擇性）
# import plotly.io as pio

filepath = 'twstockyear2024_7To12.csv'
stock_code = '2059'

if not os.path.isfile(filepath):
    title = ["日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"]
    with open(filepath, 'a', newline='', encoding='big5') as outputfile:
        outputwriter = csv.writer(outputfile)
        outputwriter.writerow(title)
        for i in range(7, 13):
            stock = twstock.Stock(stock_code)
            stocklist = stock.fetch(2024, i)
            data = []
            for stock_day in stocklist:
                strdate = stock_day.date.strftime("%Y-%m-%d")
                li = [strdate, stock_day.capacity, stock_day.turnover, stock_day.open, stock_day.high, stock_day.low,
                      stock_day.close, stock_day.change, stock_day.transaction]
                data.append(li)
            for dataline in data:
                outputwriter.writerow(dataline)
            time.sleep(1)

pdstock = pd.read_csv(filepath, encoding='big5')

# 建立 Plotly 曲線圖的 traces，含 hover 中文提示
trace_close = Scatter(
    x=pdstock['日期'],
    y=pdstock['收盤價'],
    name='收盤價',
    hovertemplate='日期：%{x}<br>收盤價：%{y:.2f}<extra></extra>'
)

trace_low = Scatter(
    x=pdstock['日期'],
    y=pdstock['最低價'],
    name='最低價',
    hovertemplate='日期：%{x}<br>最低價：%{y:.2f}<extra></extra>'
)

trace_high = Scatter(
    x=pdstock['日期'],
    y=pdstock['最高價'],
    name='最高價',
    hovertemplate='日期：%{x}<br>最高價：%{y:.2f}<extra></extra>'
)

data = [trace_close, trace_low, trace_high]

layout = Layout(
    title=f'2024年個股{stock_code}統計圖',
    font=dict(family='Microsoft JhengHei', size=16),
    xaxis=dict(title='日期', tickangle=-45),
    yaxis=dict(title='價格')
)

fig = go.Figure(data=data, layout=layout)

# ✅ 直接在 Spyder / Notebook 中呈現互動圖（不產生 HTML 檔）
fig.show()
