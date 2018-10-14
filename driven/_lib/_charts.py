# -*- coding: utf-8 -*-

"""Preprocess the data for go plotting."""

import copy

from plotly.basedatatypes import BaseTraceType
import plotly.graph_objs as go

from practical.types import (
    exactly,
    one_of,
    trace_data,
    typecheck)

#####################################################################
# DATA WRAPPING
#####################################################################

@typecheck
def wrap_data(
        data: trace_data,
        trace_type: one_of(exactly('bar'),exactly('scatter'))='scatter',
        trace_style: dict=dict()) -> BaseTraceType:
    """
    Wraps numeric data into a plotly trace object.

    Parameters
    ----------
    data: trace_data.
        A dictionnary with x and y data of appropriate types.

    Returns
    -------
    out: plotly.basedatatypes.BaseTraceType.
        The plotly data trace.
    """
    style = trace_style
    if trace_type == 'bar':
        if not style:
            style = _bar_style(60, 200, 230)

        return go.Bar(
            x=data.get('x'),
            y=data.get('y'),
            name=data.get('name',''),
            **style)
    elif trace_type == 'scatter':
        if not style:
            style = _scatter_style(60, 200, 230)
            
        return go.Scatter(
            x=data.get('x'),
            y=data.get('y'),
            name=data.get('name',''),
            mode='lines',
            **style)

#####################################################################
# TRACE STYLE
#####################################################################

def _bar_style(red, green, blue):
    return dict(
        orientation = 'v',
        width=0.5,
        opacity=0.6,
        marker=dict(
            color='rgba({},{},{},1.0)'.format(red, green, blue),
            line=dict(
                color='rgba({},{},{},0.5)'.format(red, green, blue),
                width=2)))

def _scatter_style(red, green, blue):
    return dict(
        mode='lines',
        line=dict(
            color='rgba({},{},{},0.5)'.format(red, green, blue),
            width=2))
