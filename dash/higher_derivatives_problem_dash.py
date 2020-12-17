import sys

import dash_core_components as dcc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.higher_derivatives_problem import HigherDerivativesSolver

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("""# Higher derivatives problem dash"""),
        html.Div([html.Label("Enter n"), dcc.Input(id="n")]),
        html.H4(""),
        html.Div([html.Label("Enter L"), dcc.Input(id="L")]),
        html.H4(""),
        html.Div([html.Label("Enter t0"), dcc.Input(id="t0")]),
        html.H4(""),
        html.Div([html.Label("Enter t1"), dcc.Input(id="t1")]),
        html.H4(""),
        html.Div([html.Label("Enter x0"), dcc.Input(id="x0")]),
        html.H4(""),
        html.Div([html.Label("Enter x1"), dcc.Input(id="x1")]),
        html.H4(""),
        html.Div([html.Label("Enter x0_array"), dcc.Input(id="x0_array")]),
        html.H4(""),
        html.Div([html.Label("Enter x1_array"), dcc.Input(id="x1_array")]),
        html.H4(""),
        html.Div(id="my_input"),
    ]
)


@app.callback(
    Output("my_input", "children"),
    [
        Input("n", "value"),
        Input("L", "value"),
        Input("t0", "value"),
        Input("t1", "value"),
        Input("x0", "value"),
        Input("x1", "value"),
        Input("x0_array", "value"),
        Input("x1_array", "value"),
    ],
)
def update_output(n, L, t0, t1, x0, x1, x0_array, x1_array):
    if (
        (n is not None)
        & (L is not None)
        & (t0 is not None)
        & (t1 is not None)
        & (x0 is not None)
        & (x1 is not None)
        & (x0_array is not None)
        & (x1_array is not None)
    ):

        solver = HigherDerivativesSolver(
            n=int(n),
            L=L,
            t0=float(t0),
            t1=float(t1),
            x0=float(x0),
            x1=float(x1),
            x0_array=[float(x0) for x0 in x0_array.split()],
            x1_array=[float(x1) for x1 in x1_array.split()],
        )
        try:
            solver.solve()
        except:
            to_return = "Something went wrong :("
        else:
            to_return = html.Div(
                [
                    dcc.Markdown("### ANSWER"),
                    dcc.Markdown(f"General solution: {solver.general_solution}"),
                    dcc.Markdown(f"Coefficients: {solver.coefficients}"),
                    dcc.Markdown(f"Particular solution: {solver.particular_solution}"),
                    dcc.Markdown(f"Extrema value: {solver.extrema_value}"),
                ],
                style={"columnCount": 3},
            )

        return to_return


if __name__ == "__main__":
    app.run_server(port=8060)
