# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# LOCAL DESIGN
#####################################################################
def local_design_form():
    rows = [
        [
            html.Label(
                'Delta-x (m)',
                id='section-delta-x-label'),
            dcc.RangeSlider(
                id='section-delta-x-input',
                allowCross=False,
                min=0.0,
                step=0.5,
                max=1.0e3,
                marks={
                    0:"0 m",
                    100:{'label': '100 m', 'style': {'color': '#f50'}},
                    1000:"1000 m"},
                value=[0.0, 1.0e3])],
        [
            html.Label(
                'Delta-y (m)',
                id='section-delta-y-label'),
            dcc.RangeSlider(
                id='section-delta-y-input',
                allowCross=False,
                min=-1.0e2,
                step=0.5,
                max=1.0e2,
                marks={
                    -100:'-100 m',
                    0:{'label': '0 m', 'style': {'color': '#f50'}},
                    100:'100 m'},
                value=[0.0, 0.0],)],
        [
            html.Label(
                'Support step (m)',
                id='support-step-label'),
            dcc.RangeSlider(
                id='support-step-input',
                allowCross=False,
                min=0.0,
                step=1.0e-1,
                max=1.0e1,
                marks={
                    0:"0 m",
                    1.5:{'label': '1.5 m', 'style': {'color': '#f50'}},
                    10:'10 m'},
                value=[1.0, 3.0])],
        [
            html.Label(
                'Support sector length (m)',
                id='support-sector-length-label'),
            dcc.RangeSlider(
                id='support-sector-length-input',
                allowCross=False,
                min=0.1,
                step=1.0e-2,
                max=1.0,
                marks={
                    0.1:'0.1 m',
                    0.38:{'label': '0.38 m', 'style': {'color': '#f50'}},
                    1:'1 m'},
                value=[0.38, 0.38])],
        [
            html.Label(
                'Support sector width (m)',
                id='support-sector-width-label'),
            dcc.RangeSlider(
                id='support-sector-width-input',
                allowCross=False,
                min=0.02,
                step=1.0e-2,
                max=1.0,
                marks={
                    0.02:'0.02 m',
                    0.1:{'label': '0.1 m', 'style': {'color': '#f50'}},
                    1:'1 m'},
                value=[0.1, 0.1])],
        [
            html.Label(
                'Support troughing angle (°)',
                id='support-troughing-angle-label'),
            dcc.RangeSlider(
                id='support-troughing-angle-input',
                allowCross=False,
                min=0.0,
                step=5.0,
                max=90.0,
                marks={
                    0:'0°',
                    30:{'label': '30°', 'style': {'color': '#f50'}},
                    90:'90°'},
                value=[10.0, 45.0])]]

    return html.Form(
        children=html.Fieldset(
            children=[html.P(children=list(r), style={'padding':'0 10px 20px 10px'}) for r in rows]),
        className='four columns')
