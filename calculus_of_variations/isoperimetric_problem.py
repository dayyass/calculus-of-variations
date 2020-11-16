from argparse import ArgumentParser
from sympy import var, Function, diff, integrate, dsolve, solve
from .abstract_problem import AbstractSolver
from typing import List

# to convert string to expression with eval()
from sympy.functions import *


t = var('t')
x = Function('x')(t)
x_diff = diff(x, t)


class IsoperimetricProblemSolver(AbstractSolver):

    """
    Solver for isoperimetric problem in calculus of variation.
    """

    C1 = var('C1')
    C2 = var('C2')
    lambda_0 = var('lambda_0')

    def __init__(
            self, f0: str, t0: float, t1: float, x0: float, x1: float, f_list: List[str], alpha_list: List[float],
    ):
        self._f0_str = f0
        self._f_str_list = f_list

        self.f0 = eval(f0)
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1
        self.f_list = [eval(f) for f in f_list]
        self.alpha_list = alpha_list

    def __str__(self):
        task = f'integral from {self.t0} to {self.t1} of ({self._f0_str})dt -> extr\n'
        condition_1 = f'x({self.t0}) = {self.x0}'
        condition_2 = f'x({self.t1}) = {self.x1}'
        integral_conditions = ''
        for f, alpha in zip(self.f_list, self.alpha_list):
            integral_conditions += f'integral from {self.t0} to {self.t1} of ({f})dt = {alpha}\n'

        return f'{task}\n{integral_conditions}\n{condition_1}\n{condition_2}\n'

    def __repr__(self):
        return self.__str__()

    def __make_lambdas(self):
        self.lambdas = []
        for i in range(1, len(self.f_list) + 1):
            var(f'lambda_{i}')
            self.lambdas.append(var(f'lambda_{i}'))

    def __make_equations_and_params(self):
        self.equations = [self.first_eq, self.second_eq]
        self.params = [self.C1, self.C2]

        for i in range(len(self.f_list)):
            equation = integrate(
                self.f_list[i].subs(x, self.general_solution),
                (t, self.t0, self.t1),
            ) - self.alpha_list[i]
            self.equations.append(equation)
            self.params.append(self.lambdas[i] / self.lambda_0)

    def _general_solution(self):
        self.L = self.lambda_0 * self.f0
        for i in range(len(self.f_list)):
            self.L += self.lambdas[i] * self.f_list[i]

        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs.expand()
        self.general_solution = general_solution

    def _coefficients(self):
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        self.__make_equations_and_params()

        coefficients = solve(self.equations, self.params)
        self.coefficients = coefficients

    def _particular_solution(self):
        super()._particular_solution()

    def _extrema_value(self):
        f0_subs = self.f0.subs([(x_diff, diff(self.particular_solution, t)), (x, self.particular_solution)])
        extrema_value = integrate(f0_subs, (t, self.t0, self.t1))

        self.extrema_value = extrema_value

    def solve(self, verbose: bool = True):
        self.__make_lambdas()
        super().solve(verbose=verbose)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f0', type=str, required=True)
    parser.add_argument('-t0', type=float, required=True)
    parser.add_argument('-t1', type=float, required=True)
    parser.add_argument('-x0', type=float, required=True)
    parser.add_argument('-x1', type=float, required=True)
    parser.add_argument('-f_list', type=str, nargs='+', required=True)
    parser.add_argument('-alpha_list', type=float, nargs='+', required=True)
    args = parser.parse_args()

    IsoperimetricProblemSolver(
        f0=args.f0, t0=args.t0, x0=args.x0, t1=args.t1, x1=args.x1, f_list=args.f_list, alpha_list=args.alpha_list,
    ).solve()
