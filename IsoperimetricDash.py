import dash
from dash.dependencies import Output, State, Input
import dash_core_components as dcc
import dash_html_components as html

from Isoperimetric import Isoperimetric, t, x, x_diff

# ToDo * is bad
from sympy.functions import *
from sympy import pi


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Markdown('''# The Isoperimetric Problem'''),

    html.Div([html.Label('Enter f0'),
              dcc.Input(id='f0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter t0'),
              dcc.Input(id='t0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter t1'),
              dcc.Input(id='t1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x0'),
              dcc.Input(id='x0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x1'),
              dcc.Input(id='x1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    # ToDo Нужен выпадающий список
    html.Div([html.Label('Enter f_list if necessary'),
              dcc.Input(id='f_list',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    # ToDo Нужен выпадающий список
    html.Div([html.Label('Enter alphas if necessary'),
              dcc.Input(id='alphas',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div(id='my_input')])


@app.callback(Output('my_input', 'children'),
              [Input('f0', 'value'),
               Input('t0', 'value'),
               Input('t1', 'value'),
               Input('x0', 'value'),
               Input('x1', 'value'),
               Input('f_list', 'value'),
               Input('alphas', 'value')])
def update_output(f0, t0, t1, x0, x1, f_list, alphas):
    if (f0 is not None) & \
            (t0 is not None) & \
            (t1 is not None) & \
            (x0 is not None) & \
            (x1 is not None):

        solver = Isoperimetric(f0=eval(f0),
                               t0=int(t0),
                               t1=int(t1),
                               x0=int(x0),
                               x1=int(x1),
                               f_list=eval(f_list),
                               alphas=eval(alphas))
        try:
            solver.solve()
        except:
            to_return = 'Something went wrong :('
        else:
            to_return = html.Div([ dcc.Markdown('### ANSWER'),
                                   dcc.Markdown(f'General solution: {solver.general_solution}'),
                                   dcc.Markdown(f'Coefficients: {solver.coefficients}'),
                                   dcc.Markdown(f'Particular solution: {solver.particular_solution}'),
                                   dcc.Markdown(f'Extreme value: {solver.extreme_value}')],
                                 style={'columnCount': 3})

        return to_return


if __name__ == '__main__':
    app.run_server(port=8060)
