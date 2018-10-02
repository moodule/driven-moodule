# -*- coding: utf-8 -*-
import copy
import math

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from driven._lib import *
from driven.data.referential import bulk_material_data

# TODO even the row height in the forms
# TODO add spaces between labels and inputs

#####################################################################
# PRODUCT
#####################################################################
def _product_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Transporting',
                        className='two columns'),
                    dcc.Dropdown(
                        id='product_name_input',
                        clearable=False,
                        searchable=True,
                        multi=False,
                        placeholder='Select a product',
                        options=[
                            {'label': product[0], 'value': pid}
                            for pid, product in bulk_material_data().items()],
                        className='three columns'),
                    html.Label(
                        'At',
                        className='one columns'),
                    dcc.RangeSlider(
                        id='output_input',
                        allowCross=False,
                        value=[0.0, 100.0],
                        min=0.0,
                        step=1.0,
                        max=1.0e3,
                        className='four columns'),
                    html.Label(
                        '',
                        id='output_label',
                        className='two columns')],
                    className='row'),
            html.Div(
                children=[
                    html.Label(
                        'Bulk Density (t/m³)',
                        id='product_density_label',
                        htmlFor='product_density_input'),
                    dcc.Input(
                        id='product_density_input',
                        type='number',
                        value=0.5,
                        min=1.0e-2,
                        step=1.0e-2,
                        max=1.0e2),
                    html.Label(
                        'Surcharge Angle (°)',
                        id='product_surcharge_angle_label',
                        htmlFor='product_surcharge_angle_input'),
                    dcc.Input(
                        id='product_surcharge_angle_input',
                        type='number',
                        value=20.0,
                        min=0.0,
                        step=1.0,
                        max=90.0)],
                style={'display': 'none'})],
        className='three rows')

#####################################################################
# GEOMETRY
#####################################################################
def _geometry_form():
    return html.Div(
        children=[
            html.Label(
                'Over',
                className='two columns'),
            dcc.RangeSlider(
                id='total_delta_x_input',
                allowCross=False,
                value=[1.0, 1.0],
                min=0.0,
                step=0.1,
                max=4.0,
                marks={0.0:'1 m', 1.0:'10 m', 2.0:'100 m', 3.0:'1 km', 4.0:'10 km'},
                className='four columns'),
            html.Label(
                '',
                id='total_delta_x_label',
                className='two columns'),
            dcc.RangeSlider(
                id='total_delta_y_input',
                allowCross=False,
                value=[0.0, 0.0],
                min=-1.0e2,
                step=0.5,
                max=1.0e2,
                vertical=True,
                marks={-100.0:'-100 m', -10.0:'-10 m', 0.0:'0', 10.0:'10 m', 100.0:'100 m'},
                className='two columns'),
            html.Label(
                '',
                id='total_delta_y_label',
                className='two columns')],
        className='three rows')

#####################################################################
# META
#####################################################################
def _priority_form():
    return html.Div(
        children=[
            html.Label(
                'With',
                className='two columns'),
            dcc.Dropdown(
                id='priority_input',
                clearable=False,
                searchable=True,
                multi=False,
                placeholder='Select a priority',
                options=[
                    {'label': 'Cost', 'value': 0},
                    {'label': 'Reliability', 'value': 1},
                    {'label': 'Safety', 'value': 2}],
                className='two columns'),
            html.Label(
                'as priority',
                className='two columns')],
        className='three rows')

def _scenario_form():
     return html.Div(
        children=[
            html.Label(
                'Considering',
                className='two columns'),
            dcc.Dropdown(
                id='scenario_input',
                clearable=False,
                searchable=True,
                multi=False,
                placeholder='Select a scenario',
                options=[
                    {'label': 'All', 'value': 0},
                    {'label': 'The best', 'value': 1},
                    {'label': 'The average', 'value': 2},
                    {'label': 'The worst', 'value': 3}],
                className='two columns'),
            html.Label(
                'case scenario',
                className='two columns')],
        className='three rows')

#####################################################################
# LOCATION
#####################################################################
def make_location_map(layout):
    data = [
        go.Scattermapbox(
            lat=['45.5017'],
            lon=['-73.5673'],
            mode='markers',
            marker=dict(
                size=14),
            text=['Montreal'])]

    return dict(data=data, layout=layout)

def location_form():
    return html.Div(
        children=[dcc.Graph(id='location_map')],
        id='location_form',
        className='four columns',
        style={'height':'300px'})

#####################################################################
# CONTAINER
#####################################################################
def specifications_form():
    return html.Div(
        id='specifications_form',
        children=[
            _product_form(),
            _geometry_form(),
            _priority_form(),
            _scenario_form()],
        className='eight columns',
        style={'height':'300px'})
