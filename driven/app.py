# -*- coding: utf-8 -*-
import copy
import math

import dash
import dash_core_components as dcc
import dash_html_components as html

from driven._lib import *
from driven.charts.layout import conveyor_layout_graph
from driven.charts.navigation import navigation_graph
from driven.charts.objectives import (
    make_overview_figure,
    make_cost_figure,
    make_safety_figure,
    make_reliability_figure,
    make_stability_figure)
from driven.data.referential import bulk_material_data
from driven.forms.design import local_design_form
from driven.forms.objectives import objectives_form
from driven.forms.specifications import (
    specifications_form,
    location_form)
from driven.frame import (
    header,
    summary,
    footer)

#####################################################################
# THIRD PARTY
#####################################################################

mapbox_access_token = 'pk.eyJ1IjoibW9vZHVsZSIsImEiOiJjam1lcW1qNW0wcG9rM3dsbHY2N2ZyZ29iIn0.TkBXhBxfadbKKkRH7320Ng'

#####################################################################
# APP
#####################################################################

app = dash.Dash('Driven')
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

server = app.server

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=[
        header(),
        summary(),
        html.Div(
            children=[
                specifications_form(),
                location_form()],
            className='row'),
        html.Div(
            children=[
                html.Div(
                    children=[dcc.Graph(id='safety_graph')],
                    className='four columns',
                    style={'margin-top': '10'}),
                html.Div(
                    children=[dcc.Graph(id='cost_graph')],
                    className='four columns',
                    style={'margin-top': '10'}),
                html.Div(
                    children=[dcc.Graph(id='reliability_graph')],
                    className='four columns',
                    style={'margin-top': '10'}),],
            className='row')],
    id='main_container',
    className='ten columns offset-by-one')

widget_layout = dict(
    autosize=True,
    height=500,
    font=dict(color='#CCCCCC'),
    titlefont=dict(color='#CCCCCC', size=14),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor="#191A1A",
    paper_bgcolor="#020202",
    legend=dict(font=dict(size=10), orientation='h'),
    title='Satellite Overview',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="dark",
        center=dict(
            lon=-78.05,
            lat=42.54
        ),
        zoom=7,
    )
)

#####################################################################
# UPDATE SPECIFICATIONS
#####################################################################

@app.callback(
    dash.dependencies.Output('total_delta_x_label', 'children'),
    [dash.dependencies.Input('total_delta_x_input', 'value')])
def update_delta_x_label(x_range):
    return display_value_in_label(x_range, 'Delta-x (m)')

@app.callback(
    dash.dependencies.Output('total_delta_y_label', 'children'),
    [dash.dependencies.Input('total_delta_y_input', 'value')])
def update_delta_y_label(y_range):
    return display_value_in_label(y_range, 'Delta-y (m)')

@app.callback(
    dash.dependencies.Output('output_label', 'children'),
    [dash.dependencies.Input('output_input', 'value')])
def update_output_label(output_range):
    return display_value_in_label(output_range, 'Output (t/h)')

@app.callback(
    dash.dependencies.Output('product_density_input', 'value'),
    [dash.dependencies.Input('product_name_input', 'value')])
def update_density_input(product_id):
    product = bulk_material_data().get(product_id, [])
    if product:
        return 0.001 * product[1]

@app.callback(
    dash.dependencies.Output('product_surcharge_angle_input', 'value'),
    [dash.dependencies.Input('product_name_input', 'value')])
def update_surcharge_angle_input(product_id):
    product = bulk_material_data().get(product_id, [])
    if product:
        return 180.0 * product[2] / math.pi

###############################################################################
# UPDATE GRAPHS
###############################################################################

@app.callback(
    dash.dependencies.Output('safety_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def update_safety_graph(x, y, q, p):
    return make_safety_figure(widget_layout)

@app.callback(
    dash.dependencies.Output('cost_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def update_safety_graph(x, y, q, p):
    return make_cost_figure(widget_layout)

@app.callback(
    dash.dependencies.Output('reliability_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def update_safety_graph(x, y, q, p):
    return make_reliability_figure(widget_layout)

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
