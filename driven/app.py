# -*- coding: utf-8 -*-
import math

import dash
import dash_html_components as html

from driven._lib import *
from driven.charts.layout import conveyor_layout_graph
from driven.charts.navigation import navigation_graph
from driven.charts.objectives import (
    rating_overview_graph,
    cost_graph,
    safety_graph,
    reliability_graph,
    stability_graph)
from driven.data.referential import bulk_material_data
from driven.forms.design import local_design_form
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
        # 'columnCount': 1,
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
        'backgroundColor': 'rgba(0,0,255,0.0)'},
    'navigation-graph': {
        'flex': '1 0 50%',
        'width': '50%',
        'backgroundColor': 'rgba(0,0,255,0.0)'}}

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
                navigation_graph(),
                local_design_form(style=styles['specifications-form'])],
            style={'display': 'flex', 'columnCount': 2}),
        html.Div(
            children=[
                rating_overview_graph(),
                cost_graph(),
                safety_graph(),
                reliability_graph(),
                stability_graph()],
            style={'display': 'flex', 'columnCount': 5}),
        html.Div(
            children=[
                conveyor_layout_graph(),],
            style={'display': 'flex', 'columnCount': 1})],
    id='main-container',
    style=styles['main-container'])

#####################################################################
# EVENTS
#####################################################################

@app.callback(
    dash.dependencies.Output('total-delta-x-label', 'children'),
    [dash.dependencies.Input('total-delta-x-input', 'value')])
def update_delta_x_label(x_range):
    return display_value_in_label(x_range, 'Delta-x (m)')

@app.callback(
    dash.dependencies.Output('total-delta-y-label', 'children'),
    [dash.dependencies.Input('total-delta-y-input', 'value')])
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
    product = bulk_material_data().get(product_id, [])
    if product:
        return 0.001 * product[1]

@app.callback(
    dash.dependencies.Output('product-surcharge-angle-input', 'value'),
    [dash.dependencies.Input('product-name-input', 'value')])
def update_surcharge_angle_input(product_id):
    product = bulk_material_data().get(product_id, [])
    if product:
        return 180.0 * product[2] / math.pi


#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
