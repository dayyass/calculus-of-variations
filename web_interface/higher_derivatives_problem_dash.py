import sys

import dash_core_components as dcc
import dash_html_components as html

from dash import Dash
from dash.dependencies import Input, Output, State

# TODO: fix it
sys.path.append("./")
from calculus_of_variations import HigherDerivativesSolver
from web_interface.utils import (
    dash_answer,
    dash_higher_derivatives_problem,
    get_argparse,
)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("# Higher derivatives problem"),
        dcc.Markdown("### Input"),
        html.Div(
            [
                dcc.Markdown("Enter **n**:"),
                dcc.Input(id="n", value="2", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **L**:"),
                dcc.Input(id="L", value="x_diff_2 ** 2", type="text"),
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
            [dcc.Markdown("Enter **x0**:"), dcc.Input(id="x0", value="0", type="text")]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **x1**:"), dcc.Input(id="x1", value="1", type="text")]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x0_array**:"),
                dcc.Input(id="x0_array", value="0", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **x1_array**:"),
                dcc.Input(id="x1_array", value="1", type="text"),
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
        State("n", "value"),
        State("L", "value"),
        State("t0", "value"),
        State("t1", "value"),
        State("x0", "value"),
        State("x1", "value"),
        State("x0_array", "value"),
        State("x1_array", "value"),
    ],
)
def update_output(
    n_clicks,
    n: str,
    L: str,
    t0: str,
    t1: str,
    x0: str,
    x1: str,
    x0_array: str,
    x1_array: str,
):

    # click "solve"
    if n_clicks is None:
        return

    try:
        solver = HigherDerivativesSolver(
            n=n,
            L=L,
            t0=t0,
            t1=t1,
            x0=x0,
            x1=x1,
            x0_array=x0_array,
            x1_array=x1_array,
        )
        solver.solve()

    except:
        to_return = html.Div(dcc.Markdown("### Something went wrong :("))

    else:
        to_return = html.Div(
            [
                dcc.Markdown("### Problem"),
                dash_higher_derivatives_problem(solver=solver),
                dcc.Markdown("### Answer"),
                dash_answer(solver=solver),
            ]
        )

    return to_return


if __name__ == "__main__":

    # argparse
    parser = get_argparse()
    args = parser.parse_args()

    # run server
    app.run_server(host=args.host, port=args.port, debug=args.debug)
