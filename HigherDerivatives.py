import SPCV
from SPCV import t, x, x_diff

from sympy import var, Function, diff, integrate, dsolve, solve

x_double_diff = diff(x, t, 2)
x_triple_diff = diff(x, t, 3)


class HigherDerivatives(SPCV.SPCV):
    # ToDo Fill __doc__
    """The HigherDerivatives Problem"""

    def __init__(self, L=None,
                 t0=None, t1=None,
                 x0=None, x1=None,
                 x0_array=None, x1_array=None,
                 n=2):
        self.L = L
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1
        self.x0_array = x0_array or []
        self.x1_array = x1_array or []
        self.n = n

    def _general_solution(self):
        self.L_x = diff(self.L, x)
        self.de = self.L_x
        for i in range(1, self.n + 1):
            self.de += (-1) ** i * diff(diff(self.L, diff(x, t, i)), t, i)

        general_solution = dsolve(self.de, x).rhs
        self.general_solution = general_solution

    def _coefficients(self):

        def _make_Cs():
            self.Cs = []

            for i in range(1, 2 * self.n + 1):
                # ToDo Испривать
                var('C{}'.format(i))
                self.Cs.append('C{}'.format(i))

        def _make_equations():
            self.equations = [self.first_eq, self.second_eq]

            for i in range(1, self.n):
                self.equations.append(diff(self.general_solution, t, i).subs(t, self.t0) - self.x0_array[i - 1])
                self.equations.append(diff(self.general_solution, t, i).subs(t, self.t1) - self.x1_array[i - 1])

        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        _make_Cs()
        _make_equations()

        coefficients = solve(self.equations, self.Cs)

        self.coefficients = coefficients

    def _particular_solution(self):
        super()._particular_solution()

    def _extreme_value(self):
        def _make_substitutions():
            self.substitutions = [(x, self.particular_solution)]
            for i in range(1, self.n + 1):
                self.substitutions.append((diff(x, t, i),
                                           diff(self.particular_solution, t, i)))
            self.substitutions = list(reversed(self.substitutions))

        _make_substitutions()

        extreme_value = integrate(self.L.subs(self.substitutions), (t, self.t0, self.t1))

        self.extreme_value = extreme_value

    def solve(self):
        super().solve()


def main():
    from sympy.functions import exp, log

    def solver(L, t0, t1, x0, x1, x0_array, x1_array, n):
        task = HigherDerivatives(L, t0, t1, x0, x1, x0_array, x1_array, n)
        task.solve()
        print('task')
        print('Cs', task.Cs)
        print('general_solution', task.general_solution)
        print('coefficients', task.coefficients)
        print('particular_solution', task.particular_solution)
        print('extreme_value', task.extreme_value)
        print()

    solver(n=2, L=x_double_diff ** 2,
           t0=0, t1=1,
           x0=0, x1=0,
           x0_array=[0], x1_array=[1])

    solver(n=2, L=x_double_diff ** 2 - 48 * x,
           t0=0, t1=1,
           x0=1, x1=0,
           x0_array=[-4], x1_array=[0])

    solver(n=3, L=x_triple_diff ** 2,
           t0=0, t1=1,
           x0=0, x1=1,
           x0_array=[0, 0], x1_array=[3, 6])

    solver(n=2, L=x_double_diff ** 2 - 24 * t * x,
           t0=0, t1=1,
           x0=0, x1=0.2,
           x0_array=[0], x1_array=[1])

    # ToDo Fix it
    x_fourth_diff = diff(x, t, 4)
    solver(n=4, L=x_fourth_diff ** 2,
           t0=0, t1=1,
           x0=0, x1=1,
           x0_array=[0, 0, 0], x1_array=[3, 6, 10])


if __name__ == '__main__':
    main()
