import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')

weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')

chart_def = """
{
  chart: {
    type: 'cylinder',
    options3d: {
      enabled: true,
      alpha: 15,
      beta: 15,
      depth: 50,
      viewDistance: 25
    }
  },
  xAxis: {
    categories: [],
  },
  title: {
    text: 'Highcharts Cylinder Chart'
  },
  plotOptions: {
    series: {
      depth: 25,
      colorByPoint: true
    }
  },
  series: [{
    data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
    name: 'Cylinders',
    showInLegend: false
  }]
}
"""

def app():
    wp = jp.QuasarPage()         # 'wp' is just a variable name and 'wp'stands for web page
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(weekday_average.index)
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp

jp.justpy(app)
