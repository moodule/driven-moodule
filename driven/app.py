# -*- coding: utf-8 -*-
import math
import sqlite3

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# TODO even the row height in the forms
# TODO add spaces between labels and inputs

#####################################################################
# RANDOM DATA
#####################################################################
slope = 0.2
steps = [0.4, 0.2, 1.5, 0.4, -1.0, -3.0, -2.5]
count = [5, 10, 20, 5, 2, 11, 2]
source = [
    [0.35 + 0.01 * i for i in range(100)],
    [0.5 + -5.0 * 1.0e-4 * i ** 2 for i in range(100)]]
target = [
    [31.5 + 0.01 * i for i in range(200)],
    [3.7 - 1.25e-4 * (i ** 2) + 1.923e-3 * i for i in range(200)]]
pulleys = [[-2.0, 31.5, 0.0, 33], [-3.5, 3.2, 0.0, 1.0]]
x_t, y_t = -2.0, -3.0
x_i, y_i = [x_t], [y_t]
x, y = x_t, y_t

for i in range(7):
    side = 0.0 if i < 3 else -1
    
    d_x = (count[i]-1) * steps[i]
    d_y = d_x * slope

    x += d_x
    y += d_y
    
    x_i.append(x)
    y_i.append(y + side)

conveyor_layout_data = [
    [[x_i[i] + j * steps[i] for j in range(count[i])] for i in range(7)],
    [[y_i[i] + j * steps[i] * slope for j in range(count[i])] for i in range(7)]]

conveyor_layout_figures = [
    go.Scatter(
        x=conveyor_layout_data[0][i],
        y=conveyor_layout_data[1][i],
        mode='markers+lines',
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5}
        })
    for i in range(7)] + [
    go.Scatter(
        x=pulleys[0],
        y=pulleys[1],
        mode='markers',
        marker={
            'size': 50,
            'opacity': 0.5}),
    go.Scatter(
        x=source[0],
        y=source[1],
        mode='lines',
        line={
            'width': 0.5}),
    go.Scatter(
        x=target[0],
        y=target[1],
        mode='lines',
        line={
            'width': 0.5})]

navigation_data = [
    go.Bar(
        y=['carry'],
        x=[6],
        name='Tail transition',
        orientation = 'h',
        marker = dict(
            color = 'rgba(246, 78, 139, 0.6)',
            line = dict(
                color = 'rgba(246, 78, 139, 1.0)',
                width = 3))),
    go.Bar(
        y=['carry'],
        x=[2],
        name='Feed',
        orientation = 'h',
        marker = dict(
            color = 'rgba(246, 78, 139, 0.6)',
            line = dict(
                color = 'rgba(246, 78, 139, 1.0)',
                width = 3))),
    go.Bar(
        y=['carry'],
        x=[100],
        name='Section 1',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['carry'],
        x=[10],
        name='Head transition',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['return'],
        x=[20],
        name='Belt return 1',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['return'],
        x=[75],
        name='Section 1',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['return'],
        x=[20],
        name='Belt return 2',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['return'],
        x=[5],
        name='Drive group',
        orientation='h',
        marker=dict(line=dict(width=3))),
    go.Bar(
        y=['return'],
        x=[10],
        name='Takeup',
        orientation='h',
        marker=dict(line=dict(width=3)))]

#####################################################################
# PRODUCT DATA
#####################################################################

with sqlite3.connect('./driven/data/referential.sqlite3') as ref_db:
    cursor = ref_db.cursor()
    product_catalog = {
        product[0]: product[1:]
        for product in cursor.execute(
            """select id, name, average_density, surcharge_angle
            from bulk_material
            order by name;""")}

#####################################################################
# APP
#####################################################################

app = dash.Dash('Industrious')
server = app.server

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

# app_style = {
#     'columnCount': 2}

#####################################################################
# LAYOUTS
#####################################################################

overall_layout = (
    """'spec obj obj obj obj obj'
    'spec obj obj obj obj obj'
    'spec obj obj obj obj obj'
    'spec obj obj obj obj obj'
    'spec obj obj obj obj obj'""")

objective_layout = (
    """'slider slider slider slider slider'
    'slider slider slider slider slider'
    'slider slider slider slider slider'
    'slider slider slider slider slider'
    'slider slider slider slider slider'
    'label label label label label'""")

#####################################################################
# STYLES
#####################################################################

styles = {
    'main-container': {'columnCount': 1, 'backgroundColor': 'rgba(0,0,0,0.0)'},
    'specification-form': {'flex': '1 0 50%', 'width': '50%', 'columnCount': 1, 'backgroundColor': 'rgba(255,0,0,0.0)'},
    'objective-form': {'flex': '1 0 50%', 'width': '50%', 'columnCount': 1, 'backgroundColor': 'rgba(0,255,0,0.0)'},
    'conveyor-layout-graph': {'flex': '1 0 50%', 'width': '50%', 'backgroundColor': 'rgba(0,0,255,0.0)'}}

#####################################################################
# SPECIFICATIONS FORM
#####################################################################

specification_form_rows = [
    [
        html.Label('Delta-x (m)', id='delta-x-label', htmlFor='delta-x-input'),
        dcc.RangeSlider(id='delta-x-input', value=[1.0e1, 1.0e1], min=1.0, step=1.0, max=1.0e3)],
    [
        html.Label('Delta-y (m)', id='delta-y-label', htmlFor='delta-y-input'),
        dcc.RangeSlider(id='delta-y-input', value=[0.0, 0.0], min=-1.0e2, step=0.5, max=1.0e2)],
    [
        html.Label('Output (t/h)', id='output-label', htmlFor='output-input'),
        dcc.RangeSlider(id='output-input', value=[10.0, 10.0], min=0.0, step=1.0, max=1.0e3)],
    [
        html.Label('Product', id='product-name-label', htmlFor='product-name-input'),
        dcc.Dropdown(
            id='product-name-input',
            options=[
                {'label': product[0], 'value': pid}
                for pid, product in product_catalog.items()],
            clearable=False,
            multi=False,
            placeholder='Select a product')],
    [
        html.Label('Bulk Density (t/m³)', id='product-density-label', htmlFor='product-density-input', style={'display': 'none'}),
        dcc.Input(id='product-density-input', type='number', value=0.5, min=1.0e-2, step=1.0e-2, max=1.0e2, style={'display': 'none'})],
    [
        html.Label('Surcharge Angle (°)', id='product-surcharge-angle-label',htmlFor='product-surcharge-angle-input', style={'display': 'none'}),
        dcc.Input(id='product-surcharge-angle-input', type='number', value=20.0, min=0.0, step=1.0, max=90.0, style={'display': 'none'})]]

specification_form = html.Form(
    children=html.Fieldset(
        children=[html.P(children=list(r)) for r in specification_form_rows]),
    id='specification-form',
    style=styles['specification-form'])

#####################################################################
# OBJECTIVE FORM
#####################################################################

objective_labels = [
    'Safety',
    'Cost',
    'Stability',
    'Reliability']

objective_input_labels = [
    html.Label(
        children=l,
        id=l.lower() + '-label',
        htmlFor=l.lower() + '-slider')
    for l in objective_labels]

objective_input_sliders = [
    dcc.Slider(
        id=l.lower() + '-slider',
        min=1,
        max=4,
        marks={j: str(j) for j in range(1, 5)} if i == 3 else {},
        value=1 if i else 4,
        vertical=True)
    for i, l in enumerate(objective_labels)]

objective_form_rows = zip(
    objective_input_sliders,
    objective_input_labels)

objective_form = html.Form(
    children=html.Fieldset(
        children=[
            html.P(children=objective_input_sliders, style={'flex': '5 0 auto', 'columnCount': 4, 'height': '100px'}),
            html.P(children=objective_input_labels, style={'flex': '1 0 auto', 'columnCount': 4})]),
    id='objective-form',
    style=styles['objective-form'])

#####################################################################
# DESIGN FORM
#####################################################################

#####################################################################
# CONVEYOR LAYOUT GRAPH (LINES)
#####################################################################

conveyor_layout_graph = dcc.Graph(
    id='conveyor-layout-graph',
    figure=go.Figure(
        data=conveyor_layout_figures,
        layout=go.Layout(
            title='Conveyor Layout',
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=40, r=40, t=40, b=40)
        )))

navigation_graph = dcc.Graph(
    id='navigation-graph',
    figure=go.Figure(
        data=navigation_data,
        layout=go.Layout(
            title='Navigation',
            barmode='stack',
            showlegend=False,
            margin=go.layout.Margin(l=40, r=40, t=40, b=40)
        )))

#####################################################################
# COST GRAPH
#####################################################################

# buying maintenance stock energy

#####################################################################
# SAFETY GRAPH
#####################################################################

# snatching falling ?

#####################################################################
# RELIABILITY GRAPH
#####################################################################

# rmbt : min, max, average

#####################################################################
# STABILITY GRAPH
#####################################################################

# spilling lifting

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=[
        html.Div(
            children=[specification_form, objective_form],
            style={'display': 'flex', 'columnCount': 2}),
        html.Div(
            children=[conveyor_layout_graph, navigation_graph],
            style={'display': 'flex', 'columnCount': 2})],
    id='main-container',
    style=styles['main-container'])

#####################################################################
# CALLBACKS
#####################################################################

def display_value_in_label(value_range, label_text):
    if value_range[0] == value_range[1]:
        return '{} : {}'.format(label_text, value_range[0])
    else:
        return '{} : [{} ; {}]'.format(label_text, value_range[0], value_range[1])

@app.callback(
    dash.dependencies.Output('delta-x-label', 'children'),
    [dash.dependencies.Input('delta-x-input', 'value')])
def update_delta_x_label(x_range):
    return display_value_in_label(x_range, 'Delta-x (m)')

@app.callback(
    dash.dependencies.Output('delta-y-label', 'children'),
    [dash.dependencies.Input('delta-y-input', 'value')])
def update_delta_y_label(y_range):
    return display_value_in_label(y_range, 'Delta-y (m)')

@app.callback(
    dash.dependencies.Output('output-label', 'children'),
    [dash.dependencies.Input('output-input', 'value')])
def update_output_label(output_range):
    return display_value_in_label(output_range, 'Output (t/h)')

@app.callback(
    dash.dependencies.Output('product-density-input', 'value'),
    [dash.dependencies.Input('product-name-input', 'value')])
def update_density_input(product_id):
    product = product_catalog.get(product_id, [])
    if product:
        return 0.001 * product[1]

@app.callback(
    dash.dependencies.Output('product-surcharge-angle-input', 'value'),
    [dash.dependencies.Input('product-name-input', 'value')])
def update_surcharge_angle_input(product_id):
    product = product_catalog.get(product_id, [])
    if product:
        return 180.0 * product[2] / math.pi

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
