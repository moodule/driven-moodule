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
# SPECIFICATIONS
#####################################################################
def _geometry_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Delta_x (m)',
                        id='total_delta_x_label',
                        htmlFor='total_delta_x_input'),
                    dcc.RangeSlider(
                        id='total_delta_x_input',
                        allowCross=False,
                        value=[1.0, 1.0],
                        min=0.0,
                        step=0.1,
                        max=4.0,
                        marks={0.0:'1 m', 1.0:'10 m', 2.0:'100 m', 3.0:'1 km', 4.0:'10 km'})],
                className='eight columns'),
            html.Div(
                children=[
                    html.Label(
                        'Delta_y (m)',
                        id='total_delta_y_label',
                        htmlFor='total_delta_y_input'),
                    dcc.RangeSlider(
                        id='total_delta_y_input',
                        allowCross=False,
                        value=[0.0, 0.0],
                        min=-1.0e2,
                        step=0.5,
                        max=1.0e2,
                        vertical=True,
                        marks={-100.0:'-100 m', -10.0:'-10 m', 0.0:'0', 10.0:'10 m', 100.0:'100 m'})],
                className='four columns')],
        className='row')

def _product_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Output (t/h)',
                        id='output_label',
                        htmlFor='output_input'),
                    dcc.RangeSlider(
                        id='output_input',
                        allowCross=False,
                        value=[0.0, 100.0],
                        min=0.0,
                        step=1.0,
                        max=1.0e3)],
                    className='eight columns'),
            html.Div(
                children=[
                    html.Label(
                        'Product',
                        id='product_name_label',
                        htmlFor='product_name_input'),
                    dcc.Dropdown(
                        id='product_name_input',
                        clearable=False,
                        searchable=True,
                        multi=False,
                        placeholder='Select a product',
                        options=[
                            {'label': product[0], 'value': pid}
                            for pid, product in bulk_material_data().items()])],
                    className='four columns'),
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
        className='row')

def specifications_form():
    return html.Form(
        children=html.Fieldset(
            children=[
                _geometry_form(),
                _product_form()]),
        id='specifications_form',
        className='eight columns')

###############################################################################
# LOCATION
###############################################################################
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
        className='four columns')