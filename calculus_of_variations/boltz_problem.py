import sys
from argparse import ArgumentParser

from sympy import Function, diff, dsolve, integrate, solve, var

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.abstract_problem import AbstractSolver

t = var("t")
x = Function("x")(t)
x_diff = diff(x, t)

t0 = var("t0")
t1 = var("t1")
x_t0 = Function("x")(t0)
x_t1 = Function("x")(t1)


class BoltzSolver(AbstractSolver):

    """
    Solver for Boltz problem in calculus of variation.

    Attributes:
        L: Integrand.
        l: Terminant.
        t0: Lower limit of the integral.
        t1: Upper limit of the integral.

    To use:
        solution = BoltzSolver(L='x_diff ** 2 + 2 * x', l='x_t0 ** 2', t0=0, t1=1)
        solution.solve(verbose=True)
    """

    C1 = var("C1")
    C2 = var("C2")

    def __init__(self, L: str, l: str, t0: float, t1: float):
        self._L_str = L
        self._l_str = l

        self.L = eval(L)
        self.l = eval(l)
        self.t0 = t0
        self.t1 = t1

    def __str__(self):
        task = f"integral from {self.t0} to {self.t1} of ({self._L_str})dt + {self._l_str} -> extr\n"
        return f"{task}"

    def __repr__(self):
        return self.__str__()

    def _general_solution(self):
        """
        Find general solution.
        """
        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs.expand()
        self.general_solution = general_solution

    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        self.first_eq = (
            self.L_x_diff.subs(
                [
                    (x_diff, diff(self.general_solution, t)),
                    (x, self.general_solution),
                    (t, self.t0),
                ]
            )
            - diff(self.l, x_t0).subs(x_t0, self.general_solution.subs(t, self.t0))
        )

        self.second_eq = (
            self.L_x_diff.subs(
                [
                    (x_diff, diff(self.general_solution, t)),
                    (x, self.general_solution),
                    (t, self.t1),
                ]
            )
            + diff(self.l, x_t1).subs(x_t1, self.general_solution.subs(t, self.t1))
        )

        coefficients = solve([self.first_eq, self.second_eq], [self.C1, self.C2])

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
        L_subs = self.L.subs(
            [(x_diff, diff(self.particular_solution, t)), (x, self.particular_solution)]
        )
        l_subs = self.l.subs(
            [
                (x_t0, self.particular_solution.subs(t, self.t0)),
                (x_t1, self.particular_solution.subs(t, self.t1)),
            ]
        )
        extrema_value = integrate(L_subs, (t, self.t0, self.t1)) + l_subs

        self.extrema_value = extrema_value

    def solve(self, verbose: bool = True):
        """
        Solve task using all encapsulated methods.
        """
        super().solve(verbose=verbose)


if __name__ == "__main__":

    # argparse
    parser = ArgumentParser()
    parser.add_argument("-L", type=str, required=True, help="integrand")
    parser.add_argument("-l", type=str, required=True, help="terminant")
    parser.add_argument(
        "-t0", type=float, required=True, help="lower limit of the integral"
    )
    parser.add_argument(
        "-t1", type=float, required=True, help="upper limit of the integral"
    )
    args = parser.parse_args()

    # solve
    BoltzSolver(L=args.L, l=args.l, t0=args.t0, t1=args.t1).solve()
