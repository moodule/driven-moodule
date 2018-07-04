# -*- coding: utf-8 -*-
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
pulleys = [[-2.0, 31.5], [-3.5, 3.2]]
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
            'opacity': 0.5})]

#####################################################################
# APP
#####################################################################

app = dash.Dash('Industrious')

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
    'main-container': {'flex': 'auto', 'columnCount': 1},
    'specification-form': {'flex': 1, 'columnCount': 1},
    'objective-form': {'flex': 1, 'columnCount': 5},
    'conveyor-layout-graph': {'flex': 1}}

#####################################################################
# SPECIFICATIONS FORM
#####################################################################

specification_form_rows = [
    [
        html.Label('Delta-x (m)', id='delta-x-label', htmlFor='delta-x-input'),
        dcc.RangeSlider(id='delta-x-input', value=[1.0e1, 1.0e1], min=1.0, step=1.0, max=1.0e3)],
    [
        html.Label('Delta-y (m)', id='delta-y-label', htmlFor='delta-y-input'),
        dcc.RangeSlider(id='delta-y-input', value=[0.0, 0.0], min=-1.0e2, step=0.1, max=1.0e2)],
    [
        html.Label('Output (t/h)', id='output-label', htmlFor='output-input'),
        dcc.RangeSlider(id='output-input', value=[10.0, 10.0], min=0.0, step=0.1, max=1.0e3)],
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
        value=1 if i else 5,
        vertical=True)
    for i, l in enumerate(objective_labels)]

objective_form_rows = zip(
    objective_input_sliders,
    objective_input_labels)

objective_form = html.Form(
    children=html.Fieldset(
        children=[
            html.P(children=objective_input_sliders, style=styles['objective-form']),
            html.P(children=objective_input_labels, style=styles['objective-form'])]),
    id='objective-form')

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
            legend=go.Legend(
                x=0,
                y=1.0
            ),
            margin=go.Margin(l=40, r=40, t=40, b=40)
        )))

#####################################################################
# COST GRAPH
#####################################################################

#####################################################################
# LAYOUT
#####################################################################

app.layout = html.Div(
    children=[specification_form, objective_form, conveyor_layout_graph],
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
