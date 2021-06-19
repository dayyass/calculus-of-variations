import sys
from argparse import ArgumentParser

from sympy import diff, dsolve, integrate, solve, var

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.abstract_problem import AbstractSolver
from calculus_of_variations.utils import sympy_eval, t, x, x_diff


class IsoperimetricProblemSolver(AbstractSolver):

    """
    Solver for isoperimetric problem in calculus of variation.

    Attributes:
        f0: Integrand.
        t0: Lower limit of the integral.
        t1: Upper limit of the integral.
        x0: Boundary condition in t0.
        x1: Boundary condition in t1.
        f_list: Isoperimetric conditions integrand list.
        alpha_list: Isoperimetric conditions value list.

    To use:
        solution = IsoperimetricProblemSolver(f0='x_diff ** 2', t0=0, t1=1, x0=0, x1=1, f_list=['x'], alpha_list=[0])
        solution.solve(verbose=True)
    """

    C1 = var("C1")
    C2 = var("C2")
    lambda_0 = var("lambda_0")

    def __init__(
        self,
        f0: str,
        t0: str,
        t1: str,
        x0: str,
        x1: str,
        f_list: str,
        alpha_list: str,
    ):
        self._f0_str = f0
        self._f_str_list = f_list

        self.f0 = sympy_eval(f0)
        self.t0 = sympy_eval(t0)
        self.t1 = sympy_eval(t1)
        self.x0 = sympy_eval(x0)
        self.x1 = sympy_eval(x1)
        self.f_list = [sympy_eval(f.strip()) for f in f_list.split(",")]
        self.alpha_list = [sympy_eval(alpha.strip()) for alpha in alpha_list.split(",")]

    def __str__(self):
        task = f"integral from {self.t0} to {self.t1} of ({self._f0_str})dt -> extr\n"
        condition_1 = f"x({self.t0}) = {self.x0}\n"
        condition_2 = f"x({self.t1}) = {self.x1}\n"
        integral_conditions = ""
        for f, alpha in zip(self.f_list, self.alpha_list):
            integral_conditions += (
                f"integral from {self.t0} to {self.t1} of ({f})dt = {alpha}\n"
            )

        return f"{task}{integral_conditions}{condition_1}{condition_2}"

    def __repr__(self):
        return self.__str__()

    def __make_lambdas(self):
        """
        Init lambdas for lagrangian function
        """
        self.lambdas = []
        for i in range(1, len(self.f_list) + 1):
            var(f"lambda_{i}")
            self.lambdas.append(var(f"lambda_{i}"))

    def __make_equations_and_params(self):
        """
        Init lagrangian function
        """
        self.equations = [self.first_eq, self.second_eq]
        self.params = [self.C1, self.C2]

        for i in range(len(self.f_list)):
            equation = (
                integrate(
                    self.f_list[i].subs(x, self.general_solution),
                    (t, self.t0, self.t1),
                )
                - self.alpha_list[i]
            )
            self.equations.append(equation)
            self.params.append(self.lambdas[i] / self.lambda_0)

    def _general_solution(self):
        """
        Find general solution.
        """
        self.L = self.lambda_0 * self.f0
        for i in range(len(self.f_list)):
            self.L += self.lambdas[i] * self.f_list[i]

        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs.expand()
        self.general_solution = general_solution

    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        self.__make_equations_and_params()

        coefficients = solve(self.equations, self.params)
        self.coefficients = coefficients

    def _particular_solution(self):
        """
        Substitute particular solution coefficients to general solution.
        """
        super()._particular_solution()

    def _extrema_value(self):
        """
        Find extrema value for particular solution.
        """
        f0_subs = self.f0.subs(
            [(x_diff, diff(self.particular_solution, t)), (x, self.particular_solution)]
        )
        extrema_value = integrate(f0_subs, (t, self.t0, self.t1))

        self.extrema_value = extrema_value

    def solve(self, verbose: bool = True):
        """
        Solve task using all encapsulated methods.
        """
        self.__make_lambdas()
        super().solve(verbose=verbose)


if __name__ == "__main__":

    # argparse
    parser = ArgumentParser()
    parser.add_argument("-f0", type=str, required=True, help="integrand")
    parser.add_argument(
        "-t0", type=str, required=True, help="lower limit of the integral"
    )
    parser.add_argument(
        "-t1", type=str, required=True, help="upper limit of the integral"
    )
    parser.add_argument("-x0", type=str, required=True, help="boundary condition in t0")
    parser.add_argument("-x1", type=str, required=True, help="boundary condition in t1")
    parser.add_argument(
        "-f_list",
        type=str,
        required=True,
        help="isoperimetric conditions integrand list",
    )
    parser.add_argument(
        "-alpha_list",
        type=str,
        required=True,
        help="isoperimetric conditions value list",
    )
    args = parser.parse_args()

    # solve
    IsoperimetricProblemSolver(
        f0=args.f0,
        t0=args.t0,
        x0=args.x0,
        t1=args.t1,
        x1=args.x1,
        f_list=args.f_list,
        alpha_list=args.alpha_list,
    ).solve()
