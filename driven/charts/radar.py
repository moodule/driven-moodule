# -*- coding: utf-8 -*-
import math

import dash_core_components as dcc
import plotly.graph_objs as go

#####################################################################
# POLAR GRAPH
#####################################################################
def spider_graph(id='spider-graph', style={}):
    data = [
        go.Scatterpolar(
          r = [7, 5, 3, 8],
          theta = ['Safety', 'Cost','Reliability', 'Stabiliy'],
          fill = 'toself',
          name = 'User design'
        ),
        go.Scatterpolar(
          r = [10, 8, 6, 9],
          theta = ['Safety', 'Cost','Reliability', 'Stabiliy'],
          fill = 'toself',
          name = 'Optimal design'
        )
    ]

    layout = go.Layout(
      polar = dict(
        radialaxis = dict(
          visible = True,
          range = [0, 10]
        )
      ),
      showlegend = False
    )

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout),
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))