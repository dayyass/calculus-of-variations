import dash
from dash.dependencies import Output, State, Input
import dash_core_components as dcc
import dash_html_components as html

from Multidimensional import Multidimensional, t, x1, x1_diff, x2, x2_diff

# ToDo * is bad
from sympy.functions import *
from sympy import pi


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Markdown('''# The Multidimensional Problem'''),

    html.Div([html.Label('Enter L'),
              dcc.Input(id='L',
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

    html.Div([html.Label('Enter x1_0'),
              dcc.Input(id='x1_0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x1_1'),
              dcc.Input(id='x1_1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x2_0'),
              dcc.Input(id='x2_0',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div([html.Label('Enter x2_1'),
              dcc.Input(id='x2_1',
                        type='text',
                        placeholder='type something',
                        value='')]), html.H4(''),

    html.Div(id='my_input')])


@app.callback(Output('my_input', 'children'),
              [Input('L', 'value'),
               Input('t0', 'value'),
               Input('t1', 'value'),
               Input('x1_0', 'value'),
               Input('x1_1', 'value'),
               Input('x2_0', 'value'),
               Input('x2_1', 'value')])
def update_output(L, t0, t1, x1_0, x1_1, x2_0, x2_1):
    if (L is not None) & \
            (t0 is not None) & \
            (t1 is not None) & \
            (x1_0 is not None) & \
            (x1_1 is not None) & \
            (x2_0 is not None) & \
            (x2_1 is not None):

        solver = Multidimensional(L=eval(L),
                                  t0=eval(t0),
                                  t1=eval(t1),
                                  x1_0=eval(x1_0),
                                  x1_1=eval(x1_1),
                                  x2_0=eval(x2_0),
                                  x2_1=eval(x2_1))
        try:
            solver.solve()
        except:
            to_return = 'Something went wrong :('
        else:
            to_return = html.Div([ dcc.Markdown('### ANSWER'),
                                   dcc.Markdown(f'General solution 1: {solver.general_solution_1}'),
                                   dcc.Markdown(f'General solution 2: {solver.general_solution_2}'),
                                   dcc.Markdown(f'Particular solution 1: {solver.particular_solution_1}'),
                                   dcc.Markdown(f'Particular solution 2: {solver.particular_solution_2}'),
                                   dcc.Markdown(f'Coefficients: {solver.coefficients}'),
                                   dcc.Markdown(f'Extreme value: {solver.extreme_value}')],
                                 style={'columnCount': 4})

        return to_return


if __name__ == '__main__':
    app.run_server(port=8060)
