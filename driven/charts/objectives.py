# -*- coding: utf-8 -*-
import dash_core_components as dcc
import plotly.graph_objs as go

from driven.data.testing import _random_navigation_data

#####################################################################
# OVERVIEW GRAPH
#####################################################################
def rating_overview_graph(id='rating-overview-graph', style={}):
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

    layout = go.Layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 10])),
        showlegend=False,
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout))

#####################################################################
# COST
#####################################################################
def cost_graph(id='cost-graph', data=[]):
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

    layout = go.Layout(
        title='Project Costs',
        barmode='group',
        xaxis=dict(
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)')),
        yaxis=dict(
            title='€ (kilo)',
            titlefont=dict(
                size=16,
                color='rgb(107, 107, 107)'),
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)')),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'),
        showlegend=True,
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout))

#####################################################################
# SAFETY
#####################################################################
def safety_graph(id='safety-graph', data=[]):
    x = ['Snatching Hazards', 'Falling Hazards', 'Cutting Hazards']
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

    layout = go.Layout(
        title='Safety Concerns',
        barmode='group',
        showlegend=True,
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout))

#####################################################################
# RELIABILITY
#####################################################################
def reliability_graph(id='reliability-graph', data=[]):
    x = ['Belt RMBT', 'Idlers RMBT/Wear', 'Pulleys RMBT/Wear', 'Laggings RMBT/Wear', 'Splice RMBT']
    y = [110, 40, 40, 150, 130]
    y2 = [80, 60, 50, 70, 90]
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

    layout = go.Layout(
        title='Min/Max/Average Wear',
        barmode='group',
        yaxis=dict(title='RMBT (%)'),
        showlegend=False,
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout))

#####################################################################
# Stability
#####################################################################
def stability_graph(id='stability-graph', data=[]):
    x = ['Pulley Traction (%)', 'Belt Tracking (%)']
    y = [60, 80]
    y2 = [100, 100]
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

    layout = go.Layout(
        title='Stability of the Conveyor',
        barmode='group',
        showlegend=False,
        margin=go.layout.Margin(l=40, r=40, t=40, b=40))

    return dcc.Graph(
        id=id,
        figure=go.Figure(data=data, layout=layout))