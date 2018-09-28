# -*- coding: utf-8 -*-
import copy

import plotly.graph_objs as go

from driven.data.testing import _random_navigation_data

#####################################################################
# OVERVIEW GRAPH
#####################################################################
def make_overview_figure(layout):
    data = [
        go.Scatterpolar(
            r = [7, 5, 3, 8],
            theta = ['Safety', 'Cost','Reliability', 'Stabiliy'],
            fill = 'toself',
            name = 'User design'),
        go.Scatterpolar(
            r = [10, 8, 6, 9],
            theta = ['Safety', 'Cost','Reliability', 'Stabiliy'],
            fill = 'toself',
            name = 'Optimal design')]

    overview_layout = copy.deepcopy(layout)
    overview_layout['polar'] = dict(
        radialaxis=dict(
        visible=True,
        range=[0, 10]))
    overview_layout['showlegend'] = False
    overview_layout['margin'] = go.layout.Margin(l=40, r=40, t=40, b=40)

    return dict(data=data, layout=go.Layout(overview_layout))

#####################################################################
# COST
#####################################################################
def make_cost_figure(layout):
    x = ['Buying Cost', 'Operating Cost', 'Maintenance Cost']
    y = [20, 14, 23]
    y2 = [16, 12, 10]
    data = [
        go.Bar(
            name='User Design',
            x=x,
            y=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),),
            opacity=0.6),
        go.Bar(
            name='Optimal Design',
            x=x,
            y=y2,
            textposition = 'auto',
            marker=dict(
                color='rgb(58,200,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),),
            opacity=0.6)]

    cost_layout = copy.deepcopy(layout)
    cost_layout['title'] = 'Project Costs'
    cost_layout['barmode'] = 'group'
    cost_layout['xaxis'] = dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'))
    cost_layout['yaxis'] = dict(
        title='kilo €',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'))
    cost_layout['legend']=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)')
    cost_layout['showlegend'] = True
    cost_layout['margin'] = go.layout.Margin(l=40, r=40, t=40, b=40)

    return dict(data=data, layout=go.Layout(cost_layout))

#####################################################################
# SAFETY
#####################################################################
def make_safety_figure(layout):
    x = ['Snatching', 'Falling', 'Cutting']
    y = [760, 400, 4]
    y2 = [230, 120, 2]
    data = [
        go.Bar(
            name='User Design',
            x=x,
            y=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),),
            opacity=0.6),
        go.Bar(
            name='Optimal Design',
            x=x,
            y=y2,
            textposition = 'auto',
            marker=dict(
                color='rgb(58,200,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),),
            opacity=0.6)]

    safety_layout = copy.deepcopy(layout)
    safety_layout['title'] = 'Safety Concerns'
    safety_layout['barmode'] = 'group'
    safety_layout['showlegend'] = True
    safety_layout['margin'] = go.layout.Margin(l=40, r=40, t=40, b=40)

    return dict(data=data, layout=go.Layout(safety_layout))

#####################################################################
# RELIABILITY
#####################################################################
def make_reliability_figure(layout):
    x = ['Belt RMBT', 'Idlers RMBT/Wear', 'Pulleys RMBT/Wear', 'Laggings RMBT/Wear', 'Splice RMBT']
    y1 = [110, 40, 40, 150, 130]
    y2 = [80, 60, 50, 70, 90]
    data = [
        go.Bar(
            name='User Design',
            x=x,
            y=y1,
            textposition = 'auto',
            opacity=0.6),
        go.Bar(
            name='Optimal Design',
            x=x,
            y=y2,
            textposition = 'auto',
            opacity=0.6)]

    reliability_layout = copy.deepcopy(layout)
    reliability_layout['title'] = 'Min/Max/Average Wear'
    reliability_layout['barmode'] = 'group'
    reliability_layout['yaxis'] = dict(title='RMBT (%)')
    reliability_layout['showlegend'] = False
    reliability_layout['margin'] = go.layout.Margin(l=40, r=40, t=40, b=40)

    return dict(data=data, layout=go.Layout(reliability_layout))

#####################################################################
# Stability
#####################################################################
def make_stability_figure(layout):
    x = ['Pulley Traction (%)', 'Belt Tracking (%)', 'Belt Lifting (m)']
    y = [60, 80, 0]
    y2 = [100, 100, 0]
    data = [
        go.Bar(
            name='User Design',
            x=x,
            y=y,
            textposition = 'auto',
            opacity=0.6),
        go.Bar(
            name='Optimal Design',
            x=x,
            y=y2,
            textposition = 'auto',
            opacity=0.6)]

    stability_layout = copy.deepcopy(layout)
    stability_layout['title'] = 'Stability of the Conveyor'
    stability_layout['barmode'] = 'group'
    stability_layout['showlegend'] = False
    stability_layout['margin'] = go.layout.Margin(l=40, r=40, t=40, b=40)

    return dict(data=data, layout=go.Layout(stability_layout))