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
    return 'Belt Conveyor - Design'

#####################################################################
# SUMMARY
#####################################################################

def make_risk_summary_container():
    return html.Div(
        id='risk_summary_container',
        children=[
            html.H5(id='risk_summary_text'),
            html.Span(id='risk_summary_tooltip', className='tooltiptext')],
        className='two columns tooltip')

def make_cost_summary_container():
    return html.Div(
        id='cost_summary_container',
        children=[
            html.Div(
                id='buying_cost_summary_container',
                children=[
                    html.H5(id='buying_cost_summary_text'),
                    html.Span(id='buying_cost_summary_tooltip', className='tooltiptext')],
                className='four columns tooltip'),
            html.Div(
                id='operating_cost_summary_container',
                children=[
                    html.H5(id='operating_cost_summary_text'),
                    html.Span(id='operating_cost_summary_tooltip', className='tooltiptext')],
                className='four columns tooltip'),
            html.Div(
                id='maintenance_cost_summary_container',
                children=[
                    html.H5(id='maintenance_cost_summary_text'),
                    html.Span(id='maintenance_cost_summary_tooltip', className='tooltiptext')],
                className='four columns tooltip')],
            className='eight columns')

def make_reliability_summary_container():
    return html.Div(
        id='reliability_summary_container',
        children=[
            html.H5(id='reliability_summary_text'),
            html.Span(id='reliability_summary_tooltip', className='tooltiptext')],
        className='two columns tooltip')

def update_risk_summary_text():
    return 'Risks : 800 Sources'

def update_risk_summary_tooltip():
    return 'Can be lowered to 560'

def update_buying_cost_summary_text():
    return 'Buying : 10 k€'

def update_buying_cost_summary_tooltip():
    return 'Can be lowered to 7 k€'

def update_operating_cost_summary_text():
    return 'Operating : 4 k€/year'

def update_operating_cost_summary_tooltip():
    return 'Can be lowered to 3.5 k€/year'

def update_maintenance_cost_summary_text():
    return 'Maintenance : 2 k€/year'

def update_maintenance_cost_summary_tooltip():
    return 'Can be lowered to 1.5 k€/year'

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