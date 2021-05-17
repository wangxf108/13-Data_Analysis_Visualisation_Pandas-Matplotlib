关于6-av-rat-day的制作过程。

步骤一：通过justpy创建基础框架， 为网络app的搭建做准备。

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
...
...
....
    return wp

jp.justpy(app)



步骤二：在highchart网站：https://www.highcharts.com/docs/chart-and-series-types/spline-chart 
  找到事例图的Javascript源代码在CodePen中，然后复制containe后面的源代码。
  注意前后要用6个“ 包围。

  另外，tpye：'spline',inverte: true>>>false ,方式坐标轴互换。

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Average Rating by Day'
  },
 ...
 ...(中间忽略)
 ...
  series: [{
    name: 'Rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""



步骤三：将jupyter中已经整理好的数据导入。当然是通过pandas等整理完成。
  将这组代码放在程序最上方。

import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()



步骤四：对源代码中的x, y 轴进行赋值。

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])



其他：如果运行程序以后，没有摁'contrl+C' 而退出的话，会发生error 端口被占用的现象，输入

kill -9 $(ps -A | grep python | awk '{print $1}')

来去除被占用的端口。







