import unittest
import SPCV
from sympy.functions import exp, log

from SPCV import t, x, x_diff
C1 = SPCV.SPCV.C1
C2 = SPCV.SPCV.C2

class TestSPCVBase(unittest.TestCase):

    # ToDo Why setUp yellow???
    def setUp(self, L, t0, t1, x0, x1,
              general_solution, coefficients, particular_solution, extreme_value):

        self.L = L
        self.t0 = t0
        self.t1 = t1
        self.x0 = x0
        self.x1 = x1

        self.general_solution = general_solution
        self.coefficients = coefficients
        self.particular_solution = particular_solution
        self.extreme_value = extreme_value

        self.SPCV = SPCV.SPCV(L=self.L,
                              t0=self.t0, x0=self.x0,
                              t1=self.t1, x1=self.x1)
        self.SPCV.solve()

    def test_L(self):
        self.assertEqual(self.SPCV.L,
                         self.L)

    def test_t0(self):
        self.assertEqual(self.SPCV.t0,
                         self.t0)

    def test_t1(self):
        self.assertEqual(self.SPCV.t1,
                         self.t1)

    def test_x0(self):
        self.assertEqual(self.SPCV.x0,
                         self.x0)

    def test_x1(self):
        self.assertEqual(self.SPCV.x1,
                         self.x1)

    def test_general_solution(self):
        self.assertEqual(self.SPCV.general_solution,
                         self.general_solution)

    def test_coefficients(self):
        self.assertEqual(self.SPCV.coefficients,
                         self.coefficients)

    def test_particular_solution(self):
        self.assertEqual(self.SPCV.particular_solution,
                         self.particular_solution)

    def test_extreme_value(self):
        self.assertEqual(self.SPCV.extreme_value,
                         self.extreme_value)

    def runTest(self):
        self.test_L()
        self.test_t0()
        self.test_t1()
        self.test_x0()
        self.test_x1()
        self.test_general_solution()
        self.test_coefficients()
        self.test_particular_solution()
        self.test_extreme_value()


class TestSPCV1(TestSPCVBase):

    def setUp(self):
        super().setUp(L=SPCV.x_diff ** 2,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=1,
                      general_solution=C1 + C2 * t,
                      coefficients={C1: 0,
                                    C2: 1},
                      particular_solution=t,
                      extreme_value=1)


class TestSPCV2(TestSPCVBase):

    def setUp(self):
        super().setUp(L=x_diff ** 2 + t * x,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=0,
                      general_solution=C1 + C2 * t + t ** 3 / 12,
                      coefficients={C1: 0,
                                    C2: -1 / 12},
                      particular_solution=t ** 3 / 12 - t / 12,
                      extreme_value=-1 / 180)


class TestSPCV3(TestSPCVBase):

    def setUp(self):
        super().setUp(L=t * x_diff ** 2,
                      t0=1,
                      t1=exp(1),
                      x0=0,
                      x1=1,
                      general_solution=C1 + C2 * log(t),
                      coefficients={C1: 0,
                                    C2: 1},
                      particular_solution=log(t),
                      extreme_value=1)


class TestSPCV4(TestSPCVBase):

    def setUp(self):
        super().setUp(L=x_diff ** 2 + x_diff * x + 12 * t * x,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=0,
                      general_solution=C1 + C2 * t + t ** 3,
                      coefficients={C1: 0,
                                    C2: -1},
                      particular_solution=t ** 3 - t,
                      extreme_value=-4 / 5)


class TestSPCV5(TestSPCVBase):

    def setUp(self):
        super().setUp(L=x_diff ** 2 - t ** 2 * x,
                      t0=0,
                      t1=1,
                      x0=0,
                      x1=0,
                      general_solution=C1 + C2 * t - t ** 4 / 24,
                      coefficients={C1: 0,
                                    C2: 1 / 24},
                      particular_solution=t / 24 - t ** 4 / 24,
                      extreme_value=-1 / 448)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestSPCV1(),
                    TestSPCV2(),
                    TestSPCV3(),
                    TestSPCV4(),
                    TestSPCV5()])
    runner = unittest.TextTestRunner()
    runner.run(suite)
