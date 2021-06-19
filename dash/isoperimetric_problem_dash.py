import sys
from argparse import ArgumentParser

import dash_core_components as dcc
import dash_html_components as html
from utils import dash_answer, dash_isoperimetric_problem

import dash
from dash.dependencies import Input, Output, State

# TODO: fix it
sys.path.append("./")
from calculus_of_variations import IsoperimetricProblemSolver

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("""# Isoperimetric problem"""),
        dcc.Markdown("""### Input"""),
        html.Div(
            [
                dcc.Markdown("Enter **f0**:"),
                dcc.Input(id="f0", value="x_diff ** 2", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **t0**:"), dcc.Input(id="t0", value=0, type="number")]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **t1**:"), dcc.Input(id="t1", value=1, type="number")]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **x0**:"), dcc.Input(id="x0", value=0, type="number")]
        ),
        html.Br(),
        html.Div(
            [dcc.Markdown("Enter **x1**:"), dcc.Input(id="x1", value=1, type="number")]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **f_list**:"),
                dcc.Input(id="f_list", value="x", type="text"),
            ]
        ),
        html.Br(),
        html.Div(
            [
                dcc.Markdown("Enter **alpha_list**:"),
                dcc.Input(id="alpha_list", value="0", type="text"),
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
        State("f0", "value"),
        State("t0", "value"),
        State("t1", "value"),
        State("x0", "value"),
        State("x1", "value"),
        State("f_list", "value"),
        State("alpha_list", "value"),
    ],
)
def update_output(n_clicks, f0, t0, t1, x0, x1, f_list, alpha_list):

    # click "solve"
    if n_clicks is None:
        return

    try:
        solver = IsoperimetricProblemSolver(
            f0=f0,
            t0=t0,
            t1=t1,
            x0=x0,
            x1=x1,
            f_list=f_list.split(","),
            alpha_list=alpha_list.split(","),
        )
        solver.solve()

    except:
        to_return = html.Div(dcc.Markdown("### Something went wrong :("))

    else:
        to_return = html.Div(
            [
                dcc.Markdown("""### Problem"""),
                dash_isoperimetric_problem(solver=solver),
                dcc.Markdown("### Answer"),
                dash_answer(solver=solver),
            ]
        )

    return to_return


if __name__ == "__main__":

    # argparse
    parser = ArgumentParser(description="Server configuration")
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
