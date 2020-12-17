import unittest
from typing import List

from parameterized import parameterized_class
from sympy import var

from calculus_of_variations.higher_derivatives_problem import HigherDerivativesSolver, t

Cs = {}
for i in range(1, 9):
    Cs[i] = var("C{}".format(i))


def make_solution(
    n: int,
    L: str,
    t0: float,
    t1: float,
    x0: float,
    x1: float,
    x0_array: List[float],
    x1_array: List[float],
):
    solution = HigherDerivativesSolver(n, L, t0, t1, x0, x1, x0_array, x1_array)
    solution.solve(verbose=False)
    return solution


test_case_1 = {
    "solution": make_solution(
        n=2, L="x_diff_2 ** 2", t0=0, t1=1, x0=0, x1=0, x0_array=[0], x1_array=[1]
    ),
    "general_solution": Cs[1] + Cs[2] * t + Cs[3] * t ** 2 + Cs[4] * t ** 3,
    "coefficients": {Cs[1]: 0, Cs[2]: 0, Cs[3]: -1, Cs[4]: 1},
    "particular_solution": t ** 3 - t ** 2,
    "extrema_value": 4,
}
test_case_2 = {
    "solution": make_solution(
        n=2,
        L="x_diff_2 ** 2 - 48 * x",
        t0=0,
        t1=1,
        x0=1,
        x1=0,
        x0_array=[-4],
        x1_array=[0],
    ),
    "general_solution": Cs[1] + Cs[2] * t + Cs[3] * t ** 2 + Cs[4] * t ** 3 + t ** 4,
    "coefficients": {Cs[1]: 1, Cs[2]: -4, Cs[3]: 6, Cs[4]: -4},
    "particular_solution": t ** 4 - 4 * t ** 3 + 6 * t ** 2 - 4 * t + 1,
    "extrema_value": 96 / 5,
}
test_case_3 = {
    "solution": make_solution(
        n=3, L="x_diff_3 ** 2", t0=0, t1=1, x0=0, x1=1, x0_array=[0, 0], x1_array=[3, 6]
    ),
    "general_solution": Cs[1]
    + Cs[2] * t
    + Cs[3] * t ** 2
    + Cs[4] * t ** 3
    + Cs[5] * t ** 4
    + Cs[6] * t ** 5,
    "coefficients": {Cs[1]: 0, Cs[2]: 0, Cs[3]: 0, Cs[4]: 1, Cs[5]: 0, Cs[6]: 0},
    "particular_solution": t ** 3,
    "extrema_value": 36,
}
test_case_4 = {
    "solution": make_solution(
        n=4,
        L="x_diff_4 ** 2",
        t0=0,
        t1=1,
        x0=0,
        x1=1,
        x0_array=[0, 0, 0],
        x1_array=[3, 6, 10],
    ),
    "general_solution": Cs[1]
    + Cs[2] * t
    + Cs[3] * t ** 2
    + Cs[4] * t ** 3
    + Cs[5] * t ** 4
    + Cs[6] * t ** 5
    + Cs[7] * t ** 6
    + Cs[8] * t ** 7,
    "coefficients": {
        Cs[1]: 0,
        Cs[2]: 0,
        Cs[3]: 0,
        Cs[4]: 0,
        Cs[5]: 10 / 3,
        Cs[6]: -4,
        Cs[7]: 2,
        Cs[8]: -1 / 3,
    },
    "particular_solution": -(t ** 7) / 3 + 2 * t ** 6 - 4 * t ** 5 + 10 / 3 * t ** 4,
    "extrema_value": 640,
}


@parameterized_class([test_case_1, test_case_2, test_case_3, test_case_4])
class TestSolver(unittest.TestCase):
    def test_general_solution(self):
        self.assertAlmostEqual(self.solution.general_solution, self.general_solution)

    def test_coefficients(self):
        for coef in self.coefficients.keys():
            self.assertAlmostEqual(
                self.solution.coefficients[coef], self.coefficients[coef]
            )

    def test_particular_solution(self):
        self.assertAlmostEqual(
            self.solution.particular_solution, self.particular_solution
        )

    def test_extrema_value(self):
        self.assertAlmostEqual(self.solution.extrema_value, self.extrema_value)


if __name__ == "__main__":
    unittest.main()
