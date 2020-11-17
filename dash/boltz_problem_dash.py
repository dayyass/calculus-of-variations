import sys
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html

# TODO: fix it
sys.path.append('./')
from calculus_of_variations.boltz_problem import BoltzSolver


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''# Boltz problem dash'''),
    html.Div([html.Label('Enter L'), dcc.Input(id='L')]), html.H4(''),
    html.Div([html.Label('Enter l'), dcc.Input(id='l')]), html.H4(''),
    html.Div([html.Label('Enter t0'), dcc.Input(id='t0')]), html.H4(''),
    html.Div([html.Label('Enter t1'), dcc.Input(id='t1')]), html.H4(''),
    html.Div(id='my_input'),
])


@app.callback(
    Output('my_input', 'children'),
    [Input('L', 'value'), Input('l', 'value'), Input('t0', 'value'), Input('t1', 'value')],
)
def update_output(L, l, t0, t1):
    if (L is not None) & (l is not None) & (t0 is not None) & (t1 is not None):

        solver = BoltzSolver(L=L, l=l, t0=float(t0), t1=float(t1))
        try:
            solver.solve()
        except:
            to_return = 'Something went wrong :('
        else:
            to_return = html.Div(
                [
                    dcc.Markdown('### ANSWER'),
                    dcc.Markdown(f'General solution: {solver.general_solution}'),
                    dcc.Markdown(f'Coefficients: {solver.coefficients}'),
                    dcc.Markdown(f'Particular solution: {solver.particular_solution}'),
                    dcc.Markdown(f'Extrema value: {solver.extrema_value}'),
                ],
                style={'columnCount': 3},
            )

        return to_return


if __name__ == '__main__':
    app.run_server(port=8060)
