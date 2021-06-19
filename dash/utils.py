from typing import Dict

import dash_core_components as dcc
import dash_html_components as html
from sympy.core.symbol import Symbol


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
            dcc.Markdown(f"**General solution**: {solver.general_solution}"),
            dcc.Markdown(
                f"**Coefficients**: {print_coefficients(solver.coefficients)}"
            ),
            dcc.Markdown(f"**Particular solution**: {solver.particular_solution}"),
            dcc.Markdown(f"**Extrema value**: {solver.extrema_value}"),
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
