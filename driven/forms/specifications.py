# -*- coding: utf-8 -*-
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
def specifications_form():
    specification_form_rows = [
        [
            html.Label('Delta_x (m)', id='total_delta_x_label', htmlFor='total_delta_x_input'),
            dcc.RangeSlider(id='total_delta_x_input', allowCross=False, value=[1.0e1, 1.0e1], min=1.0, step=1.0, max=1.0e3)],
        [
            html.Label('Delta_y (m)', id='total_delta_y_label', htmlFor='total_delta_y_input'),
            dcc.RangeSlider(id='total_delta_y_input', allowCross=False, value=[0.0, 0.0], min=-1.0e2, step=0.5, max=1.0e2)],
        [
            html.Label('Output (t/h)', id='output_label', htmlFor='output_input'),
            dcc.RangeSlider(id='output_input', allowCross=False, value=[0.0, 100.0], min=0.0, step=1.0, max=1.0e3)],
        [
            html.Label('Product', id='product_name_label', htmlFor='product_name_input'),
            dcc.Dropdown(
                id='product_name_input',
                options=[
                    {'label': product[0], 'value': pid}
                    for pid, product in bulk_material_data().items()],
                clearable=False,
                multi=False,
                placeholder='Select a product')],
        [
            html.Label('Bulk Density (t/m³)', id='product_density_label', htmlFor='product_density_input', style={'display': 'none'}),
            dcc.Input(id='product_density_input', type='number', value=0.5, min=1.0e-2, step=1.0e-2, max=1.0e2, style={'display': 'none'})],
        [
            html.Label('Surcharge Angle (°)', id='product_surcharge_angle_label',htmlFor='product_surcharge_angle_input', style={'display': 'none'}),
            dcc.Input(id='product_surcharge_angle_input', type='number', value=20.0, min=0.0, step=1.0, max=90.0, style={'display': 'none'})]]

    return html.Form(
        children=html.Fieldset(
            children=[html.P(children=list(r), style={'padding':'0 10px 20px 10px'}) for r in specification_form_rows]),
        id='specifications_form',
        className='six columns')

###############################################################################
# LOCATION
###############################################################################

def location_form():
    return html.Div(
        id='location_form',
        className='six columns')