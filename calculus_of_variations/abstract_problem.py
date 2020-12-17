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
        self.general_solution = None

    @abstractmethod
    def _coefficients(self):
        """
        Find particular solution coefficients.
        """
        self.coefficients = None

    @abstractmethod
    def _particular_solution(self):
        """
        Substitute particular solution coefficients to general solution.
        """
        particular_solution = self.general_solution.subs(self.coefficients)
        self.particular_solution = particular_solution

    @abstractmethod
    def _extrema_value(self):
        """
        Find extrema value for particular solution.
        """
        self.extrema_value = None

    @abstractmethod
    def solve(self, verbose: bool = True):
        """
        Solve task using all encapsulated methods.
        """
        self._general_solution()
        self._coefficients()
        self._particular_solution()
        self._extrema_value()

        if verbose:
            print(self)
            print(f"general_solution: {self.general_solution}")
            print(f"coefficients: {self.coefficients}")
            print(f"particular_solution: {self.particular_solution}")
            print(f"extrema_value: {self.extrema_value}")
            print()
