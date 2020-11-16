### About
My bachelor project on solving the *Calculus of variations* problems using symbolic mathematics.

I [participated](https://it-mm.rea.ru/uploads/arhiv/2019/sertificat/299.pdf) with this project at the IX International Scientific and Practical Conference named after A.I. Kitov "Information Technologies and Mathematical Methods in Economics and Management".
More about conference [here](https://it-mm.rea.ru/eng).

### What is *Calculus of variations*
According to Wikipedia:

The **calculus of variations** is a field of mathematical analysis that uses variations, which are small changes in functions and functionals, to find maxima and minima of functionals: mappings from a set of functions to the real numbers. Functionals are often expressed as definite integrals involving functions and their derivatives. Functions that maximize or minimize functionals may be found using the Euler–Lagrange equation of the calculus of variations.

More about it [here](https://en.wikipedia.org/wiki/Calculus_of_variations).

### Simplest problem
The definition above might seem quite difficult to understend so let's consider the simplest problem:

<img src="https://render.githubusercontent.com/render/math?math=I(x) = \int_{t_0}^{t_1} L(t, x(t), \dot x(t)) dt \to extr">
<img src="https://render.githubusercontent.com/render/math?math=x(t_0) = x_0">
<img src="https://render.githubusercontent.com/render/math?math=x(t_1) = x_1">

This is the task of findinig an extrema in continuously differentiable functions space
<img src="https://render.githubusercontent.com/render/math?math=C^1([t_0, t_1], \mathbb{R})">
, where:

<img src="https://render.githubusercontent.com/render/math?math=I(x): C^1([t_0, t_1], \mathbb{R}) \to \mathbb{R}"> - functional to maximize/minimize,

<img src="https://render.githubusercontent.com/render/math?math=[t_0, t_1]: t_0 < t_1"> - fixed closed line segment,

<img src="https://render.githubusercontent.com/render/math?math=x(t) \in C^1([t_0, t_1], \mathbb{R})"> - continuously differentiable function,

<img src="https://render.githubusercontent.com/render/math?math=\dot x(t) = \frac {dx}{dt})"> - function derivative,

<img src="https://render.githubusercontent.com/render/math?math=x_0, x_1 \in \mathbb{R}"> - boundary conditions.

#### Example
<img src="https://render.githubusercontent.com/render/math?math=I(x) = \int_{0}^{1} (\dot x^2 %2B tx) dt \to extr">
<img src="https://render.githubusercontent.com/render/math?math=x(0) = 0">
<img src="https://render.githubusercontent.com/render/math?math=x(1) = 0">

### Euler–Lagrange equation
Functions that maximize or minimize functionals may be found using the [Euler–Lagrange equation](https://en.wikipedia.org/wiki/Euler–Lagrange_equation) of the calculus of variations:

<img src="https://render.githubusercontent.com/render/math?math=L_x(t, x(t), \dot x(t)) - \frac {d}{dt}L_{\dot x}(t, x(t), \dot x(t)) = 0">, where

<img src="https://render.githubusercontent.com/render/math?math=L_x"> - partial derivative of <img src="https://render.githubusercontent.com/render/math?math=L"> w.r.t. <img src="https://render.githubusercontent.com/render/math?math=x">,

<img src="https://render.githubusercontent.com/render/math?math=L_{\dot x}"> - partial derivative of <img src="https://render.githubusercontent.com/render/math?math=L"> w.r.t. <img src="https://render.githubusercontent.com/render/math?math=\dot x">.

Arbitrary constants arising when solving this differential equation, find from the given boundary conditions.

### List of supported problems
- [x] [Simplest problem](https://github.com/dayyass/calculus_of_variations/wiki/Simplest-problem)
- [x] [Boltz problem](https://github.com/dayyass/calculus_of_variations/wiki/Boltz-problem)
- [x] [Isoperimetric problem](https://github.com/dayyass/calculus_of_variations/wiki/Isoperimetric-problem)
- [x] [Higher derivatives problem](https://github.com/dayyass/calculus_of_variations/wiki/Higher-derivatives-problem)
- [x] [Multidimensional problem](https://github.com/dayyass/calculus_of_variations/wiki/Multidimensional-problem)

### Usage
```
# Simplest problem
python calculus_of_variations/simplest_problem.py -L {str} -t0 {float} -t1 {float} -x0 {float} -x1 {float}

# Boltz problem
python calculus_of_variations/boltz_problem.py -L {str} -l {str} -t0 {float} -t1 {float}

# Isoperimetric problem
python calculus_of_variations/isoperimetric_problem.py -f0 {str} -t0 {float} -t1 {float} -x0 {float} -x1 {float} -f_list {str_1} {str_2} ... -alpha_list {float_1} {float_2} ...

# Higher derivatives problem
python calculus_of_variations/higher_derivatives_problem.py -n {int} -L {str} -t0 {float} -t1 {float} -x0 {float} -x1 {float} -x0_array {float_1} {float_2} ... -x1_array {float_1} {float_2} ...

# Multidimensional problem
python calculus_of_variations/multidimensional_problem.py -L {str} -t0 {float} -t1 {float} -x1_0 {float} -x1_1 {float} -x2_0 {float} -x2_1 {float}
```
