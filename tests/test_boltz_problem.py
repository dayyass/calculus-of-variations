import sys
import unittest

from parameterized import parameterized_class

# TODO: fix it
sys.path.append("./")
from calculus_of_variations.boltz_problem import BoltzSolver
from calculus_of_variations.utils import log, sympy_eval, t

C1 = BoltzSolver.C1
C2 = BoltzSolver.C2


def make_solution(L: str, l: str, t0: str, t1: str):
    solution = BoltzSolver(
        L=L,
        l=l,
        t0=sympy_eval(t0),
        t1=sympy_eval(t1),
    )
    solution.solve(verbose=False)
    return solution


test_case_1 = {
    "solution": make_solution(L="x_diff ** 2 + 2 * x", l="x_t0 ** 2", t0="0", t1="1"),
    "general_solution": C1 + C2 * t + t ** 2 / 2,
    "coefficients": {C1: -1, C2: -1},
    "particular_solution": t ** 2 / 2 - t - 1,
    "extrema_value": -4 / 3,
}
test_case_2 = {
    "solution": make_solution(L="x_diff ** 2 - x", l="-x_t1 ** 2 / 2", t0="0", t1="1"),
    "general_solution": C1 + C2 * t - t ** 2 / 4,
    "coefficients": {C1: -3 / 4, C2: 0},
    "particular_solution": -(t ** 2) / 4 - 3 / 4,
    "extrema_value": 5 / 12,
}
test_case_3 = {
    "solution": make_solution(
        L="t ** 2 * x_diff ** 2", l="-2 * x_t0 + x_t1 ** 2", t0="1", t1="2"
    ),
    "general_solution": C1 + C2 / t,
    "coefficients": {C1: 1 / 2, C2: 1},
    "particular_solution": 1 / 2 + 1 / t,
    "extrema_value": -3 / 2,
}
test_case_4 = {
    "solution": make_solution(
        L="2 * (t * x_diff ** 2 + x_diff * x)",
        l="3 * x_t0 ** 2 - x_t1 ** 2 - 4 * x_t1",
        t0="1",
        t1="exp(1)",
    ),
    "general_solution": C1 + C2 * log(t),
    "coefficients": {C1: 1, C2: 1},
    "particular_solution": log(t) + 1,
    "extrema_value": -4,
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
