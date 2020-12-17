import sys

import dash_core_components as dcc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.isoperimetric_problem import IsoperimetricProblemSolver

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Markdown("""# Isoperimetric problem dash"""),
        html.Div([html.Label("Enter f0"), dcc.Input(id="f0")]),
        html.H4(""),
        html.Div([html.Label("Enter t0"), dcc.Input(id="t0")]),
        html.H4(""),
        html.Div([html.Label("Enter t1"), dcc.Input(id="t1")]),
        html.H4(""),
        html.Div([html.Label("Enter x0"), dcc.Input(id="x0")]),
        html.H4(""),
        html.Div([html.Label("Enter x1"), dcc.Input(id="x1")]),
        html.H4(""),
        html.Div([html.Label("Enter f_list"), dcc.Input(id="f_list")]),
        html.H4(""),
        html.Div([html.Label("Enter alpha_list"), dcc.Input(id="alpha_list")]),
        html.H4(""),
        html.Div(id="my_input"),
    ]
)


@app.callback(
    Output("my_input", "children"),
    [
        Input("f0", "value"),
        Input("t0", "value"),
        Input("t1", "value"),
        Input("x0", "value"),
        Input("x1", "value"),
        Input("f_list", "value"),
        Input("alpha_list", "value"),
    ],
)
def update_output(f0, t0, t1, x0, x1, f_list, alpha_list):
    if (
        (f0 is not None)
        & (t0 is not None)
        & (t1 is not None)
        & (x0 is not None)
        & (x1 is not None)
        & (f_list is not None)
        & (alpha_list is not None)
    ):

        solver = IsoperimetricProblemSolver(
            f0=f0,
            t0=float(t0),
            t1=float(t1),
            x0=float(x0),
            x1=float(x1),
            f_list=f_list.split(),
            alpha_list=[float(alpha) for alpha in alpha_list.split()],
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
