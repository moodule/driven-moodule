# -*- coding: utf-8 -*-
import math

import dash_core_components as dcc
import plotly.graph_objs as go

#####################################################################
# RANDOM DATA
#####################################################################
def _random_layout_data():
    slope = 0.2
    steps = [0.4, 0.2, 1.5, 0.4, -1.0, -3.0, -2.5]
    count = [5, 10, 20, 5, 2, 11, 2]
    source = [
        [0.35 + 0.01 * i for i in range(100)],
        [0.5 + -5.0 * 1.0e-4 * i ** 2 for i in range(100)]]
    target = [
        [31.5 + 0.01 * i for i in range(200)],
        [3.7 - 1.25e-4 * (i ** 2) + 1.923e-3 * i for i in range(200)]]
    pulleys = [[-2.0, 31.5, 0.0, 33], [-3.5, 3.2, 0.0, 1.0]]
    x_t, y_t = -2.0, -3.0
    x_i, y_i = [x_t], [y_t]
    x, y = x_t, y_t

    for i in range(7):
        side = 0.0 if i < 3 else -1
        
        d_x = (count[i]-1) * steps[i]
        d_y = d_x * slope

        x += d_x
        y += d_y
        
        x_i.append(x)
        y_i.append(y + side)

    conveyor_layout_data = [
        [[x_i[i] + j * steps[i] for j in range(count[i])] for i in range(7)],
        [[y_i[i] + j * steps[i] * slope for j in range(count[i])] for i in range(7)]]

    conveyor_layout_figures = [
        go.Scatter(
            x=conveyor_layout_data[0][i],
            y=conveyor_layout_data[1][i],
            mode='markers+lines',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5}
            })
        for i in range(7)] + [
        go.Scatter(
            x=pulleys[0],
            y=pulleys[1],
            mode='markers',
            marker={
                'size': 50,
                'opacity': 0.5}),
        go.Scatter(
            x=source[0],
            y=source[1],
            mode='lines',
            line={
                'width': 0.5}),
        go.Scatter(
            x=target[0],
            y=target[1],
            mode='lines',
            line={
                'width': 0.5})]

    return conveyor_layout_figures

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
