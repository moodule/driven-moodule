# -*- coding: utf-8 -*-
import math

import dash_core_components as dcc
import plotly.graph_objs as go

from driven.data.testing import _random_layout_data

#####################################################################
# GRAPH
#####################################################################
def conveyor_layout_graph(id='conveyor-layout-graph', data=[]):
    return dcc.Graph(
        id=id,
        figure=go.Figure(
            data=_random_layout_data(),
            layout=go.Layout(
                title='Conveyor Layout',
                showlegend=False,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=40, t=40, b=40))))
