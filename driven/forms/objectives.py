# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#####################################################################
# PRODUCT DATA
#####################################################################
def objectives_form(id='objectives-form', style={}):
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

    return html.Form(
        children=html.Fieldset(
            children=[
                html.P(children=objective_input_sliders, style={'flex': '5 0 auto', 'columnCount': 4, 'height': '100px', 'padding': '10px'}),
                html.P(children=objective_input_labels, style={'flex': '1 0 auto', 'columnCount': 4,'padding': '10px'})]),
        id=id,
        style=style)
