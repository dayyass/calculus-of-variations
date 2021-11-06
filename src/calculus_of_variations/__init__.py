from .boltz_problem import BoltzSolver
from .higher_derivatives_problem import HigherDerivativesSolver
from .isoperimetric_problem import IsoperimetricSolver
from .multidimensional_problem import MultidimensionalSolver
from .simplest_problem import SimplestSolver

__version__ = "0.3.0"

__all__ = [
    "SimplestSolver",
    "BoltzSolver",
    "IsoperimetricSolver",
    "HigherDerivativesSolver",
    "MultidimensionalSolver",
]
