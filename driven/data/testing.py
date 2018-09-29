# -*- coding: utf-8 -*-

"""
================
Internal toolbox
================

Documentation is available in the docstrings and
online at __

Subpackages
-----------
"""

from __future__ import division, print_function, absolute_import

import random

import plotly.graph_objs as go
from practical.memory import memoize

#####################################################################
# STYLE
#####################################################################

def bar_style(red, green, blue):
    return dict(
        orientation = 'v',
        width=0.5,
        opacity=0.6,
        marker=dict(
            color='rgb({},{},{},1.0)'.format(red, green, blue),
            line=dict(
                color='rgb({},{},{},0.5)'.format(red, green, blue),
                width=1.5)))

#####################################################################
# FAKE LAYOUTS
#####################################################################
@memoize
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
# FAKE NAVIGATION
#####################################################################
@memoize
def _random_navigation_data():
    return [
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
# FAKE COSTS
#####################################################################
@memoize
def _random_cost_data():
    buying_cost = [
        go.Bar(
            x=['Buying'],
            y=[random.randrange(10)],
            name='Idlers',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Buying'],
            y=[random.randrange(10)],
            name='Belt',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Buying'],
            y=[random.randrange(10)],
            name='Pulleys',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Buying'],
            y=[random.randrange(10)],
            name='Drives & Reducers',
            **bar_style(160, 200, 220))]

    operating_cost = [
        go.Bar(
            x=['Operating'],
            y=[random.randrange(10)],
            name='Best Case',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Operating'],
            y=[random.randrange(10)],
            name='Average Case',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Operating'],
            y=[random.randrange(10)],
            name='Worst Case',
            **bar_style(160, 200, 220))]

    maintenance_cost = [
        go.Bar(
            x=['Maintenance'],
            y=[random.randrange(10)],
            name='Best Case',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Maintenance'],
            y=[random.randrange(10)],
            name='Average Case',
            **bar_style(160, 200, 220)),
        go.Bar(
            x=['Maintenance'],
            y=[random.randrange(10)],
            name='Worst Case',
            **bar_style(160, 200, 220))]

    return buying_cost + operating_cost + maintenance_cost

@memoize
def _random_safety_data():
    return

@memoize
def _random_reliability_data():
    return