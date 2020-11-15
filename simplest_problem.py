from argparse import ArgumentParser
from abstract_problem import AbstractSolver
from sympy import var, Function, diff, integrate, dsolve, solve


t = var('t')
x = Function('x')(t)
x_diff = diff(x, t)


class SimplestProblemSolver(AbstractSolver):

    """
    Solver for simplest problem in calculus of variation.
    """

    C1 = var('C1')
    C2 = var('C2')

    def __init__(self, L: str, t0: float, t1: float, x0: float, x1: float):
        self._L_str = L
        self.L = eval(L)
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1

    def __str__(self):
        task = f'integral from {self.t0} to {self.t1} of {self._L_str} -> extr'
        condition_1 = f'x({self.t0}) = {self.x0}'
        condition_2 = f'x({self.t1}) = {self.x1}'
        return f'{task}\n{condition_1}\n{condition_2}\n'

    def __repr__(self):
        return self.__str__()

    def _general_solution(self):
        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs
        self.general_solution = general_solution

    def _coefficients(self):
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        coefficients = solve([self.first_eq, self.second_eq], [self.C1, self.C2])
        self.coefficients = coefficients

    def _particular_solution(self):
        particular_solution = self.general_solution.subs(self.coefficients)
        self.particular_solution = particular_solution

    def _extrema_value(self):
        extreme_value = integrate(self.L.subs([(x_diff, diff(self.particular_solution, t)),
                                               (x, self.particular_solution)]),
                                  (t, self.t0, self.t1))

        self.extreme_value = extreme_value

    def solve(self, verbose: bool = True):
        self._general_solution()
        self._coefficients()
        self._particular_solution()
        self._extrema_value()

        if verbose:
            print(self)
            print(f'general_solution: {self.general_solution}')
            print(f'coefficients: {self.coefficients}')
            print(f'particular_solution: {self.particular_solution}')
            print(f'extreme_value: {self.extreme_value}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-L', type=str, required=True)
    parser.add_argument('-t0', type=float, required=True)
    parser.add_argument('-t1', type=float, required=True)
    parser.add_argument('-x0', type=float, required=True)
    parser.add_argument('-x1', type=float, required=True)
    args = parser.parse_args()

    SimplestProblemSolver(L=args.L, t0=args.t0, x0=args.x0, t1=args.t1, x1=args.x1).solve()
