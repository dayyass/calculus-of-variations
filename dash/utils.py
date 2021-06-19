from typing import Dict

from sympy.core.symbol import Symbol


def print_coefficients(coefficients: Dict[Symbol, float]) -> str:
    """
    Convert dict of coefficients to ready-to-print coefficients string.

    :param Dict[Symbol, float] coefficients: dict of coefficients.
    :return: ready-to-print coefficients string.
    :rtype: str
    """

    return ", ".join([f"{k} = {v}" for k, v in coefficients.items()])
