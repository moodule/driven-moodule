# -*- coding: utf-8 -*-
import math
import sqlite3

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from driven.charts.layout import conveyor_layout_graph
from driven.charts.navigation import navigation_graph
from driven.charts.spider import spider_graph
from driven.forms.objectives import objectives_form
from driven.forms.specifications import specifications_form

#####################################################################
# APP
#####################################################################

app = dash.Dash('Industrious')
server = app.server

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

# app_style = {
#     'columnCount': 2}

#####################################################################
# STYLES
#####################################################################

styles = {
    'main-container': {
        'columnCount': 1,
        'backgroundColor': 'rgba(0,0,0,0.0)'},
    'specifications-form': {
        'flex': '1 0 50%',
        'width': '50%',
        'columnCount': 1,
        'backgroundColor': 'rgba(255,0,0,0.0)'},
    'objectives-form': {
        'flex': '1 0 50%',
        'width': '50%',
        'columnCount': 1,
        'backgroundColor': 'rgba(0,255,0,0.0)'},
    'conveyor-layout-graph': {
        'flex': '1 0 50%',
        'width': '50%',
        'backgroundColor': 'rgba(0,0,255,0.0)'}}

#####################################################################
# COST GRAPH
#####################################################################

# buying maintenance stock energy
# stack les coûts de chaque composant

#####################################################################
# SAFETY GRAPH
#####################################################################

# snatching falling ?

#####################################################################
# RELIABILITY GRAPH
#####################################################################

# rmbt : min, max, average

#####################################################################
# STABILITY GRAPH
#####################################################################

# spilling lifting

#####################################################################
# EXPORT BUTTON
#####################################################################

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                specifications_form(style=styles['specifications-form']),
                objectives_form(style=styles['objectives-form'])],
            style={'display': 'flex', 'columnCount': 2}),
        html.Div(
            children=[
                conveyor_layout_graph(),
                navigation_graph(),
                spider_graph()],
            style={'display': 'flex', 'columnCount': 2})],
    id='main-container',
    style=styles['main-container'])

#####################################################################
# CALLBACKS
#####################################################################

def display_value_in_label(value_range, label_text):
    if value_range[0] == value_range[1]:
        return '{} : {}'.format(label_text, value_range[0])
    else:
        return '{} : [{} ; {}]'.format(label_text, value_range[0], value_range[1])

@app.callback(
    dash.dependencies.Output('delta-x-label', 'children'),
    [dash.dependencies.Input('delta-x-input', 'value')])
def update_delta_x_label(x_range):
    return display_value_in_label(x_range, 'Delta-x (m)')

@app.callback(
    dash.dependencies.Output('delta-y-label', 'children'),
    [dash.dependencies.Input('delta-y-input', 'value')])
def update_delta_y_label(y_range):
    return display_value_in_label(y_range, 'Delta-y (m)')

@app.callback(
    dash.dependencies.Output('output-label', 'children'),
    [dash.dependencies.Input('output-input', 'value')])
def update_output_label(output_range):
    return display_value_in_label(output_range, 'Output (t/h)')

@app.callback(
    dash.dependencies.Output('product-density-input', 'value'),
    [dash.dependencies.Input('product-name-input', 'value')])
def update_density_input(product_id):
    product = product_catalog.get(product_id, [])
    if product:
        return 0.001 * product[1]

@app.callback(
    dash.dependencies.Output('product-surcharge-angle-input', 'value'),
    [dash.dependencies.Input('product-name-input', 'value')])
def update_surcharge_angle_input(product_id):
    product = product_catalog.get(product_id, [])
    if product:
        return 180.0 * product[2] / math.pi

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
