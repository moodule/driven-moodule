# -*- coding: utf-8 -*-
import math

import dash_core_components as dcc
import plotly.graph_objs as go

from driven.data.testing import _random_navigation_data

#####################################################################
# GRAPH
#####################################################################
def navigation_graph(id='navigation-graph', data=[]):
    return dcc.Graph(
        id=id,
        figure=go.Figure(
            data=_random_navigation_data(),
            layout=go.Layout(
                title='Navigation',
                barmode='stack',
                showlegend=False,
                margin=go.layout.Margin(l=40, r=40, t=40, b=40))))

