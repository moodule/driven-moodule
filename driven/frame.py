# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# HEADER
#####################################################################

def make_title():
    return html.H1(
        id='title_text',
        className='eight columns')

def make_logo():
    return html.Img(
        id='logo_image',
        src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
        className='one columns',
        style={
            'height': '100',
            'width': '225',
            'float': 'right',
            'position': 'relative'})

def update_title():
    return 'New Belt Conveyor - Design'

#####################################################################
# SUMMARY
#####################################################################

def make_risk_summary_container():
    return html.Div(
        id='risk_summary_container',
        children=[
            html.H5(id='risk_summary_text', style={'text-align':'left'}),
            html.Span(id='risk_summary_tooltip', className='tooltiptext')],
        className='two columns tooltip')

def make_cost_summary_container():
    return html.Div(
        id='cost_summary_container',
        children=[
            html.H5(id='cost_summary_text', style={'text-align':'center'}),
            html.Span(id='cost_summary_tooltip', className='tooltiptext')],
        className='eight columns tooltip')

def make_reliability_summary_container():
    return html.Div(
        id='reliability_summary_container',
        children=[
            html.H5(id='reliability_summary_text', style={'text-align':'right'}),
            html.Span(id='reliability_summary_tooltip', className='tooltiptext')],
        className='two columns tooltip')

def update_risk_summary_text():
    return 'Risks : 800 Sources'

def update_risk_summary_tooltip():
    return 'Can be lowered to 560'

def update_cost_summary_text():
    return 'Buying : 10 k€ | Operating : 4 k€/year | Maintenance : 2 k€/year'

def update_cost_summary_tooltip():
    return 'Can be lowered to 7 k€ | 3.5 k€/year | 1.5 k€/year'

def update_reliability_summary_text():
    return 'Wear : Low'

def update_reliability_summary_tooltip():
    return ''

#####################################################################
# FOOTER
#####################################################################

def make_footer():
    return html.Div(
        id='footer_container',
        children=[],
        className='row')