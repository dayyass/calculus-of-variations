import argparse
import sys

import dash_core_components as dcc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.simplest_problem import SimplestProblemSolver

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("""### Simplest problem dash"""),
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
        html.Div(id="my_input"),
    ]
)


@app.callback(
    Output("my_input", "children"),
    [
        Input("L", "value"),
        Input("t0", "value"),
        Input("t1", "value"),
        Input("x0", "value"),
        Input("x1", "value"),
    ],
)
def update_output(L, t0, t1, x0, x1):
    if (
        (L is not None)
        & (t0 is not None)
        & (t1 is not None)
        & (x0 is not None)
        & (x1 is not None)
    ):

        solver = SimplestProblemSolver(
            L=L, t0=float(t0), t1=float(t1), x0=float(x0), x1=float(x1)
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

    # argparse
    parser = argparse.ArgumentParser(description="Server configuration")
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        type=str,
        required=False,
        help="Host IP used to serve the application",
    )
    parser.add_argument(
        "--port",
        default=8050,
        type=int,
        required=False,
        help="Port used to serve the application",
    )
    parser.add_argument(
        "--debug",
        default=False,
        type=bool,
        required=False,
        help="Set Flask debug mode and enable dev tools",
    )
    args = parser.parse_args()

    # run server
    app.run_server(host=args.host, port=args.port, debug=args.debug)
