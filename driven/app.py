# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# APP
#####################################################################

app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

# app_style = {
#     'columnCount': 2}

#####################################################################
# ELEMENTS
#####################################################################

objective_labels = [
    'Safety',
    'Cost',
    'Stability',
    'Reliability',
    'Robustness']
objective_elements = [(
        html.Label(l),
        dcc.Slider(
            id=l.lower() + '-slider',
            min=1,
            max=5,
            marks={i: str(i) for i in range(1, 6)} if j == 4 else {},
            value=5-j))
    for j, l in enumerate(objective_labels)]

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=(
        [e[0] for e in objective_elements]
        + [e[1] for e in objective_elements]))

if __name__ == '__main__':
    app.run_server(debug=True)

# [
#     html.Label('Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Multi-Select Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value=['MTL', 'SF'],
#         multi=True
#     ),

#     html.Label('Radio Items'),
#     dcc.RadioItems(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Checkboxes'),
#     dcc.Checklist(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         values=['MTL', 'SF']
#     ),

#     html.Label('Text Input'),
#     dcc.Input(value='MTL', type='text'),

#     html.Label('Slider'),
#     dcc.Slider(
#         min=0,
#         max=9,
#         marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
#         value=5,
#     )]