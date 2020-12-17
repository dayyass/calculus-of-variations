import sys
from argparse import ArgumentParser

from sympy import Function, diff, dsolve, integrate, solve, var

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.abstract_problem import AbstractSolver

# maximum 2 dimensions
t = var("t")
x1 = Function("x1")(t)
x1_diff = diff(x1, t)
x2 = Function("x2")(t)
x2_diff = diff(x2, t)


class MultidimensionalSolver(AbstractSolver):

    """
    Solver for simplest problem with two dimensions in calculus of variation.

    Attributes:
        L: Integrand.
        t0: Lower limit of the integral.
        t1: Upper limit of the integral.
        x1_0: Boundary condition of x1 in t0.
        x1_1: Boundary condition of x1 in t1.
        x2_0: Boundary condition of x2 in t0.
        x2_1: boundary condition of x2 in t1.

    To use:
        solution = MultidimensionalSolver(L='x1_diff**2 + x2_diff**2', t0=0, t1=1, x1_0=0, x1_1=1, x2_0=0, x2_1=1)
        solution.solve(verbose=True)
    """

    C1 = var("C1")
    C2 = var("C2")
    C3 = var("C3")
    C4 = var("C4")

    def __init__(
        self,
        L: str,
        t0: float,
        t1: float,
        x1_0: float,
        x1_1: float,
        x2_0: float,
        x2_1: float,
    ):
        self._L_str = L

        self.L = eval(L)
        self.t0 = t0
        self.t1 = t1
        self.x1_0 = x1_0
        self.x1_1 = x1_1
        self.x2_0 = x2_0
        self.x2_1 = x2_1

    def __str__(self):
        task = f"integral from {self.t0} to {self.t1} of ({self._L_str})dt -> extr\n"
        condition_x1_0 = f"x1({self.t0}) = {self.x1_0}\n"
        condition_x1_1 = f"x1({self.t1}) = {self.x1_1}\n"
        condition_x2_0 = f"x2({self.t0}) = {self.x2_0}\n"
        condition_x2_1 = f"x2({self.t1}) = {self.x2_1}\n"
        return f"{task}{condition_x1_0}{condition_x1_1}{condition_x2_0}{condition_x2_1}"

    def __repr__(self):
        return self.__str__()

    def __make_substitutions(self):
        """
        Substitutions for finding extrema_value
        """
        self.substitutions = [
            (x1_diff, diff(self.particular_solution_1, t)),
            (x2_diff, diff(self.particular_solution_2, t)),
            (x1, self.particular_solution_1),
            (x2, self.particular_solution_2),
        ]

    def _general_solution(self):
        """
        Find general solution.
        """
        self.L_x1 = diff(self.L, x1)
        self.L_x2 = diff(self.L, x2)
        self.L_x1_diff = diff(self.L, x1_diff)
        self.L_x2_diff = diff(self.L, x2_diff)

        self.de1 = self.L_x1 - diff(self.L_x1_diff, t)
        self.de2 = self.L_x2 - diff(self.L_x2_diff, t)

        self.Cs_1 = (self.C1, self.C3)
        self.Cs_2 = (self.C2, self.C4)

        if self.L_x1 == self.L_x1.subs(
            [(x2_diff, 0), (x2, 0)]
        ) and self.L_x2 == self.L_x2.subs([(x1_diff, 0), (x1, 0)]):
            general_solution_1 = dsolve(self.de1).rhs.expand()
            general_solution_2 = (
                dsolve(self.de2).rhs.expand().subs([self.Cs_1, self.Cs_2])
            )

        elif self.L_x1 == self.L_x1.subs([(x2_diff, 0), (x2, 0)]):
            general_solution_1 = dsolve(self.de1).rhs.expand()
            general_solution_2 = (
                dsolve(self.de2)
                .rhs.expand()
                .subs(
                    [
                        (x1_diff, diff(general_solution_1, t)),
                        (x1, general_solution_1),
                        self.Cs_1,
                        self.Cs_2,
                    ]
                )
            )
        elif self.L_x2 == self.L_x2.subs([(x1_diff, 0), (x1, 0)]):
            general_solution_2 = dsolve(self.de2).rhs.expand()
            general_solution_1 = (
                dsolve(self.de1)
                .rhs.expand()
                .subs(
                    [
                        (x2_diff, diff(general_solution_2, t)),
                        (x2, general_solution_2),
                        self.Cs_1,
                        self.Cs_2,
                    ]
                )
            )
        else:
            general_solution = dsolve([self.de1, self.de2], [x1, x2])
            general_solution_1 = general_solution[0].rhs.expand()
            general_solution_2 = general_solution[1].rhs.expand()

        self.general_solution_1 = general_solution_1
        self.general_solution_2 = general_solution_2

    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        self.first_eq = self.general_solution_1.subs(t, self.t0) - self.x1_0
        self.second_eq = self.general_solution_1.subs(t, self.t1) - self.x1_1
        self.third_eq = self.general_solution_2.subs(t, self.t0) - self.x2_0
        self.fourth_eq = self.general_solution_2.subs(t, self.t1) - self.x2_1

        self.equations = [self.first_eq, self.second_eq, self.third_eq, self.fourth_eq]
        self.params = [self.C1, self.C2, self.C3, self.C4]

        coefficients = solve(self.equations, self.params)
        self.coefficients = coefficients

    def _particular_solution(self):
        """
        Substitute particular solution coefficients to general solution.
        """
        self.particular_solution_1 = self.general_solution_1.subs(self.coefficients)
        self.particular_solution_2 = self.general_solution_2.subs(self.coefficients)

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
        super().solve(verbose=False)

        if verbose:
            print(self)
            print(f"general_solution_1: {self.general_solution_1}")
            print(f"general_solution_2: {self.general_solution_2}")
            print(f"coefficients: {self.coefficients}")
            print(f"particular_solution_1: {self.particular_solution_1}")
            print(f"particular_solution_2: {self.particular_solution_2}")
            print(f"extrema_value: {self.extrema_value}")
            print()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-L", type=str, required=True, help="integrand")
    parser.add_argument(
        "-t0", type=float, required=True, help="lower limit of the integral"
    )
    parser.add_argument(
        "-t1", type=float, required=True, help="upper limit of the integral"
    )
    parser.add_argument(
        "-x1_0", type=float, required=True, help="boundary condition of x1 in t0"
    )
    parser.add_argument(
        "-x1_1", type=float, required=True, help="boundary condition of x1 in t1"
    )
    parser.add_argument(
        "-x2_0", type=float, required=True, help="boundary condition of x2 in t0"
    )
    parser.add_argument(
        "-x2_1", type=float, required=True, help="boundary condition of x2 in t1"
    )
    args = parser.parse_args()

    MultidimensionalSolver(
        L=args.L,
        t0=args.t0,
        t1=args.t1,
        x1_0=args.x1_0,
        x1_1=args.x1_1,
        x2_0=args.x2_0,
        x2_1=args.x2_1,
    ).solve()
