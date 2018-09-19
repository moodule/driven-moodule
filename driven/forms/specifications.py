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
# INPUT ROWS
#####################################################################
def specifications_form(id='specifications-form', style={}):
    specification_form_rows = [
        [
            html.Label('Delta-x (m)', id='total-delta-x-label', htmlFor='total-delta-x-input'),
            dcc.RangeSlider(id='total-delta-x-input', allowCross=False, value=[1.0e1, 1.0e1], min=1.0, step=1.0, max=1.0e3)],
        [
            html.Label('Delta-y (m)', id='total-delta-y-label', htmlFor='total-delta-y-input'),
            dcc.RangeSlider(id='total-delta-y-input', allowCross=False, value=[0.0, 0.0], min=-1.0e2, step=0.5, max=1.0e2)],
        [
            html.Label('Output (t/h)', id='output-label', htmlFor='output-input'),
            dcc.RangeSlider(id='output-input', allowCross=False, value=[0.0, 100.0], min=0.0, step=1.0, max=1.0e3)],
        [
            html.Label('Product', id='product-name-label', htmlFor='product-name-input'),
            dcc.Dropdown(
                id='product-name-input',
                options=[
                    {'label': product[0], 'value': pid}
                    for pid, product in bulk_material_data().items()],
                clearable=False,
                multi=False,
                placeholder='Select a product')],
        [
            html.Label('Bulk Density (t/m³)', id='product-density-label', htmlFor='product-density-input', style={'display': 'none'}),
            dcc.Input(id='product-density-input', type='number', value=0.5, min=1.0e-2, step=1.0e-2, max=1.0e2, style={'display': 'none'})],
        [
            html.Label('Surcharge Angle (°)', id='product-surcharge-angle-label',htmlFor='product-surcharge-angle-input', style={'display': 'none'}),
            dcc.Input(id='product-surcharge-angle-input', type='number', value=20.0, min=0.0, step=1.0, max=90.0, style={'display': 'none'})]]

    return html.Form(
        children=html.Fieldset(
            children=[html.P(children=list(r), style={'padding':'0 10px 20px 10px'}) for r in specification_form_rows]),
        id=id,
        style=style)
