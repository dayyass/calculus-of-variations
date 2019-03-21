import SPCV
from SPCV import t

from sympy import var, Function, diff, integrate, dsolve, solve

x1 = Function('x1')(t)
x1_diff = diff(x1, t)
x2 = Function('x2')(t)
x2_diff = diff(x2, t)


class Multidimensional(SPCV.SPCV):
    # ToDo Fill __doc__
    """The Multidimensional Problem"""

    # ToDo Change the way of declare
    C1 = var('C1')
    C2 = var('C2')
    C3 = var('C3')
    C4 = var('C4')

    def __init__(self, L=None,
                 t0=None, t1=None,
                 x1_0=None, x1_1=None,
                 x2_0=None, x2_1=None):
        self.L = L
        self.t0 = t0
        self.t1 = t1
        self.x1_0 = x1_0
        self.x1_1 = x1_1
        self.x2_0 = x2_0
        self.x2_1 = x2_1

    def _general_solution(self):
        self.L_x1 = diff(self.L, x1)
        self.L_x2 = diff(self.L, x2)
        self.L_x1_diff = diff(self.L, x1_diff)
        self.L_x2_diff = diff(self.L, x2_diff)

        self.de1 = self.L_x1 - diff(self.L_x1_diff, t)
        self.de2 = self.L_x2 - diff(self.L_x2_diff, t)

        self.Cs_1 = (Multidimensional.C1,
                     Multidimensional.C3)
        self.Cs_2 = (Multidimensional.C2,
                     Multidimensional.C4)

        if self.L_x1 == self.L_x1.subs([(x2_diff, 0), (x2, 0)]) and \
                self.L_x2 == self.L_x2.subs([(x1_diff, 0), (x1, 0)]):
            general_solution_1 = dsolve(self.de1).rhs
            general_solution_2 = dsolve(self.de2).rhs.subs([self.Cs_1, self.Cs_2])

        elif self.L_x1 == self.L_x1.subs([(x2_diff, 0), (x2, 0)]):
            general_solution_1 = dsolve(self.de1).rhs
            general_solution_2 = dsolve(self.de2).rhs.subs([(x1_diff, diff(general_solution_1, t)),
                                                            (x1, general_solution_1),
                                                            self.Cs_1, self.Cs_2])
        elif self.L_x2 == self.L_x2.subs([(x1_diff, 0), (x1, 0)]):
            general_solution_2 = dsolve(self.de2).rhs
            general_solution_1 = dsolve(self.de1).rhs.subs([(x2_diff, diff(general_solution_2, t)),
                                                            (x2, general_solution_2),
                                                            self.Cs_1, self.Cs_2])
        else:
            # ToDo Два раза вызывается dsolve - исправить
            general_solution_1 = dsolve([self.de1, self.de2],
                                        [x1, x2])[0].rhs
            general_solution_2 = dsolve([self.de1, self.de2],
                                        [x1, x2])[1].rhs

        self.general_solution_1 = general_solution_1
        self.general_solution_2 = general_solution_2

    def _coefficients(self):
        # ToDo возможно инкапсулировать
        self.first_eq = self.general_solution_1.subs(t, self.t0) - self.x1_0
        self.second_eq = self.general_solution_1.subs(t, self.t1) - self.x1_1
        self.third_eq = self.general_solution_2.subs(t, self.t0) - self.x2_0
        self.fourth_eq = self.general_solution_2.subs(t, self.t1) - self.x2_1

        self.equations = [self.first_eq,
                          self.second_eq,
                          self.third_eq,
                          self.fourth_eq]

        self.params = [Multidimensional.C1,
                       Multidimensional.C2,
                       Multidimensional.C3,
                       Multidimensional.C4]

        coefficients = solve(self.equations,
                             self.params)

        self.coefficients = coefficients

    def _particular_solution(self):
        self.particular_solution_1 = self.general_solution_1.subs(self.coefficients)
        self.particular_solution_2 = self.general_solution_2.subs(self.coefficients)

    def _extreme_value(self):
        def _make_substitutions():
            self.substitutions = [(x1_diff, diff(self.particular_solution_1, t)),
                                  (x2_diff, diff(self.particular_solution_2, t)),
                                  (x1, self.particular_solution_1),
                                  (x2, self.particular_solution_2)]

        _make_substitutions()

        extreme_value = integrate(self.L.subs(self.substitutions),
                                  (t, self.t0, self.t1))
        self.extreme_value = extreme_value

    def solve(self):
        super().solve()


def main():
    from sympy import pi
    from sympy.functions import exp, log

    def solver(L, t0, t1, x1_0, x1_1, x2_0, x2_1):
        task = Multidimensional(L, t0, t1, x1_0, x1_1, x2_0, x2_1)
        task.solve()
        print('task')
        print('general_solution 1', task.general_solution_1)
        print('general_solution 2', task.general_solution_2)
        print('coefficients', task.coefficients)
        print('particular_solution_1', task.particular_solution_1)
        print('particular_solution_2', task.particular_solution_2)
        print('extreme_value', task.extreme_value)
        print()

    solver(L=x1_diff**2 + x2_diff**2,
           t0=0, t1=1,
           x1_0=0, x1_1=1,
           x2_0=0, x2_1=1)

    solver(L=x1_diff ** 2 + x2_diff ** 2,
           t0=0, t1=1,
           x1_0=0,x1_1=1,
           x2_0=1, x2_1=exp(1))

    solver(L=x2 ** 2 + x1_diff ** 2 + x2_diff ** 2,
           t0=0, t1=1,
           x1_0=0, x1_1=1,
           x2_0=1, x2_1=exp(1))

    solver(L=x1_diff * x2_diff - x1 * x2,
           t0=0, t1=pi / 2,
           x1_0=0, x1_1=1,
           x2_0=1, x2_1=0)

    solver(L=2 * x1 + x2 ** 2 + x1_diff ** 2 + x2_diff ** 2,
           t0=0, t1=1,
           x1_0=0, x1_1=0.5,
           x2_0=1, x2_1=exp(-1))

    # ToDo not solve
    # solver(L=x1_diff * x2_diff + x1 * x2,
    #        t0=0, t1=1,
    #        x1_0=0, x1_1=exp(1),
    #        x2_0=1, x2_1=exp(-1))


if __name__ == '__main__':
    main()
