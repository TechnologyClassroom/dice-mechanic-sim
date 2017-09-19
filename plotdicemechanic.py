# plotdicemechanic.py
# 
# visualize csv data with plotly for Midnight Riders

# Michael McMahon

# https://plot.ly/python/getting-started/#initialization-for-offline-plotting
# https://plot.ly/python/plot-data-from-csv/#plotting-data-from-external-source

# Install dependencies
#  pip install plotly --upgrade
#  pip install pandas --upgrade

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd

input='test.csv'
df = pd.read_csv(input)

# Export table in html
#df_external_source = FF.create_table(df.head())
#py.plot(df_external_source, filename='midnight-riders-table-'+input+'.html')

# Plot each score as a line graph
trace0 = go.Scatter(x = list(range(0,7)), y = df["'R1'"], name='R1')
trace1 = go.Scatter(x = list(range(0,7)), y = df["'M1'"], name='M1')
trace2 = go.Scatter(x = list(range(0,7)), y = df["'R2'"], name='R2')
trace3 = go.Scatter(x = list(range(0,7)), y = df["'M2'"], name='M2')
trace4 = go.Scatter(x = list(range(0,7)), y = df["'R3'"], name='R3')
trace5 = go.Scatter(x = list(range(0,7)), y = df["'M3'"], name='M3')
trace6 = go.Scatter(x = list(range(0,7)), y = df["'R4'"], name='R4')
trace7 = go.Scatter(x = list(range(0,7)), y = df["'M4'"], name='M4')
layout = go.Layout(title=input, 
  plot_bgcolor='rgb(230, 230,230)', showlegend=True)
fig = go.Figure(data=[trace0, trace1, trace2, trace3, trace4, trace5, trace6, 
  trace7], layout=layout)

# Display line graph
py.plot(fig, filename='midnight-riders-'+input+'.html')

