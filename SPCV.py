from sympy import var, Function, diff, integrate, dsolve, solve

t = var('t')
x = Function('x')(t)
x_diff = diff(x, t)


class SPCV:
    # ToDo Fill __doc__
    """The Simplest Problem in Calculus of Variations"""

    C1 = var('C1')
    C2 = var('C2')

    def __init__(self, L=None,
                 t0=None, t1=None,
                 x0=None, x1=None):

        self.L = L
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1

    def __str__(self):
        # ToDo __str__
        pass

    def __repr__(self):
        # ToDo __repr__
        pass

    def _general_solution(self):
        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs
        self.general_solution = general_solution

    def _coefficients(self):
        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        coefficients = solve([self.first_eq, self.second_eq], [SPCV.C1, SPCV.C2])
        self.coefficients = coefficients

    def _particular_solution(self):
        particular_solution = self.general_solution.subs(self.coefficients)
        self.particular_solution = particular_solution

    def _extreme_value(self):
        extreme_value = integrate(self.L.subs([(x_diff, diff(self.particular_solution, t)),
                                               (x, self.particular_solution)]),
                                  (t, self.t0, self.t1))

        self.extreme_value = extreme_value

    def solve(self):
        self._general_solution()
        self._coefficients()
        self._particular_solution()
        self._extreme_value()


def main():
    from sympy.functions import exp

    def solver(L, t0, t1, x0, x1):
        task = SPCV(L, t0, t1, x0, x1)
        task.solve()
        print('task')
        print('general_solution', task.general_solution)
        print('coefficients', task.coefficients)
        print('particular_solution', task.particular_solution)
        print('extreme_value', task.extreme_value)
        print()

    solver(L=x_diff ** 2,
           t0=0, x0=0,
           t1=1, x1=1)

    solver(L=x_diff ** 2 + t * x,
           t0=0, x0=0,
           t1=1, x1=0)

    solver(L=t * x_diff ** 2,
           t0=1, x0=0,
           t1=exp(1), x1=1)

    solver(L=x_diff ** 2 + x_diff * x + 12 * t * x,
           t0=0, x0=0,
           t1=1, x1=0)

    solver(L=x_diff ** 2 - t ** 2 * x,
           t0=0, x0=0,
           t1=1, x1=0)

    # Test
    try:
        solver(L=x_diff ** 4,
               t0=0, x0=0,
               t1=1, x1=0)
    except:
        print('Cannot solve :(')


if __name__ == '__main__':
    main()
