# -*- coding: utf-8 -*-
import copy
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

mapbox_access_token = ''

#####################################################################
# APP
#####################################################################

app = dash.Dash('Industrious')
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
                navigation_graph(),
                local_design_form()],
            className='row'),
        html.Div(
            children=[
                safety_graph(),
                cost_graph(),
                reliability_graph()],
            className='row'),
        html.Div(
            children=[
                conveyor_layout_graph()],
            className='row')],
    id='main_container',
    className='ten columns offset-by-one')

widget_layout = dict(
    autosize=True,
    height=500,
    font=dict(color='#CCCCCC'),
    titlefont=dict(color='#CCCCCC', size='14'),
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
# EVENTS
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


#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
