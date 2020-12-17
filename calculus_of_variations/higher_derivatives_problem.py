import sys
from argparse import ArgumentParser
from typing import List

from sympy import Function, diff, dsolve, integrate, solve, var

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.abstract_problem import AbstractSolver

t = var("t")
x = Function("x")(t)
x_diff = diff(x, t)

# maximum 4 order derivatives
x_diff_2 = diff(x, t, 2)
x_diff_3 = diff(x, t, 3)
x_diff_4 = diff(x, t, 4)


class HigherDerivativesSolver(AbstractSolver):

    """
    Solver for simplest problem with higher derivatives in calculus of variation.

    Attributes:
        n: Order of differentiation.
        L: Integrand.
        t0: Lower limit of the integral.
        t1: Upper limit of the integral.
        x0: Boundary condition in t0.
        x1: Boundary condition in t1.
        x0_array: Higher order boundary condition in t0 list.
        x1_array: Higher order boundary condition in t1 list.

    To use:
        solution = HigherDerivativesSolver(n=2, L='x_diff_2 ** 2', t0=0, t1=1, x0=0, x1=0, x0_array=[0], x1_array=[1])
        solution.solve(verbose=True)
    """

    def __init__(
        self,
        n: int,
        L: str,
        t0: float,
        t1: float,
        x0: float,
        x1: float,
        x0_array: List[float],
        x1_array: List[float],
    ):
        self._L_str = L

        self.n = n
        self.L = eval(L)
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1
        self.x0_array = x0_array
        self.x1_array = x1_array

    def __str__(self):
        task = f"integral from {self.t0} to {self.t1} of ({self._L_str})dt -> extr\n"
        condition_x0, condition_x1 = "", ""
        for i in range(self.n):
            if i == 0:
                condition_x0 += f"x({self.t0}) = {self.x0}\n"
                condition_x1 += f"x({self.t1}) = {self.x1}\n"
            else:
                condition_x0 += f"x_diff_{i}({self.t0}) = {self.x0_array[i-1]}\n"
                condition_x1 += f"x_diff_{i}({self.t1}) = {self.x1_array[i-1]}\n"

        return f"{task}{condition_x0}{condition_x1}"

    def __repr__(self):
        return self.__str__()

    def __make_Cs(self):
        """
        Init coefficients for general solution
        """
        self.Cs = []
        for i in range(1, 2 * self.n + 1):
            self.Cs.append(var("C{}".format(i)))

    def __make_equations(self):
        """
        Init the Euler-Poisson equation
        """
        self.equations = [self.first_eq, self.second_eq]

        for i in range(1, self.n):
            self.equations.append(
                diff(self.general_solution, t, i).subs(t, self.t0)
                - self.x0_array[i - 1]
            )
            self.equations.append(
                diff(self.general_solution, t, i).subs(t, self.t1)
                - self.x1_array[i - 1]
            )

    def __make_substitutions(self):
        """
        Substitutions for finding extrema_value
        """
        self.substitutions = [(x, self.particular_solution)]
        for i in range(1, self.n + 1):
            self.substitutions.append(
                (diff(x, t, i), diff(self.particular_solution, t, i))
            )
        self.substitutions = list(reversed(self.substitutions))

    def _general_solution(self):
        """
        Find general solution.
        """
        self.L_x = diff(self.L, x)
        self.de = self.L_x
        for i in range(1, self.n + 1):
            self.de += (-1) ** i * diff(diff(self.L, diff(x, t, i)), t, i)

        general_solution = dsolve(self.de, x).rhs.expand()
        self.general_solution = general_solution

    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        self.__make_Cs()
        self.__make_equations()

        coefficients = solve(self.equations, self.Cs)
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
        self.__make_substitutions()

        extrema_value = integrate(
            self.L.subs(self.substitutions), (t, self.t0, self.t1)
        )
        self.extrema_value = extrema_value

    def solve(self, verbose: bool = True):
        """
        Solve task using all encapsulated methods.
        """
        super().solve(verbose=verbose)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", type=int, required=True, help="order of differentiation")
    parser.add_argument("-L", type=str, required=True, help="integrand")
    parser.add_argument(
        "-t0", type=float, required=True, help="lower limit of the integral"
    )
    parser.add_argument(
        "-t1", type=float, required=True, help="upper limit of the integral"
    )
    parser.add_argument(
        "-x0", type=float, required=True, help="boundary condition in t0"
    )
    parser.add_argument(
        "-x1", type=float, required=True, help="boundary condition in t1"
    )
    parser.add_argument(
        "-x0_array",
        type=float,
        nargs="+",
        required=True,
        help="higher order boundary condition in t0 list",
    )
    parser.add_argument(
        "-x1_array",
        type=float,
        nargs="+",
        required=True,
        help="higher order boundary condition in t1 list",
    )
    args = parser.parse_args()

    HigherDerivativesSolver(
        n=args.n,
        L=args.L,
        t0=args.t0,
        t1=args.t1,
        x0=args.x0,
        x1=args.x1,
        x0_array=args.x0_array,
        x1_array=args.x1_array,
    ).solve()
