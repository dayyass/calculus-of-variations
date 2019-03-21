import SPCV
from SPCV import t, x, x_diff


from sympy import var, Function, diff, integrate, dsolve, solve


t0 = var('t0')
t1 = var('t1')
x_t0 = Function('x')(t0)
x_t1 = Function('x')(t1)


class Boltz(SPCV.SPCV):
    # ToDo Fill __doc__
    """The Boltz Problem"""

    # ToDo Change the way of declare
    C1 = var('C1')
    C2 = var('C2')

    def __init__(self, L=None, l=None,
                 t0=None, t1=None):
        self.L = L
        self.l = l
        self.t0 = t0
        self.t1 = t1

    def _general_solution(self):
        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs
        self.general_solution = general_solution

    def _coefficients(self):
        self.first_eq = self.L_x_diff.subs([(x_diff, diff(self.general_solution, t)),
                                            (x, self.general_solution), (t, self.t0)]) - \
                        diff(self.l, x_t0).subs(x_t0, self.general_solution.subs(t, self.t0))

        self.second_eq = self.L_x_diff.subs([(x_diff, diff(self.general_solution, t)),
                                             (x, self.general_solution), (t, self.t1)]) + \
                         diff(self.l, x_t1).subs(x_t1, self.general_solution.subs(t, self.t1))

        coefficients = solve([self.first_eq, self.second_eq], [Boltz.C1, Boltz.C2])

        self.coefficients = coefficients

    def _particular_solution(self):
        super()._particular_solution()

    def _extreme_value(self):
        extreme_value = integrate(self.L.subs([(x_diff, diff(self.particular_solution, t)),
                                               (x, self.particular_solution)]),
                                  (t, self.t0,self.t1)) + \
                        self.l.subs([(x_t0, self.particular_solution.subs(t, self.t0)),
                                     (x_t1, self.particular_solution.subs(t, self.t1))])

        self.extreme_value = extreme_value

    def solve(self):
        super().solve()


def main():
    from sympy.functions import exp, log

    def solver(L, l, t0, t1):
        task = Boltz(L, l, t0, t1)
        task.solve()
        print('task')
        print('general_solution', task.general_solution)
        print('coefficients', task.coefficients)
        print('particular_solution', task.particular_solution)
        print('extreme_value', task.extreme_value)
        print()

    solver(L=x_diff ** 2 + 2 * x,
           l=x_t0 ** 2,
           t0=0, t1=1)

    solver(L=x_diff ** 2 - x,
           l=-x_t1 ** 2 / 2,
           t0=0, t1=1)

    solver(L=t ** 2 * x_diff ** 2,
           l=-2 * x_t0 + x_t1 ** 2,
           t0=1, t1=2)

    solver(L=2 * (t * x_diff ** 2 + x_diff * x),
           l=3 * x_t0 ** 2 - x_t1 ** 2 - 4 * x_t1,
           t0=1, t1=exp(1))


if __name__ == '__main__':
    main()
