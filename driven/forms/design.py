# -*- coding: utf-8 -*-
import math

import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# LOCAL DESIGN
#####################################################################
def local_design_form(id='local-design-form', style={}):
    rows = [
        [
            html.Label('Delta-x (m)', id='section-delta-x-label', htmlFor='section-delta-x-input'),
            dcc.RangeSlider(id='section-delta-x-input', value=[0.0, 1.0e3], min=0.0, step=0.5, max=1.0e3, marks={1: 0.0, 2:100.0, 3:1.0e3})],
        [
            html.Label('Delta-y (m)', id='section-delta-y-label', htmlFor='section-delta-y-input'),
            dcc.RangeSlider(id='section-delta-y-input', value=[0.0, 0.0], min=-1.0e2, step=0.5, max=1.0e2, marks={1:-1.0e2, 2:0.0, 3:1.0e2})],
        [
            html.Label('Support step (m)', id='support-step-label', htmlFor='support-step-input'),
            dcc.RangeSlider(id='support-step-input', value=[1.0, 3.0], min=0.0, step=1.0e-1, max=1.0e1, marks={1:0.0, 2:1.5, 3:1.0e1})],
        [
            html.Label('Support sector length (m)', id='support-sector-length-label', htmlFor='support-sector-length-input'),
            dcc.RangeSlider(id='support-sector-length-input', value=[0.38, 0.38], min=0.1, step=1.0e-2, max=1.0, marks={1:0.1, 2:0.38, 3:1.0})],
        [
            html.Label('Support sector width (m)', id='support-sector-width-label',htmlFor='support-sector-width-input'),
            dcc.RangeSlider(id='support-sector-width-input', value=[0.1, 0.1], min=0.02, step=1.0e-2, max=1.0, marks={1:0.02, 2:0.1, 3:1.0})],
        [
            html.Label('Support troughing angle (°)', id='support-troughing-angle-label',htmlFor='support-troughing-angle-input'),
            dcc.RangeSlider(id='support-troughing-angle-input', value=[10.0, 45.0], min=0.0, step=5.0, max=90.0, marks={1:0.0, 2:30.0, 3:90.0})]]

    return html.Form(
        children=html.Fieldset(
            children=[html.P(children=list(r)) for r in rows]),
        id=id,
        style=style)
