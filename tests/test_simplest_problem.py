import unittest

from parameterized import parameterized_class

from src.calculus_of_variations import SimplestSolver
from src.calculus_of_variations.utils import log, t

C1 = SimplestSolver.C1
C2 = SimplestSolver.C2


def make_solution(L: str, t0: str, t1: str, x0: str, x1: str):
    solution = SimplestSolver(L=L, t0=t0, t1=t1, x0=x0, x1=x1)
    solution.solve(verbose=False)
    return solution


test_case_1 = {
    "solution": make_solution(L="x_diff ** 2", t0="0", t1="1", x0="0", x1="1"),
    "general_solution": C1 + C2 * t,
    "coefficients": {C1: 0, C2: 1},
    "particular_solution": t,
    "extrema_value": 1,
}
test_case_2 = {
    "solution": make_solution(L="x_diff ** 2 + t * x", t0="0", t1="1", x0="0", x1="0"),
    "general_solution": C1 + C2 * t + t ** 3 / 12,
    "coefficients": {C1: 0, C2: -1 / 12},
    "particular_solution": t ** 3 / 12 - t / 12,
    "extrema_value": -1 / 180,
}
test_case_3 = {
    "solution": make_solution(L="t * x_diff ** 2", t0="1", t1="E", x0="0", x1="1"),
    "general_solution": C1 + C2 * log(t),
    "coefficients": {C1: 0, C2: 1},
    "particular_solution": log(t),
    "extrema_value": 1,
}
test_case_4 = {
    "solution": make_solution(
        L="x_diff ** 2 + x_diff * x + 12 * t * x", t0="0", t1="1", x0="0", x1="0"
    ),
    "general_solution": C1 + C2 * t + t ** 3,
    "coefficients": {C1: 0, C2: -1},
    "particular_solution": t ** 3 - t,
    "extrema_value": -4 / 5,
}
test_case_5 = {
    "solution": make_solution(
        L="x_diff ** 2 - t ** 2 * x", t0="0", t1="1", x0="0", x1="0"
    ),
    "general_solution": C1 + C2 * t - t ** 4 / 24,
    "coefficients": {C1: 0, C2: 1 / 24},
    "particular_solution": t / 24 - t ** 4 / 24,
    "extrema_value": -1 / 448,
}


@parameterized_class([test_case_1, test_case_2, test_case_3, test_case_4, test_case_5])
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
