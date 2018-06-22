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
        html.Label('Delta-x', htmlFor='delta-x-input'),
        dcc.Input(id='delta-x-input', value=1.0, min=0.1, step=0.1, max=1.0e5),
        html.Abbr('m')],
    [
        html.Label('Delta-y', htmlFor='delta-y-input'),
        dcc.Input(id='delta-y-input', value=0.0, min=-1.0e3, step=0.1, max=1.0e3),
        html.Abbr('m')],
    [
        html.Label('Output', htmlFor='output'),
        dcc.Input(id='output', value=10.0, min=0.1, step=0.1, max=1.0e4),
        html.Abbr('t/h')],
    [
        html.Label('Product', htmlFor='product-name'),
        dcc.Dropdown(
            id='product-name',
            options=[
                {'label':'Coal', 'value':'coal'},
                {'label':'Truc', 'value':'truc'}],
            value='coal',
            multi=False)]]

specification_form = html.Form(
    children=html.Fieldset(
        children=(
            [html.Legend('Specifications')]
            + [html.P(children=list(r)) for r in specification_form_rows])),
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
    children=html.Fieldset(
        children=(
            [html.Legend('Objectives')]
            + [html.P(children=list(r)) for r in objective_form_rows])),
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

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
