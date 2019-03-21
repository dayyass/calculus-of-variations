import SPCV
from SPCV import t, x, x_diff


from sympy import var, Function, diff, integrate, dsolve, solve


class Isoperimetric(SPCV.SPCV):
    # ToDo Fill __doc__
    """The Isoperimetric Problem"""

    # ToDo Change the way of declare
    C1 = var('C1')
    C2 = var('C2')
    lambda_0 = var('lambda_0')

    def __init__(self, f0=None,
                 t0=None, t1=None,
                 x0=None, x1=None,
                 f_list=None, alphas=None):
        self.f0 = f0
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1
        self.f_list = f_list or []
        self.alphas = alphas or []

    def _make_lambdas(self):
        self.lambdas = []
        for i in range(1, len(self.f_list) + 1):
            var(f'lambda_{i}')
            self.lambdas.append(var(f'lambda_{i}'))

    def _general_solution(self):
        self.L = Isoperimetric.lambda_0 * self.f0
        for i in range(len(self.f_list)):
            self.L += self.lambdas[i] * self.f_list[i]

        self.L_x_diff = diff(self.L, x_diff)
        self.L_x = diff(self.L, x)

        general_solution = dsolve(self.L_x - diff(self.L_x_diff, t), x).rhs
        self.general_solution = general_solution

    def _coefficients(self):

        def _make_equations_and_params():
            self.equations = [self.first_eq, self.second_eq]
            self.params = [Isoperimetric.C1, Isoperimetric.C2]

            for i in range(len(self.f_list)):
                equation = integrate(self.f_list[i].subs(x, self.general_solution),
                                     (t, self.t0, self.t1)) - self.alphas[i]
                self.equations.append(equation)
                self.params.append(self.lambdas[i] / Isoperimetric.lambda_0)

        self.first_eq = self.general_solution.subs(t, self.t0) - self.x0
        self.second_eq = self.general_solution.subs(t, self.t1) - self.x1

        _make_equations_and_params()

        coefficients = solve(self.equations,
                             self.params)

        self.coefficients = coefficients

    def _particular_solution(self):
        super()._particular_solution()

    def _extreme_value(self):
        extreme_value = integrate(self.f0.subs([(x_diff, diff(self.particular_solution, t)),
                                                (x, self.particular_solution)]),
                                  (t, self.t0, self.t1))

        self.extreme_value = extreme_value

    def solve(self):
        self._make_lambdas()
        super().solve()


def main():
    from sympy import pi
    from sympy.functions import exp, log, sin, cos

    def solver(f0, t0, t1, x0, x1, f_list, alpha):
        task = Isoperimetric(f0, t0, t1, x0, x1, f_list, alpha)
        task.solve()
        print('task')
        print('lambdas', task.lambdas)
        print('general_solution', task.general_solution)
        print('coefficients', task.coefficients)
        print('particular_solution', task.particular_solution)
        print('extreme_value', task.extreme_value)
        print()

    solver(f0=x_diff**2,
           t0=0, t1=1,
           x0=0, x1=1,
           f_list=[x], alpha=[0])

    solver(f0=x_diff ** 2,
           t0=0, t1=1,
           x0=0, x1=1,
           f_list=[t * x], alpha=[0])

    solver(f0=x_diff ** 2,
           t0=0, t1=1,
           x0=0, x1=0,
           f_list=[x, t * x], alpha=[1, 0])

    solver(f0=x_diff ** 2,
           t0=0, t1=pi,
           x0=1, x1=-1,
           f_list=[x * cos(t)], alpha=[pi / 2])

    # ToDo Something wrong with answer
    solver(f0=t ** 2 * x_diff ** 2,
           t0=1, t1=2,
           x0=1, x1=2,
           f_list=[t * x], alpha=[7 / 3])


if __name__ == '__main__':
    main()
