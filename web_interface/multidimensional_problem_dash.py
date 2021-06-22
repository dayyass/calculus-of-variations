import sys

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from dash import Dash

# TODO: fix it
sys.path.append("./")
from calculus_of_variations import MultidimensionalSolver
from web_interface.utils import (
    dash_multidimensional_answer,
    dash_multidimensional_problem,
    get_argparse,
)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("# Multidimensional problem"),
        dcc.Markdown("### Input"),
        html.Div(
            [
                dcc.Markdown("Enter **L**:"),
                dcc.Input(id="L", value="x1_diff ** 2 + x2_diff ** 2", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **t0**:"), dcc.Input(id="t0", value="0", type="text")]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **t1**:"), dcc.Input(id="t1", value="1", type="text")]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x1_0**:"),
                dcc.Input(id="x1_0", value="0", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x1_1**:"),
                dcc.Input(id="x1_1", value="1", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x2_0**:"),
                dcc.Input(id="x2_0", value="0", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x2_1**:"),
                dcc.Input(id="x2_1", value="1", type="text"),
            ]
        ),
        html.Br(),
        html.Button("solve", id="solve"),
        html.Br(),
        html.Div(id="input"),
    ]
)


@app.callback(
    Output(component_id="input", component_property="children"),
    [Input("solve", "n_clicks")],
    [
        State("L", "value"),
        State("t0", "value"),
        State("t1", "value"),
        State("x1_0", "value"),
        State("x1_1", "value"),
        State("x2_0", "value"),
        State("x2_1", "value"),
    ],
)
def update_output(
    n_clicks, L: str, t0: str, t1: str, x1_0: str, x1_1: str, x2_0: str, x2_1: str
):

    # click "solve"
    if n_clicks is None:
        return

    try:
        solver = MultidimensionalSolver(
            L=L, t0=t0, t1=t1, x1_0=x1_0, x1_1=x1_1, x2_0=x2_0, x2_1=x2_1
        )
        solver.solve()

    except:
        to_return = html.Div(dcc.Markdown("### Something went wrong :("))

    else:
        to_return = html.Div(
            [
                dcc.Markdown("### Problem"),
                dash_multidimensional_problem(solver=solver),
                dcc.Markdown("### Answer"),
                dash_multidimensional_answer(solver=solver),
            ]
        )

    return to_return


if __name__ == "__main__":

    # argparse
    parser = get_argparse()
    args = parser.parse_args()

    # run server
    app.run_server(host=args.host, port=args.port, debug=args.debug)
