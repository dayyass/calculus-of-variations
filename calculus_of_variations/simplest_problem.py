from argparse import ArgumentParser

from sympy import Function, diff, dsolve, integrate, solve, var

from .abstract_problem import AbstractSolver

t = var("t")
x = Function("x")(t)
x_diff = diff(x, t)


class SimplestProblemSolver(AbstractSolver):

    """
    Solver for simplest problem in calculus of variation.

    Attributes:
        L: Integrand.
        t0: Lower limit of the integral.
        t1: Upper limit of the integral.
        x0: Boundary condition in t0.
        x1: Boundary condition in t1.

    To use:
        solution = SimplestProblemSolver(L='x_diff ** 2', t0=0, t1=1, x0=0, x1=1)
        solution.solve(verbose=True)
    """

    C1 = var("C1")
    C2 = var("C2")

    def __init__(self, L: str, t0: float, t1: float, x0: float, x1: float):
        """

        @param L:
        @param t0:
        @param t1:
        @param x0:
        @param x1:
        """
        self._L_str = L

        self.L = eval(L)
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1

    def __str__(self):
        task = f"integral from {self.t0} to {self.t1} of ({self._L_str})dt -> extr\n"
        condition_1 = f"x({self.t0}) = {self.x0}\n"
        condition_2 = f"x({self.t1}) = {self.x1}\n"
        return f"{task}{condition_1}{condition_2}"

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
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

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
        extrema_value = integrate(L_subs, (t, self.t0, self.t1))

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
    args = parser.parse_args()

    # solve
    SimplestProblemSolver(
        L=args.L, t0=args.t0, x0=args.x0, t1=args.t1, x1=args.x1
    ).solve()
