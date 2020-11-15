### About
My bachelor project on solving the *Calculus of variations* problems using symbolic differentiation and integration.

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
