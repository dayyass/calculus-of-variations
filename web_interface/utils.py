from argparse import ArgumentParser
from typing import Dict

import dash_core_components as dcc
import dash_html_components as html
from sympy.core.symbol import Symbol


def get_argparse() -> ArgumentParser:
    """
    Helper function to get ArgumentParser.
    """

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

    return parser


def print_coefficients(coefficients: Dict[Symbol, float]) -> str:
    """
    Convert dict of coefficients to ready-to-print coefficients string.

    :param Dict[Symbol, float] coefficients: dict of coefficients.
    :return: ready-to-print coefficients string.
    :rtype: str
    """

    return ", ".join([f"{k} = {v}" for k, v in coefficients.items()])


def dash_answer(solver):
    """
    Helper function to print solver answer.
    """

    return html.Div(
        [
            dcc.Markdown(
                r"**General solution**: "
                + str(solver.general_solution).replace("*", r"\*")
            ),
            dcc.Markdown(
                r"**Coefficients**: "
                + str(print_coefficients(solver.coefficients)).replace("*", r"\*")
            ),
            dcc.Markdown(
                r"**Particular solution**: "
                + str(solver.particular_solution).replace("*", r"\*")
            ),
            dcc.Markdown(
                r"**Extrema value**: " + str(solver.extrema_value).replace("*", r"\*")
            ),
        ]
    )


def dash_simplest_problem(
    solver,
    render_latex_url=r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print simplest problem.
    """

    return html.Div(
        [
            html.Img(
                src=rf"{render_latex_url}=I(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.L})| dt \to extr".replace(
                    "+", "%2B"
                )
            ),
            html.Br(),
            html.Img(src=f"{render_latex_url}=x({solver.t0}) = {solver.x0}"),
            html.Br(),
            html.Img(src=f"{render_latex_url}=x({solver.t1}) = {solver.x1}"),
            html.Br(),
        ]
    )


def dash_boltz_problem(
    solver,
    render_latex_url=r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print boltz problem.
    """

    return html.Div(
        [
            html.Img(
                src=rf"{render_latex_url}=B(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.L})| + \verb|({solver.l})| dt \to extr".replace(
                    "+", "%2B"
                )
            ),
            html.Br(),
        ]
    )


def dash_isoperimetric_problem(
    solver,
    render_latex_url=r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print isoperimetric problem.
    """

    problem = [
        html.Img(
            src=rf"{render_latex_url}=I_0(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.f0})| dt \to extr".replace(
                "+", "%2B"
            )
        ),
        html.Br(),
    ]

    for i in range(len(solver.f_list)):
        problem.extend(
            [
                html.Img(
                    src=rf"{render_latex_url}=I_{i + 1}(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.f_list[i]})| dt = {solver.alpha_list[i]}".replace(
                        "+", "%2B"
                    )
                ),
                html.Br(),
            ]
        )

    problem.extend(
        [
            html.Img(src=f"{render_latex_url}=x({solver.t0}) = {solver.x0}"),
            html.Br(),
            html.Img(src=f"{render_latex_url}=x({solver.t1}) = {solver.x1}"),
            html.Br(),
        ]
    )

    return html.Div(problem)
