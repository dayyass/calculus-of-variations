[![tests](https://github.com/dayyass/calculus-of-variations/actions/workflows/tests.yml/badge.svg)](https://github.com/dayyass/calculus-of-variations/actions/workflows/tests.yml)
[![linter](https://github.com/dayyass/calculus-of-variations/actions/workflows/linter.yml/badge.svg)](https://github.com/dayyass/calculus-of-variations/actions/workflows/linter.yml)
[![codecov](https://codecov.io/gh/dayyass/calculus-of-variations/branch/master/graph/badge.svg?token=H8OFWPPUOY)](https://codecov.io/gh/dayyass/calculus-of-variations)

[![python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://github.com/dayyass/calculus-of-variations#requirements)
[![release (latest by date)](https://img.shields.io/github/v/release/dayyass/calculus-of-variations)](https://github.com/dayyass/calculus-of-variations/releases/latest)
[![license](https://img.shields.io/github/license/dayyass/calculus-of-variations?color=blue)](https://github.com/dayyass/calculus-of-variations/blob/main/LICENSE)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-black)](https://github.com/dayyass/calculus-of-variations/blob/main/.pre-commit-config.yaml)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![pypi version](https://img.shields.io/pypi/v/calculus-of-variations)](https://pypi.org/project/calculus-of-variations)
[![pypi downloads](https://img.shields.io/pypi/dm/calculus-of-variations)](https://pypi.org/project/calculus-of-variations)


### About
My bachelor project on solving the **Calculus of variations** problems using symbolic mathematics (2018).

I [*participated*](https://it-mm.rea.ru/uploads/arhiv/2019/sertificat/299.pdf) with this project at the IX International Scientific and Practical Conference named after A.I. Kitov "Information Technologies and Mathematical Methods in Economics and Management" ([*link*](https://it-mm.rea.ru/eng)).<br>

My [*presentation*](presentation.pdf) about this project.

### What is Calculus of variations
According to [Wikipedia](https://en.wikipedia.org/wiki/Calculus_of_variations):<br>
The **calculus of variations** is a field of mathematical analysis that uses variations, which are small changes in functions and functionals, to find maxima and minima of functionals: mappings from a set of functions to the real numbers. Functionals are often expressed as definite integrals involving functions and their derivatives. Functions that maximize or minimize functionals may be found using the Euler–Lagrange equation of the calculus of variations.<br>

### Simplest problem
The definition above might seem quite difficult to understand, so let's consider the simplest problem:

<img src="https://render.githubusercontent.com/render/math?math=I(x) = \int_{t_0}^{t_1} L(t, x(t), \dot x(t)) dt \to extr"><br/>
<img src="https://render.githubusercontent.com/render/math?math=x(t_0) = x_0"><br/>
<img src="https://render.githubusercontent.com/render/math?math=x(t_1) = x_1"><br/>

This is the task of finding an extrema in continuously differentiable functions space
<img src="https://render.githubusercontent.com/render/math?math=C^1([t_0, t_1], \mathbb{R})">
, where:

<img src="https://render.githubusercontent.com/render/math?math=I(x): C^1([t_0, t_1], \mathbb{R}) \to \mathbb{R}"> - functional to maximize/minimize,<br/>
<img src="https://render.githubusercontent.com/render/math?math=[t_0, t_1]: t_0 < t_1"> - fixed closed line segment,<br/>
<img src="https://render.githubusercontent.com/render/math?math=x(t) \in C^1([t_0, t_1], \mathbb{R})"> - continuously differentiable function,<br/>
<img src="https://render.githubusercontent.com/render/math?math=\dot x(t) = \frac {dx}{dt})"> - function derivative,<br/>
<img src="https://render.githubusercontent.com/render/math?math=x_0, x_1 \in \mathbb{R}"> - boundary conditions.<br/>

#### Example
<img src="https://render.githubusercontent.com/render/math?math=I(x) = \int_{0}^{1} (\dot x^2 %2B tx) dt \to extr"><br/>
<img src="https://render.githubusercontent.com/render/math?math=x(0) = 0"><br/>
<img src="https://render.githubusercontent.com/render/math?math=x(1) = 0"><br/>

### Euler–Lagrange equation
Functions that maximize or minimize functionals may be found using the [*Euler–Lagrange equation*](https://en.wikipedia.org/wiki/Euler–Lagrange_equation) of the calculus of variations:

<img src="https://render.githubusercontent.com/render/math?math=L_x(t, x(t), \dot x(t)) - \frac {d}{dt}L_{\dot x}(t, x(t), \dot x(t)) = 0">, where

<img src="https://render.githubusercontent.com/render/math?math=L_x"> - partial derivative of <img src="https://render.githubusercontent.com/render/math?math=L"> w.r.t. <img src="https://render.githubusercontent.com/render/math?math=x">,<br/>
<img src="https://render.githubusercontent.com/render/math?math=L_{\dot x}"> - partial derivative of <img src="https://render.githubusercontent.com/render/math?math=L"> w.r.t. <img src="https://render.githubusercontent.com/render/math?math=\dot x">.<br/>

Arbitrary constants arising when solving this differential equation, find them from the given boundary conditions.

### List of supported problems
- [x] [*Simplest problem*](https://github.com/dayyass/calculus_of_variations/wiki/Simplest-problem)
- [x] [*Boltz problem*](https://github.com/dayyass/calculus_of_variations/wiki/Boltz-problem)
- [x] [*Isoperimetric problem*](https://github.com/dayyass/calculus_of_variations/wiki/Isoperimetric-problem)
- [x] [*Higher derivatives problem*](https://github.com/dayyass/calculus_of_variations/wiki/Higher-derivatives-problem)
- [x] [*Multidimensional problem*](https://github.com/dayyass/calculus_of_variations/wiki/Multidimensional-problem)

More about each task in [*project wiki*](https://github.com/dayyass/calculus_of_variations/wiki).

### Usage
First, install the package:
```
pip install calculus-of-variations
```

Usage for example above:
```python3
import calculus_of_variations

solver = calculus_of_variations.SimplestSolver(
    L="x_diff ** 2",
    t0="0", t1="1",
    x0="0", x1="1",
)

solver.solve()

# integral from 0 to 1 of (x_diff ** 2)dt -> extr
# x(0) = 0
# x(1) = 1

# general_solution: C1 + C2*t
# coefficients: {C1: 0, C2: 1}
# particular_solution: t
# extrema_value: 1
```

Other cases:
```python3
# Simplest problem
solver = calculus_of_variations.SimplestSolver(
    L="x_diff ** 2",
    t0="0", t1="1",
    x0="0", x1="1",
)
solver.solve()

# Boltz problem
solver = calculus_of_variations.BoltzSolver(
    L="x_diff ** 2 + 2 * x",
    l="x_t0 ** 2",
    t0="0", t1="1",
)
solver.solve()

# Isoperimetric problem
solver = calculus_of_variations.IsoperimetricSolver(
    f0="x_diff ** 2",
    t0="0", t1="1",
    x0="0", x1="1",
    f_list="x",
    alpha_list="0",
)
solver.solve()

# Higher derivatives problem
solver = calculus_of_variations.HigherDerivativesSolver(
    n="2",
    L="x_diff_2 ** 2",
    t0="0", t1="1",
    x0="0", x1="0",
    x0_array="0",
    x1_array="1",
)
solver.solve()

# Multidimensional problem
solver = calculus_of_variations.MultidimensionalSolver(
    L="x1_diff**2 + x2_diff**2",
    t0="0", t1="1",
    x1_0="0", x1_1="1",
    x2_0="0", x2_1="1",
)
solver.solve()
```

For specific examples see [**examples.sh**](https://github.com/dayyass/calculus_of_variations/blob/master/examples.sh).<br>
List of **allowed functions** that you can use as parameters: [*link*](https://github.com/dayyass/calculus_of_variations/wiki/Allowed-functions).

### Web-interface
The project supports simple web-interface for solving problems.
You can specify **host** (`--host`) and **port** (`--port`) (default values: `host: 127.0.0.1` and `port: 8050`):
```
# Simplest problem
python -m web_interface.simplest_problem_dash --host "127.0.0.1" --port 8050

# Boltz problem
python -m web_interface.boltz_problem_dash --host "127.0.0.1" --port 8050

# Isoperimetric problem
python -m web_interface.isoperimetric_problem_dash --host "127.0.0.1" --port 8050

# Higher derivatives problem
python -m web_interface.higher_derivatives_problem_dash --host "127.0.0.1" --port 8050

# Multidimensional problem
python -m web_interface.multidimensional_problem_dash --host "127.0.0.1" --port 8050
```

You can also launch web-interface using docker.<br>
To build docker image run:
```
docker image build -t calculus_of_variations .
```
You can also pull image from [Docker Hub](https://hub.docker.com/r/dayyass/calculus_of_variations):
```
docker pull dayyass/calculus_of_variations
```

To start docker container run (example for **simplest_problem_dash**):
```
docker container run -d -p 8050:8050 --name calculus_of_variations calculus_of_variations python -m web_interface.simplest_problem_dash --host 0.0.0.0 --port 8050
```
To access web-interface go to `http://localhost:8050`

### Tests
To launch [**tests**](https://github.com/dayyass/calculus_of_variations/tree/master/tests) run the following commands:<br>
`python -m unittest discover`

To use [**pre-commit**](https://pre-commit.com) hooks run:<br>
`pre-commit install`

To measure [**code coverage**](https://coverage.readthedocs.io) run the following commands:<br>
`coverage run -m unittest discover && coverage report -m`

## Requirements
Python >= 3.6

### Citation
If you use **calculus_of_variations** in a scientific publication, we would appreciate references to the following BibTex entry:
```bibtex
@misc{dayyass2018variations,
    author       = {El-Ayyass, Dani},
    title        = {Calculus of Variations problems solving using symbolic mathematics},
    howpublished = {\url{https://github.com/dayyass/calculus_of_variations}},
    year         = {2018}
}
```
