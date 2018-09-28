# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# HEADER
#####################################################################

def header():
    title = html.H1(
        children='Belt Conveyor - Design',
        className='eight columns')
    logo = html.Img(
        src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
        className='one columns',
        style={
            'height': '100',
            'width': '225',
            'float': 'right',
            'position': 'relative',})

    return html.Div(
        id='header',
        children=[title, logo],
        className='row')

def summary():
    return html.Div(
        children=[
            html.H5(
                'Risks : ',
                id='risk_text',
                className='two columns'),
            html.H5(
                'Cost : ',
                id='cost_text',
                className='eight columns',
                style={'text-align': 'center'}),
            html.H5(
                'Lifespan : ?',
                id='lifespan_text',
                className='two columns',
                style={'text-align': 'right'}),],
        className='row')

#####################################################################
# FOOTER
#####################################################################

def footer():
    return html.Div(
        id='footer',
        children=[],
        className='row')