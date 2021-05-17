# justpy 用javascript编写，能够直接完成网页app的构建
# 此处调用了Quasar框架设计网页 https://quasar.dev/introduction-to-quasar
# 插入的第三部分，用到highchart，这是一个javascript库，javascript此处用的是Json，而Json在python中通用。
# https://www.highcharts.com/docs/chart-and-series-types/spline-chart 找到事例图的Javascript源代码在CodePen中，然后复制containe后面的源代码。
# 新建 chart_def 然后将复制的代码补充在'='后面。复制的这部分更像是library。

import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} km: {point.y}°C'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""

def app():
    wp = jp.QuasarPage()                                      # 'wp' is just a variable name and 'wp'stands for web page
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.title.text = "Average Rating by Day"           #可以对应用源代码的指定位置进行内容更改。
    hc.options.xAxis.categories = list(day_average.index)     # 这里给源代码中的 xAxis 创建了一个key值，并赋值
    hc.options.series[0].data = list(day_average['Rating'])   # series中整体作为一个library，其index=0， 因此series[0] 可以选取整个library.其后面加一个data，可以指代library中的data项目。然后将数据x，y坐标分别用其他值代替。完美套用Javascript.

    return wp

jp.justpy(app)