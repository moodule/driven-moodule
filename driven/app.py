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
from driven.forms.design import (
    make_global_design_geometry_form,
    make_global_design_components_form,
    make_global_design_systems_form,
    make_local_design_form)
from driven.forms.objectives import (
    make_objectives_form)
from driven.forms.specifications import (
    make_location_form,
    make_location_map,
    make_specifications_form)
from driven.frame import (
    make_title,
    make_logo,
    make_cost_summary_container,
    make_reliability_summary_container,
    make_risk_summary_container,
    update_risk_summary_text,
    update_risk_summary_tooltip,
    update_cost_summary_text,
    update_cost_summary_tooltip,
    update_reliability_summary_text,
    update_reliability_summary_tooltip,
    make_footer)

#####################################################################
# THIRD PARTY
#####################################################################

mapbox_access_token = 'pk.eyJ1IjoibW9vZHVsZSIsImEiOiJjam1lcW1qNW0wcG9rM3dsbHY2N2ZyZ29iIn0.TkBXhBxfadbKKkRH7320Ng'

#####################################################################
# APP
#####################################################################

app = dash.Dash(__name__)
# app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

server = app.server

#####################################################################
# PAGE LAYOUT
#####################################################################

app.layout = html.Div(
    children=[
        html.Div(
            id='header_container',
            children=[
                make_title(),
                make_logo()],
            className='row'),
        html.Div(
            id='summary_container',
            children=[
                make_risk_summary_container(),
                make_cost_summary_container(),
                make_reliability_summary_container()],
            className='row'),
        html.Div(
            id='specifications_container',
            children=[
                make_specifications_form(),
                make_location_form()],
            className='row',
            style={'margin-top':'40px'}),
        html.Div(
            id='objective_graph_container',
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
            className='row'),
        html.Div(
            id='design_container',
            children=[
                make_global_design_geometry_form(),
                make_global_design_components_form(),
                make_global_design_systems_form()],
            className='row')],
    id='main_container',
    className='ten columns offset-by-one')

#####################################################################
# WIDGET LAYOUT
#####################################################################

input_layout = dict(
    autosize=True,
    font=dict(color='#000000'),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0),
    hovermode="closest",
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF",
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-78.05,
            lat=42.54),
        zoom=7))

output_layout = dict(
    autosize=True,
    height=500,
    font=dict(color='#CCCCCC'),
    titlefont=dict(color='#CCCCCC', size=14),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45),
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
            lat=42.54),
        zoom=7))

#####################################################################
# UPDATE RISK SUMMARY
#####################################################################

@app.callback(
    dash.dependencies.Output('risk_summary_text', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_risk_summary_text(x, y, q, p):
    return update_risk_summary_text()

@app.callback(
    dash.dependencies.Output('risk_summary_tooltip', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_risk_summary_tooltip(x, y, q, p):
    return update_risk_summary_tooltip()

#####################################################################
# UPDATE COST SUMMARY
#####################################################################

@app.callback(
    dash.dependencies.Output('cost_summary_text', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_buying_cost_summary_text(x, y, q, p):
    return update_cost_summary_text()

@app.callback(
    dash.dependencies.Output('cost_summary_tooltip', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_buying_cost_summary_tooltip(x, y, q, p):
    return update_cost_summary_tooltip()

#####################################################################
# UPDATE RELIABILITY SUMMARY
#####################################################################

@app.callback(
    dash.dependencies.Output('reliability_summary_text', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_reliability_summary_text(x, y, q, p):
    return update_reliability_summary_text()

@app.callback(
    dash.dependencies.Output('reliability_summary_tooltip', 'children'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_reliability_summary_tooltip(x, y, q, p):
    return update_reliability_summary_tooltip()

#####################################################################
# UPDATE SPECIFICATIONS
#####################################################################

def exp_range(r):
    return [10.0**e for e in r]

@app.callback(
    dash.dependencies.Output('total_delta_x_label', 'children'),
    [dash.dependencies.Input('total_delta_x_input', 'value')])
def _update_delta_x_label(x_range):
    return display_value_in_label(
        value_range=exp_range(x_range),
        label_text='{} m',
        precision=0)

@app.callback(
    dash.dependencies.Output('total_delta_y_label', 'children'),
    [dash.dependencies.Input('total_delta_y_input', 'value')])
def _update_delta_y_label(y_range):
    return display_value_in_label(
        value_range=y_range,
        label_text='{} m',
        precision=0)

@app.callback(
    dash.dependencies.Output('output_label', 'children'),
    [dash.dependencies.Input('output_input', 'value')])
def _update_output_label(output_range):
    return display_value_in_label(
        value_range=exp_range(output_range),
        label_text='{} t/h',
        precision=0)

@app.callback(
    dash.dependencies.Output('product_density_input', 'value'),
    [dash.dependencies.Input('product_name_input', 'value')])
def _update_density_input(product_id):
    product = bulk_material_data().get(product_id, [])
    if product:
        return 0.001 * product[1]

@app.callback(
    dash.dependencies.Output('product_surcharge_angle_input', 'value'),
    [dash.dependencies.Input('product_name_input', 'value')])
def _update_surcharge_angle_input(product_id):
    product = bulk_material_data().get(product_id, [])
    if product:
        return 180.0 * product[2] / math.pi

#####################################################################
# UPDATE GRAPHS
#####################################################################

@app.callback(
    dash.dependencies.Output('location_map', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_location_map(x, y, q, p):
    return make_location_map(input_layout)

@app.callback(
    dash.dependencies.Output('safety_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_safety_graph(x, y, q, p):
    return make_safety_figure(output_layout)

@app.callback(
    dash.dependencies.Output('cost_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_safety_graph(x, y, q, p):
    return make_cost_figure(output_layout)

@app.callback(
    dash.dependencies.Output('reliability_graph', 'figure'),
    [
        dash.dependencies.Input('total_delta_x_input', 'value'),
        dash.dependencies.Input('total_delta_y_input', 'value'),
        dash.dependencies.Input('output_input', 'value'),
        dash.dependencies.Input('product_name_input', 'value')])
def _update_safety_graph(x, y, q, p):
    return make_reliability_figure(output_layout)

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
