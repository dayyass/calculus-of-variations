import sys
from argparse import ArgumentParser
from typing import Dict, Union

import dash_core_components as dcc
import dash_html_components as html
from sympy.core.symbol import Symbol

# TODO: fix it
sys.path.append("./")
from src.calculus_of_variations import (
    BoltzSolver,
    HigherDerivativesSolver,
    IsoperimetricSolver,
    MultidimensionalSolver,
    SimplestSolver,
)


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


def dash_answer(
    solver: Union[
        BoltzSolver, IsoperimetricSolver, SimplestSolver, HigherDerivativesSolver
    ]
):
    """
    Helper function to print solver answer.
    """

    answer = [
        dcc.Markdown(
            r"**General solution**: " + str(solver.general_solution).replace("*", r"\*")
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

    return html.Div(answer)


def dash_multidimensional_answer(solver: MultidimensionalSolver):
    """
    Helper function to print multidimensional solver answer.
    """

    answer = [
        dcc.Markdown(
            r"**General solution 1**: "
            + str(solver.general_solution_1).replace("*", r"\*")
        ),
        dcc.Markdown(
            r"**General solution 2**: "
            + str(solver.general_solution_2).replace("*", r"\*")
        ),
        dcc.Markdown(
            r"**Coefficients**: "
            + str(print_coefficients(solver.coefficients)).replace("*", r"\*")
        ),
        dcc.Markdown(
            r"**Particular solution_1**: "
            + str(solver.particular_solution_1).replace("*", r"\*")
        ),
        dcc.Markdown(
            r"**Particular solution_2**: "
            + str(solver.particular_solution_2).replace("*", r"\*")
        ),
        dcc.Markdown(
            r"**Extrema value**: " + str(solver.extrema_value).replace("*", r"\*")
        ),
    ]

    return html.Div(answer)


def dash_simplest_problem(
    solver: SimplestSolver,
    render_latex_url: str = r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print simplest problem.
    """

    assert isinstance(
        solver, SimplestSolver
    ), f"solver should be SimplestSolver, not {type(solver)}."

    problem = [
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

    return html.Div(problem)


def dash_boltz_problem(
    solver: BoltzSolver,
    render_latex_url: str = r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print boltz problem.
    """

    assert isinstance(
        solver, BoltzSolver
    ), f"solver should be BoltzSolver, not {type(solver)}."

    problem = [
        html.Img(
            src=rf"{render_latex_url}=B(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.L})| + \verb|({solver.l})| dt \to extr".replace(
                "+", "%2B"
            )
        ),
        html.Br(),
    ]

    return html.Div(problem)


def dash_isoperimetric_problem(
    solver: IsoperimetricSolver,
    render_latex_url: str = r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print isoperimetric problem.
    """

    assert isinstance(
        solver, IsoperimetricSolver
    ), f"solver should be IsoperimetricSolver, not {type(solver)}."

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


def dash_higher_derivatives_problem(
    solver: HigherDerivativesSolver,
    render_latex_url: str = r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print higher derivatives problem.
    """

    assert isinstance(
        solver, HigherDerivativesSolver
    ), f"solver should be HigherDerivativesSolver, not {type(solver)}."

    problem = [
        html.Img(
            src=rf"{render_latex_url}=I(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.L})| dt \to extr".replace(
                "+", "%2B"
            )
        ),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x({solver.t0}) = {solver.x0}"),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x({solver.t1}) = {solver.x1}"),
        html.Br(),
    ]

    for i in range(1, solver.n):
        problem.extend(
            [
                html.Img(
                    src=rf"{render_latex_url}=\verb|x_diff_{i}({solver.t0}) = {solver.x0_array[i-1]}|"
                ),
                html.Br(),
                html.Img(
                    src=rf"{render_latex_url}=\verb|x_diff_{i}({solver.t1}) = {solver.x1_array[i-1]}|"
                ),
                html.Br(),
            ]
        )

    return html.Div(problem)


def dash_multidimensional_problem(
    solver: MultidimensionalSolver,
    render_latex_url: str = r"https://render.githubusercontent.com/render/math?math",
):
    """
    Helper function to print multidimensional problem.
    """

    assert isinstance(
        solver, MultidimensionalSolver
    ), f"solver should be MultidimensionalSolver, not {type(solver)}."

    problem = [
        html.Img(
            src=rf"{render_latex_url}=I(x) = \int_{solver.t0}^{solver.t1} \verb|({solver.L})| dt \to extr".replace(
                "+", "%2B"
            )
        ),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x_1({solver.t0}) = {solver.x1_0}"),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x_1({solver.t1}) = {solver.x1_1}"),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x_2({solver.t0}) = {solver.x2_0}"),
        html.Br(),
        html.Img(src=rf"{render_latex_url}=x_2({solver.t1}) = {solver.x2_1}"),
        html.Br(),
    ]

    return html.Div(problem)
