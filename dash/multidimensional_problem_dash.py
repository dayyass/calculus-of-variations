import sys

import dash_core_components as dcc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.multidimensional_problem import MultidimensionalSolver

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("""# Multidimensional problem dash"""),
        html.Div([html.Label("Enter L"), dcc.Input(id="L")]),
        html.H4(""),
        html.Div([html.Label("Enter t0"), dcc.Input(id="t0")]),
        html.H4(""),
        html.Div([html.Label("Enter t1"), dcc.Input(id="t1")]),
        html.H4(""),
        html.Div([html.Label("Enter x1_0"), dcc.Input(id="x1_0")]),
        html.H4(""),
        html.Div([html.Label("Enter x1_1"), dcc.Input(id="x1_1")]),
        html.H4(""),
        html.Div([html.Label("Enter x2_0"), dcc.Input(id="x2_0")]),
        html.H4(""),
        html.Div([html.Label("Enter x2_1"), dcc.Input(id="x2_1")]),
        html.H4(""),
        html.Div(id="my_input"),
    ]
)


@app.callback(
    Output("my_input", "children"),
    [
        Input("L", "value"),
        Input("t0", "value"),
        Input("t1", "value"),
        Input("x1_0", "value"),
        Input("x1_1", "value"),
        Input("x2_0", "value"),
        Input("x2_1", "value"),
    ],
)
def update_output(L, t0, t1, x1_0, x1_1, x2_0, x2_1):
    if (
        (L is not None)
        & (t0 is not None)
        & (t1 is not None)
        & (x1_0 is not None)
        & (x1_1 is not None)
        & (x2_0 is not None)
        & (x2_1 is not None)
    ):

        solver = MultidimensionalSolver(
            L=L,
            t0=float(t0),
            t1=float(t1),
            x1_0=float(x1_0),
            x1_1=float(x1_1),
            x2_0=float(x2_0),
            x2_1=float(x2_1),
        )
        try:
            solver.solve()
        except:
            to_return = "Something went wrong :("
        else:
            to_return = html.Div(
                [
                    dcc.Markdown("### ANSWER"),
                    dcc.Markdown(f"General solution 1: {solver.general_solution_1}"),
                    dcc.Markdown(f"General solution 2: {solver.general_solution_2}"),
                    dcc.Markdown(
                        f"Particular solution 1: {solver.particular_solution_1}"
                    ),
                    dcc.Markdown(
                        f"Particular solution 2: {solver.particular_solution_2}"
                    ),
                    dcc.Markdown(f"Coefficients: {solver.coefficients}"),
                    dcc.Markdown(f"Extrema value: {solver.extrema_value}"),
                ],
                style={"columnCount": 4},
            )

        return to_return


if __name__ == "__main__":
    app.run_server(port=8060)
