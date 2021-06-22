[![tests](https://github.com/dayyass/calculus_of_variations/actions/workflows/tests.yml/badge.svg)](https://github.com/dayyass/calculus_of_variations/actions/workflows/tests.yml)
[![linter](https://github.com/dayyass/calculus_of_variations/actions/workflows/linter.yml/badge.svg)](https://github.com/dayyass/calculus_of_variations/actions/workflows/linter.yml)
[![codecov](https://codecov.io/gh/dayyass/calculus_of_variations/branch/master/graph/badge.svg?token=H8OFWPPUOY)](https://codecov.io/gh/dayyass/calculus_of_variations)
[![license](https://img.shields.io/github/license/dayyass/calculus_of_variations)](LICENSE)
[![release (latest by date)](https://img.shields.io/github/v/release/dayyass/calculus_of_variations)](https://github.com/dayyass/calculus_of_variations/releases/latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](.pre-commit-config.yaml)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
First, install dependencies:
```
# clone repo (https/ssh)
git clone https://github.com/dayyass/calculus_of_variations.git
# git clone git@github.com:dayyass/calculus_of_variations.git

# install dependencies (preferable in venv)
cd calculus_of_variations
pip install -r requirements.txt
```

Usage for example above:
```
python calculus_of_variations/simplest_problem.py -L "x_diff ** 2" -t0 "0" -t1 "1" -x0 "0" -x1 "1"
```

General cases:
```
# Simplest problem
python calculus_of_variations/simplest_problem.py -L {str} -t0 {str} -t1 {str} -x0 {str} -x1 {str}

# Boltz problem
python calculus_of_variations/boltz_problem.py -L {str} -l {str} -t0 {str} -t1 {str}

# Isoperimetric problem
python calculus_of_variations/isoperimetric_problem.py -f0 {str} -t0 {str} -t1 {str} -x0 {str} -x1 {str} -f_list "{str_1}, {str_2}, ..." -alpha_list "{str_1}, {str_2}, ..."

# Higher derivatives problem
python calculus_of_variations/higher_derivatives_problem.py -n {str} -L {str} -t0 {str} -t1 {str} -x0 {str} -x1 {str} -x0_array "{str_1}, {str_2}, ..." -x1_array "{str_1}, {str_2}, ..."

# Multidimensional problem
python calculus_of_variations/multidimensional_problem.py -L {str} -t0 {str} -t1 {str} -x1_0 {str} -x1_1 {str} -x2_0 {str} -x2_1 {str}
```

For specific examples see [**examples.sh**](examples.sh).
List of [*allowed functions*](https://github.com/dayyass/calculus_of_variations/wiki/Allowed-functions) that you can use ass parameters.

### Web-interface
The project supports simple web-interface for solving problems.
You can specify *host* (*--host*) and *port* (*--port*) (default values: `host: 127.0.0.1` and `port: 8050`):
```
# Simplest problem
python web_interface/simplest_problem_dash.py --host "127.0.0.1" --port 8050

# Boltz problem
python web_interface/boltz_problem_dash.py --host "127.0.0.1" --port 8050

# Isoperimetric problem
python web_interface/isoperimetric_problem_dash.py --host "127.0.0.1" --port 8050

# Higher derivatives problem
python web_interface/higher_derivatives_problem_dash.py --host "127.0.0.1" --port 8050

# Multidimensional problem
python web_interface/multidimensional_problem_dash.py --host "127.0.0.1" --port 8050
```

### Tests
To launch [**tests**](tests) run one of the following commands:<br>
`pytest` or `python -m unittest discover`

To use [**pre-commit**](https://pre-commit.com) hooks run:<br>
`pre-commit install`

To measure [**code coverage**](https://coverage.readthedocs.io) run one of the following commands:<br>
`coverage run -m pytest && coverage report -m` or `coverage run -m unittest discover && coverage report -m`

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
