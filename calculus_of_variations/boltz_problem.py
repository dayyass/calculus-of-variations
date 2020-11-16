from argparse import ArgumentParser
from sympy import var, Function, diff, integrate, dsolve, solve
from .abstract_problem import AbstractSolver


t = var('t')
x = Function('x')(t)
x_diff = diff(x, t)

t0 = var('t0')
t1 = var('t1')
x_t0 = Function('x')(t0)
x_t1 = Function('x')(t1)


class BoltzSolver(AbstractSolver):

    """
    Solver for Boltz problem in calculus of variation.
    """

    C1 = var('C1')
    C2 = var('C2')

    def __init__(self, L: str, l: str, t0: float, t1: float):
        self._L_str = L
        self._l_str = l

        self.L = eval(L)
        self.l = eval(l)
        self.t0 = t0
        self.t1 = t1

    def __str__(self):
        task = f'integral from {self.t0} to {self.t1} of ({self._L_str})dt + {self._l_str} -> extr\n'
        return f'{task}\n'

    def __repr__(self):
        return self.__str__()

    def _general_solution(self):
        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs.expand()
        self.general_solution = general_solution

    def _coefficients(self):
        self.first_eq = self.L_x_diff.subs([
            (x_diff, diff(self.general_solution, t)),
            (x, self.general_solution), (t, self.t0),
        ]) - diff(self.l, x_t0).subs(x_t0, self.general_solution.subs(t, self.t0))

        self.second_eq = self.L_x_diff.subs([
            (x_diff, diff(self.general_solution, t)),
            (x, self.general_solution), (t, self.t1),
        ]) + diff(self.l, x_t1).subs(x_t1, self.general_solution.subs(t, self.t1))

        coefficients = solve([self.first_eq, self.second_eq], [self.C1, self.C2])

        self.coefficients = coefficients

    def _particular_solution(self):
        super()._particular_solution()

    def _extrema_value(self):
        L_subs = self.L.subs([(x_diff, diff(self.particular_solution, t)), (x, self.particular_solution)])
        l_subs = self.l.subs([
            (x_t0, self.particular_solution.subs(t, self.t0)),
            (x_t1, self.particular_solution.subs(t, self.t1)),
        ])
        extreme_value = integrate(L_subs, (t, self.t0, self.t1)) + l_subs

        self.extreme_value = extreme_value

    def solve(self, verbose: bool = True):
        super().solve(verbose=verbose)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-L', type=str, required=True)
    parser.add_argument('-l', type=str, required=True)
    parser.add_argument('-t0', type=float, required=True)
    parser.add_argument('-t1', type=float, required=True)
    args = parser.parse_args()

    BoltzSolver(L=args.L, l=args.l, t0=args.t0, t1=args.t1).solve()
