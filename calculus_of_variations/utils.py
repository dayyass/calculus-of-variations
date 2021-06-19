from typing import Any

from sympy import Function, diff, var

# https://docs.sympy.org/latest/modules/core.html?highlight=pi#module-sympy.core.numbers
from sympy.core.numbers import E, GoldenRatio, I, pi  # noqa: F401

# https://docs.sympy.org/latest/modules/functions/combinatorial.html#factorial
from sympy.functions.combinatorial.factorials import (  # noqa: F401
    factorial,
    factorial2,
    subfactorial,
)

# https://docs.sympy.org/latest/modules/functions/combinatorial.html
from sympy.functions.combinatorial.numbers import (  # noqa: F401
    bell,
    bernoulli,
    binomial,
    catalan,
    euler,
    fibonacci,
    stirling,
)

# https://docs.sympy.org/latest/modules/functions/elementary.html#sympy-functions-elementary-complexes
from sympy.functions.elementary.complexes import Abs, im, re, sign  # noqa: F401

# https://docs.sympy.org/latest/modules/functions/elementary.html#sympy-functions-elementary-exponential
from sympy.functions.elementary.exponential import exp, log  # noqa: F401

# https://docs.sympy.org/latest/modules/functions/elementary.html#sympy-functions-elementary-hyperbolic
from sympy.functions.elementary.hyperbolic import (  # noqa: F401
    acosh,
    acoth,
    acsch,
    asech,
    asinh,
    atanh,
    cosh,
    coth,
    csch,
    sech,
    sinh,
    tanh,
)

# https://docs.sympy.org/latest/modules/functions/elementary.html#sympy-functions-elementary-trigonometric
from sympy.functions.elementary.trigonometric import (  # noqa: F401
    acos,
    acot,
    acsc,
    asec,
    asin,
    atan,
    atan2,
    cos,
    cot,
    csc,
    sec,
    sin,
    sinc,
    tan,
)

t = var("t")
x = Function("x")(t)
x_diff = diff(x, t)

# Boltz
t0 = var("t0")
t1 = var("t1")
x_t0 = Function("x")(t0)
x_t1 = Function("x")(t1)


def sympy_eval(string) -> Any:
    """
    Eval string.
    """

    return eval(string)
