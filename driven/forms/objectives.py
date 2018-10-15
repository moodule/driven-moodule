# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# PRODUCT DATA
#####################################################################

def make_objectives_form(id='objectives-form', style={}):
    objective_labels = [
        'Safety',
        'Cost',
        'Stability',
        'Reliability']

    objective_input_labels = [
        html.Label(
            children=l,
            id=l.lower() + '-label',
            htmlFor=l.lower() + '-slider',
            style={'flex': '1 1 auto'})
        for l in objective_labels]

    objective_input_sliders = [
        html.Div(
            id=l.lower() + '-slider-div',
            style={'flex': '1 1 auto', 'padding': '10px'},
            children=[dcc.Slider(
                id=l.lower() + '-slider',
                min=1,
                max=4,
                marks={j: str(j) for j in range(1, 5)} if i == 3 else {},
                value=1 if i else 4,
                vertical=True)])
        for i, l in enumerate(objective_labels)]

    return html.Form(
        children=html.Fieldset(
            children=[
                html.Div(children=objective_input_sliders, style={'display': 'flex', 'flex': '5 5 auto', 'columnCount': 4, 'height': '100px'}),
                html.Div(children=objective_input_labels, style={'display': 'flex', 'flex': '1 1 auto', 'columnCount': 4})]),
        id=id,
        style=style)
