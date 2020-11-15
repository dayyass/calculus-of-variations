from abc import ABC, abstractmethod


class AbstractSolver(ABC):

    """
    Abstract solver for different problems in calculus of variation.
    """

    @abstractmethod
    def _general_solution(self):
        """
        Find general solution.
        """
        pass

    @abstractmethod
    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        pass

    @abstractmethod
    def _particular_solution(self):
        """
        Substitute particular solution coefficients to general solution.
        """
        pass

    @abstractmethod
    def _extrema_value(self):
        """
        Find extrema value for particular solution.
        """
        pass

    @abstractmethod
    def solve(self, verbose: bool = True):
        """
        Solve task using all encapsulated methods.
        """
        pass
