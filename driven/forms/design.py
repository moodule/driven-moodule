# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# LOCAL DESIGN
#####################################################################

def _local_design_geometry_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Delta-x',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='section_delta_x_input',
                            allowCross=False,
                            min=0.0,
                            step=0.5,
                            max=1.0e3,
                            marks={
                                0:"0 m",
                                1000:"1000 m"},
                            value=[0.0, 1.0e3]),
                        className='eight columns')],
                className='row'),
            html.Div(
                children=[
                    html.Label(
                        'Delta-y',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='section-delta-y-input',
                            allowCross=False,
                            min=-1.0e2,
                            step=0.5,
                            max=1.0e2,
                            marks={
                                -100:'-100 m',
                                100:'100 m'},
                            value=[0.0, 0.0]),
                        className='eight columns')],
                className='row')],
        className='four columns')

def _local_design_support_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Support step',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='support-step-input',
                            allowCross=False,
                            min=0.0,
                            step=1.0e-1,
                            max=1.0e1,
                            marks={
                                0:"0 m",
                                10:'10 m'},
                            value=[1.0, 3.0]),
                        className='eight columns')],
                className='row'),
            html.Div(
                children=[
                    html.Label(
                        'Support sector length',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='support-sector-length-input',
                            allowCross=False,
                            min=0.1,
                            step=1.0e-2,
                            max=1.0,
                            marks={
                                0.1:'0.1 m',
                                1:'1 m'},
                            value=[0.38, 0.38]),
                        className='eight columns')],
                className='row'),
            html.Div(
                children=[
                    html.Label(
                        'Support sector width',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='support-sector-width-input',
                            allowCross=False,
                            min=0.02,
                            step=1.0e-2,
                            max=1.0,
                            marks={
                                0.02:'0.02 m',
                                1:'1 m'},
                            value=[0.1, 0.1]),
                        className='eight columns')],
                className='row'),
            html.Div(
                children=[
                    html.Label(
                        'Support troughing angle',
                        className='four columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='support-troughing-angle-input',
                            allowCross=False,
                            min=0.0,
                            step=5.0,
                            max=90.0,
                            marks={
                                0:'0°',
                                90:'90°'},
                            value=[10.0, 45.0]),
                        className='eight columns')],
                className='row')],
        className='four columns')

def make_local_design_form():
    return html.Div(
        id='local_design_form',
        children=[
            _local_design_geometry_form(),
            _local_design_support_form()],
        className='row')

#####################################################################
# GLOBAL DESIGN
#####################################################################

def make_global_design_geometry_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Tail x',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='tail_x_input',
                            allowCross=False,
                            min=-1.0e4,
                            step=1.0,
                            max=1.0e4,
                            marks={
                                -10000:"-10 km",
                                10000:"10 km"},
                            value=[-1.0e4, 1.0e4]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Tail y',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='tail_y_input',
                            allowCross=False,
                            min=-1.0e2,
                            step=1.0,
                            max=1.0e2,
                            marks={
                                -100:"-100 m",
                                100:"100 m"},
                            value=[-1.0e2, 1.0e2]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Head x',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='head_x_input',
                            allowCross=False,
                            min=-1.0e4,
                            step=1.0,
                            max=1.0e4,
                            marks={
                                -10000:"-10 km",
                                10000:"10 km"},
                            value=[-1.0e4, 1.0e4]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Head y',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='head_y_input',
                            allowCross=False,
                            min=-1.0e2,
                            step=1.0,
                            max=1.0e2,
                            marks={
                                -100:"-100 m",
                                100:"100 m"},
                            value=[-100.0, -100.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                className='four rows')],
        className='four columns',
        style={
            'height':'400px',
            # 'background-color':'#020202',
            'color':'#fff'})

def make_global_design_components_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Belt speed',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='belt_speed_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=10.0,
                            marks={
                                0:"0",
                                10:"10 m/s"},
                            value=[0.0, 10.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Belt width',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='belt_width_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=10.0,
                            marks={
                                0:"0",
                                10:"10 m"},
                            value=[0.0, 10.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Belt strength',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='belt_strength_input',
                            allowCross=False,
                            min=0.0,
                            step=100.0,
                            max=5.0e3,
                            marks={
                                0:"0",
                                5000:"5000 N/mm"},
                            value=[0.0, 5000.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Splice strength',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='splice_strength_ratio_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=100.0,
                            marks={
                                0:"0",
                                100:"100 %"},
                            value=[0.0, 100.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Pulley radius (A)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='pulley_a_external_radius_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=3.0,
                            marks={
                                0:"0",
                                3:"3 m"},
                            value=[0.0, 3.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Pulley radius (B)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='pulley_b_external_radius_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=3.0,
                            marks={
                                0:"0",
                                3:"3 m"},
                            value=[0.0, 3.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Pulley radius (C)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='pulley_c_external_radius_input',
                            allowCross=False,
                            min=0.0,
                            step=0.1,
                            max=3.0,
                            marks={
                                0:"0",
                                3:"3 m"},
                            value=[0.0, 3.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A', 'display':'hidden'}),
            html.Div(
                className='five rows',
                style={'display':'hidden'})],
        className='four columns',
        style={
            'height':'400px',
            # 'background-color':'#020202',
            'color':'#fff'})

def make_global_design_systems_form():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label(
                        'Drive power (1)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='drive_power_1_input',
                            allowCross=False,
                            min=0.0,
                            step=1.0,
                            max=1000.0,
                            marks={
                                0:"0",
                                1000:"1000 kW"},
                            value=[0.0, 1000.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Drive power (2)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='drive_power_2_input',
                            allowCross=False,
                            min=0.0,
                            step=1.0,
                            max=1000.0,
                            marks={
                                0:"0",
                                1000:"1000 kW"},
                            value=[0.0, 1000.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Wrap angle (1)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='drive_wrap_angle_1_input',
                            allowCross=False,
                            min=0.0,
                            step=1.0,
                            max=360.0,
                            marks={
                                0:"0",
                                360:"360 °"},
                            value=[0.0, 360.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Wrap angle (2)',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='drive_wrap_angle_2_input',
                            allowCross=False,
                            min=0.0,
                            step=1.0,
                            max=360.0,
                            marks={
                                0:"0",
                                360:"360 °"},
                            value=[0.0, 360.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Engine efficiency',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='drive_engine_efficiency_input',
                            allowCross=False,
                            min=0.0,
                            step=5,
                            max=100.0,
                            marks={
                                0:"0",
                                100:"100 %"},
                            value=[0.0, 100.0]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                children=[
                    html.Label(
                        'Takeup tension',
                        className='five columns',
                        style={'text-align':'right', 'padding':'10px'}),
                    html.Div(
                        children=dcc.RangeSlider(
                            id='takeup_tension_input',
                            allowCross=False,
                            min=0.0,
                            step=100.0,
                            max=1.0e6,
                            marks={
                                0:"0",
                                1000000:"1000 kN"},
                            value=[0.0, 1.0e6]),
                        className='six columns')],
                className='two rows',
                style={'background-color':'#191A1A'}),
            html.Div(
                className='six rows',
                style={'display':'hidden'})],
        className='four columns',
        style={
            'height':'400px',
            # 'background-color':'#020202',
            'color':'#fff'})
