import unittest
import Isoperimetric
from sympy import var, pi
from sympy.functions import exp, log, cos
# import SPCVUnittests

from Isoperimetric import t, x, x_diff
C1 = Isoperimetric.Isoperimetric.C1
C2 = Isoperimetric.Isoperimetric.C2
lambda_0 = Isoperimetric.Isoperimetric.lambda_0
lambda_1 = var('lambda_1')
lambda_2 = var('lambda_2')


# ToDo Think about inheritance
class TestIsoperimetricBase(unittest.TestCase):

    # ToDo Why setUp yellow???
    def setUp(self, f0, t0, t1, x0, x1, f_list, alphas,
              general_solution, coefficients, particular_solution, extreme_value):

        self.f0 = f0
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1
        self.f_list = f_list
        self.alphas = alphas

        self.general_solution = general_solution
        self.coefficients = coefficients
        self.particular_solution = particular_solution
        self.extreme_value = extreme_value

        self.Isoperimetric = Isoperimetric.Isoperimetric(f0=self.f0,
                                                         t0=self.t0,
                                                         t1=self.t1,
                                                         x0=self.x0,
                                                         x1=self.x1,
                                                         f_list=self.f_list,
                                                         alphas=self.alphas)
        self.Isoperimetric.solve()

    def test_f0(self):
        self.assertEqual(self.Isoperimetric.f0,
                         self.f0)

    def test_t0(self):
        self.assertEqual(self.Isoperimetric.t0,
                         self.t0)

    def test_t1(self):
        self.assertEqual(self.Isoperimetric.t1,
                         self.t1)

    def test_x0(self):
        self.assertEqual(self.Isoperimetric.x0,
                         self.x0)

    def test_x1(self):
        self.assertEqual(self.Isoperimetric.x1,
                         self.x1)

    def test_f_list(self):
        self.assertEqual(self.Isoperimetric.f_list,
                         self.f_list)

    def test_alphas(self):
        self.assertEqual(self.Isoperimetric.alphas,
                         self.alphas)

    def test_general_solution(self):
        self.assertEqual(self.Isoperimetric.general_solution,
                         self.general_solution)

    def test_coefficients(self):
        self.assertEqual(self.Isoperimetric.coefficients,
                         self.coefficients)

    def test_particular_solution(self):
        self.assertEqual(self.Isoperimetric.particular_solution,
                         self.particular_solution)

    def test_extreme_value(self):
        self.assertEqual(self.Isoperimetric.extreme_value,
                         self.extreme_value)

    def runTest(self):
        self.test_f0()
        self.test_t0()
        self.test_t1()
        self.test_x0()
        self.test_x1()
        self.test_f_list()
        self.test_alphas()
        self.test_general_solution()
        self.test_coefficients()
        self.test_particular_solution()
        self.test_extreme_value()


class TestIsoperimetric1(TestIsoperimetricBase):

    def setUp(self):
        super().setUp(f0=x_diff**2,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=1,
                      f_list=[x],
                      alphas=[0],
                      general_solution=C1 + C2*t + lambda_1*t**2/(4*lambda_0),
                      coefficients={C1: 0,
                                    lambda_1/lambda_0: 12,
                                    C2: -2},
                      particular_solution=3*t**2 - 2*t,
                      extreme_value=4)


class TestIsoperimetric2(TestIsoperimetricBase):

    def setUp(self):
        super().setUp(f0=x_diff**2,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=1,
                      f_list=[t * x],
                      alphas=[0],
                      general_solution=C1 + C2*t + lambda_1*t**3/(12*lambda_0),
                      coefficients={C1: 0,
                                    lambda_1/lambda_0: 30,
                                    C2: -3/2},
                      particular_solution=5*t**3/2 - 3*t/2,
                      extreme_value=6)


class TestIsoperimetric3(TestIsoperimetricBase):

    def setUp(self):
        super().setUp(f0=x_diff**2,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=0,
                      f_list=[x, t * x],
                      alphas=[1, 0],
                      general_solution=C1 + C2*t + lambda_1*t**2/(4*lambda_0) + \
                                       lambda_2*t**3/(12*lambda_0),
                      coefficients={C1: 0,
                                    lambda_2/lambda_0: 720,
                                    lambda_1/lambda_0: -384,
                                    C2: 36},
                      particular_solution=60*t**3 - 96*t**2 + 36*t,
                      extreme_value=192)


class TestIsoperimetric4(TestIsoperimetricBase):

    def setUp(self):
        super().setUp(f0=x_diff**2,
                      t0=0,
                      t1=pi,
                      x0=1,
                      x1=-1,
                      f_list=[x * cos(t)],
                      alphas=[pi / 2],
                      general_solution=C1 + C2*t - lambda_1*cos(t)/(2*lambda_0),
                      coefficients={C1: 0,
                                    lambda_1/lambda_0: -2,
                                    C2: 0},
                      particular_solution=cos(t),
                      extreme_value=pi/2)

    # ToDo May have errors
class TestIsoperimetric5(TestIsoperimetricBase):

    def setUp(self):
        super().setUp(f0=t ** 2 * x_diff ** 2,
                      t0=1,
                      t1=2,
                      x0=1,
                      x1=2,
                      f_list=[t * x],
                      alphas=[7 / 3],
                      general_solution=C1 + C2/t + lambda_1*t/(4*lambda_0),
                      coefficients={C1: 0,
                                    C2: 0,
                                    lambda_1/lambda_0: 4},
                      particular_solution=t,
                      extreme_value=7 / 3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestIsoperimetric1(),
                    TestIsoperimetric2(),
                    TestIsoperimetric3(),
                    TestIsoperimetric4(),
                    TestIsoperimetric5()])
    runner = unittest.TextTestRunner()
    runner.run(suite)
