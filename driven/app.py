# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# TODO even the row height in the forms
# TODO add spaces between labels and inputs

#####################################################################
# APP
#####################################################################

app = dash.Dash('Industrious')

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

# app_style = {
#     'columnCount': 2}

#####################################################################
# STYLES
#####################################################################

styles = {
    'main-container': {'columnCount': 2},
    'specifications-form': {},
    'objective-form': {},
    'product-density-input': {'display': 'none'},
    'product-surcharge-angle-input': {'display': 'none'}}

#####################################################################
# SPECIFICATIONS FORM
#####################################################################

specification_form_rows = [
    [
        html.Label('Delta-x (m)', id='delta-x-label', htmlFor='delta-x-input'),
        dcc.RangeSlider(id='delta-x-input', value=[1.0e1, 1.0e1], min=1.0, step=1.0, max=1.0e5)],
    [
        html.Label('Delta-y (m)', htmlFor='delta-y-input'),
        dcc.Input(id='delta-y-input', type='number', value=0.0, min=-1.0e3, step=0.1, max=1.0e3)],
    [
        html.Label('Output (t/h)', htmlFor='output'),
        dcc.Input(id='output', type='number', value=10.0, min=0.1, step=0.1, max=1.0e4)],
    [
        html.Label('Product', htmlFor='product-name'),
        dcc.Dropdown(
            id='product-name',
            options=[
                {'label':'Coal', 'value':'coal'},
                {'label':'Truc', 'value':'truc'}],
            value='coal',
            multi=False)],
    [
        html.Label('Bulk Density (t/m³)', htmlFor='product-density-input', style={'display': 'none'}),
        dcc.Input(id='product-density-input', type='number', value=0.5, min=1.0e-2, step=1.0e-2, max=1.0e2, style={'display': 'none'})],
    [
        html.Label('Surcharge Angle (°)', htmlFor='product-density-input', style={'display': 'none'}),
        dcc.Input(id='product-surcharge-angle-input', type='number', value=20.0, min=0.0, step=1.0, max=90.0, style={'display': 'none'})]]

specification_form = html.Form(
    children=(
        [html.Legend('Specifications')]
        + [html.P(children=list(r)) for r in specification_form_rows]),
    id='specification-form')

#####################################################################
# OBJECTIVE FORM
#####################################################################

objective_labels = [
    'Safety',
    'Cost',
    'Stability',
    'Reliability',
    'Robustness']

objective_input_labels = [
    html.Label(
        children=l,
        htmlFor=l.lower() + '-slider')
    for l in objective_labels]

objective_input_sliders = [
    dcc.Slider(
        id=l.lower() + '-slider',
        min=1,
        max=5,
        marks={j: str(j) for j in range(1, 6)} if i == 4 else {},
        value=1 if i else 5)
    for i, l in enumerate(objective_labels)]

objective_form_rows = zip(
    objective_input_labels,
    objective_input_sliders)

objective_form = html.Form(
    children=(
        [html.Legend('Objectives')]
        + [html.P(children=list(r)) for r in objective_form_rows]),
    id='objective-form')

#####################################################################
# DESIGN FORM
#####################################################################

#####################################################################
# CONVEYOR LAYOUT GRAPH (LINES)
#####################################################################

#####################################################################
# COST GRAPH
#####################################################################

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=[specification_form, objective_form],
    id='main-container',
    style=styles['main-container'])

#####################################################################
# CALLBACKS
#####################################################################

@app.callback(
    dash.dependencies.Output('delta-x-label', 'children'),
    [dash.dependencies.Input('delta-x-input', 'value')])
def set_cities_options(x_range):
    if x_range[0] == x_range[1]:
        return 'Delta-x (m) : {}'.format(x_range[0])
    else:
        return 'Delta-x (m) : [{} ; {}]'.format(x_range[0], x_range[1])

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
