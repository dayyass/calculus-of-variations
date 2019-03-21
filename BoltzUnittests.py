import unittest
import Boltz
from sympy.functions import exp, log
# import SPCVUnittests

from Boltz import t, x, x_diff, x_t0, x_t1
C1 = Boltz.Boltz.C1
C2 = Boltz.Boltz.C2

# ToDo Think about inheritance
class TestBoltzBase(unittest.TestCase):

    # ToDo Why setUp yellow???
    def setUp(self, L, l, t0, t1,
              general_solution, coefficients, particular_solution, extreme_value):

        self.L = L
        self.l = l
        self.t0 = t0
        self.t1 = t1

        self.general_solution = general_solution
        self.coefficients = coefficients
        self.particular_solution = particular_solution
        self.extreme_value = extreme_value

        self.Boltz = Boltz.Boltz(L=self.L, l=self.l,
                                 t0=self.t0, t1=self.t1)
        self.Boltz.solve()

    def test_L(self):
        self.assertEqual(self.Boltz.L,
                         self.L)

    def test_l(self):
        self.assertEqual(self.Boltz.l,
                         self.l)

    def test_t0(self):
        self.assertEqual(self.Boltz.t0,
                         self.t0)

    def test_t1(self):
        self.assertEqual(self.Boltz.t1,
                         self.t1)

    def test_general_solution(self):
        self.assertEqual(self.Boltz.general_solution,
                         self.general_solution)

    def test_coefficients(self):
        self.assertEqual(self.Boltz.coefficients,
                         self.coefficients)

    def test_particular_solution(self):
        self.assertEqual(self.Boltz.particular_solution,
                         self.particular_solution)

    def test_extreme_value(self):
        self.assertEqual(self.Boltz.extreme_value,
                         self.extreme_value)

    def runTest(self):
        self.test_L()
        self.test_l()
        self.test_t0()
        self.test_t1()
        self.test_general_solution()
        self.test_coefficients()
        self.test_particular_solution()
        self.test_extreme_value()


class TestBoltz1(TestBoltzBase):

    def setUp(self):
        super().setUp(L=x_diff ** 2 + 2 * x,
                      l=x_t0 ** 2,
                      t0=0,
                      t1=1,
                      general_solution=C1 + C2 * t + t ** 2 / 2,
                      coefficients={C1: -1,
                                    C2: -1},
                      particular_solution=t ** 2 / 2 - t - 1,
                      extreme_value=-4 / 3)


class TestBoltz2(TestBoltzBase):

    def setUp(self):
        super().setUp(L=x_diff ** 2 - x,
                      l=-x_t1 ** 2 / 2,
                      t0=0,
                      t1=1,
                      general_solution=C1 + C2 * t - t ** 2 / 4,
                      coefficients={C1: -3 / 4,
                                    C2: 0},
                      particular_solution=-t ** 2 / 4 - 3 / 4,
                      extreme_value=5 / 12)


class TestBoltz3(TestBoltzBase):

    def setUp(self):
        super().setUp(L=t**2 * x_diff**2,
                      l=-2*x_t0 + x_t1**2,
                      t0=1,
                      t1=2,
                      general_solution=C1 + C2/t,
                      coefficients={C1: 1/2,
                                    C2: 1},
                      particular_solution=1/2 + 1/t,
                      extreme_value=-3/2)


class TestBoltz4(TestBoltzBase):

    def setUp(self):
        super().setUp(L=2*(t*x_diff**2 + x_diff*x),
                      l=3*x_t0**2 - x_t1**2 - 4*x_t1,
                      t0=1,
                      t1=exp(1),
                      general_solution=C1 + C2*log(t),
                      coefficients={C1: 1,
                                    C2: 1},
                      particular_solution=log(t) + 1,
                      extreme_value=-4)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestBoltz1(),
                    TestBoltz2(),
                    TestBoltz3(),
                    TestBoltz4()])
    runner = unittest.TextTestRunner()
    runner.run(suite)
