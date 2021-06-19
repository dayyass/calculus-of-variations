import sys
import unittest

from parameterized import parameterized_class

# TODO: fix it
sys.path.append("./")
from calculus_of_variations import MultidimensionalSolver
from calculus_of_variations.utils import I, exp, t

C1 = MultidimensionalSolver.C1
C2 = MultidimensionalSolver.C2
C3 = MultidimensionalSolver.C3
C4 = MultidimensionalSolver.C4


def make_solution(L: str, t0: str, t1: str, x1_0: str, x1_1: str, x2_0: str, x2_1: str):
    solution = MultidimensionalSolver(
        L=L, t0=t0, t1=t1, x1_0=x1_0, x1_1=x1_1, x2_0=x2_0, x2_1=x2_1
    )
    solution.solve(verbose=False)
    return solution


test_case_1 = {
    "solution": make_solution(
        L="x1_diff**2 + x2_diff**2",
        t0="0",
        t1="1",
        x1_0="0",
        x1_1="1",
        x2_0="0",
        x2_1="1",
    ),
    "general_solution_1": C1 + C2 * t,
    "general_solution_2": C3 + C4 * t,
    "coefficients": {C1: 0, C2: 1, C3: 0, C4: 1},
    "particular_solution_1": t,
    "particular_solution_2": t,
    "extrema_value": 2,
}
test_case_2 = {
    "solution": make_solution(
        L="x1_diff ** 2 + x2_diff ** 2",
        t0="0",
        t1="1",
        x1_0="0",
        x1_1="1",
        x2_0="1",
        x2_1="E",
    ),
    "general_solution_1": C1 + C2 * t,
    "general_solution_2": C3 + C4 * t,
    "coefficients": {C1: 0, C2: 1, C3: 1, C4: exp(1) - 1},
    "particular_solution_1": t,
    "particular_solution_2": t * (exp(1) - 1) + 1,
    "extrema_value": 1 + (exp(1) - 1) ** 2,
}
test_case_3 = {
    "solution": make_solution(
        L="x2 ** 2 + x1_diff ** 2 + x2_diff ** 2",
        t0="0",
        t1="1",
        x1_0="0",
        x1_1="1",
        x2_0="1",
        x2_1="E",
    ),
    "general_solution_1": C1 + C2 * t,
    "general_solution_2": C3 * exp(-t) + C4 * exp(t),
    "coefficients": {C1: 0, C2: 1, C3: 0, C4: 1},
    "particular_solution_1": t,
    "particular_solution_2": exp(t),
    "extrema_value": exp(2),
}
test_case_4 = {
    "solution": make_solution(
        L="x1_diff * x2_diff - x1 * x2",
        t0="0",
        t1="pi / 2",
        x1_0="0",
        x1_1="1",
        x2_0="1",
        x2_1="0",
    ),
    "general_solution_1": 2 * I * C1 * exp(I * t) + 2 * I * C2 * exp(-I * t),
    "general_solution_2": C3 * exp(I * t) + C4 * exp(-I * t),
    "coefficients": {C1: -1 / 4, C2: 1 / 4, C3: 1 / 2, C4: 1 / 2},
    "particular_solution_1": -I * exp(I * t) / 2 + I * exp(-I * t) / 2,
    "particular_solution_2": exp(I * t) / 2 + exp(-I * t) / 2,
    "extrema_value": -1,
}
test_case_5 = {
    "solution": make_solution(
        L="2 * x1 + x2 ** 2 + x1_diff ** 2 + x2_diff ** 2",
        t0="0",
        t1="1",
        x1_0="0",
        x1_1="0.5",
        x2_0="1",
        x2_1="exp(-1)",
    ),
    "general_solution_1": C1 + C2 * t + t ** 2 / 2,
    "general_solution_2": C3 * exp(-t) + C4 * exp(t),
    "coefficients": {C1: 0, C2: 0, C3: 1, C4: 0},
    "particular_solution_1": t ** 2 / 2,
    "particular_solution_2": exp(-t),
    "extrema_value": 5 / 3 - exp(-2),
}


@parameterized_class([test_case_1, test_case_2, test_case_3, test_case_4, test_case_5])
class TestSolver(unittest.TestCase):
    def test_general_solution_1(self):
        self.assertAlmostEqual(
            self.solution.general_solution_1, self.general_solution_1
        )

    def test_general_solution_2(self):
        self.assertAlmostEqual(
            self.solution.general_solution_2, self.general_solution_2
        )

    def test_coefficients(self):
        for coef in self.coefficients.keys():
            self.assertAlmostEqual(
                self.solution.coefficients[coef], self.coefficients[coef]
            )

    def test_particular_solution_1(self):
        self.assertAlmostEqual(
            self.solution.particular_solution_1, self.particular_solution_1
        )

    def test_particular_solution_2(self):
        self.assertAlmostEqual(
            self.solution.particular_solution_2, self.particular_solution_2
        )

    def test_extrema_value(self):
        self.assertAlmostEqual(self.solution.extrema_value, self.extrema_value)


if __name__ == "__main__":
    unittest.main()
