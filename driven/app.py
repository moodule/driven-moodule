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
    'objective-form': {'columnCount': 2}}

#####################################################################
# SPECIFICATIONS FORM
#####################################################################

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
    children=[objective_form],
    id='main-container')

#####################################################################
# CALLBACKS
#####################################################################

#####################################################################
# SERVER
#####################################################################

if __name__ == '__main__':
    app.run_server(debug=True)
