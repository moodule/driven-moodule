# -*- coding: utf-8 -*-
import math

import plotly.graph_objs as go

#####################################################################
# RANDOM DATA
#####################################################################
def _random_navigation_data():
    navigation_data = [
        go.Bar(
            y=['carry'],
            x=[6],
            name='Tail transition',
            orientation = 'h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['carry'],
            x=[2],
            name='Feed',
            orientation = 'h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['carry'],
            x=[100],
            name='Section 1',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['carry'],
            x=[10],
            name='Head transition',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['return'],
            x=[20],
            name='Belt return 1',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['return'],
            x=[75],
            name='Section 1',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['return'],
            x=[20],
            name='Belt return 2',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['return'],
            x=[5],
            name='Drive group',
            orientation='h',
            marker=dict(line=dict(width=3))),
        go.Bar(
            y=['return'],
            x=[10],
            name='Takeup',
            orientation='h',
            marker=dict(line=dict(width=3)))]

#####################################################################
# GRAPH
#####################################################################
def navigation_graph(id='navigation-graph', data=[])
    return dcc.Graph(
        id=id,
        figure=go.Figure(
            data=_random_navigation_data(),
            layout=go.Layout(
                title='Navigation',
                barmode='stack',
                showlegend=False,
                margin=go.layout.Margin(l=40, r=40, t=40, b=40))))
