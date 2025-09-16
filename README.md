# Compare different quadrature rules for integration

There are two examples provided for calculating the weights and abscissas for gaussian quadrature rules, try:

```
make
./gqconstants
```

or

```
python gqconstants.py
```

You can also use the C++ example as a guide to build your own executable

There is no need to look at rules >~25 for Gaussian quadrature.  And you can also stop at ~ 1000 divisions for the trapezoidal and Simpson's rules.  If you run much longer you'll see the numerical errors bevome visible for the trapezoidal, but hyou'll need to think about how to code efficiently or the running time may be very long.

Answers: 

My code can be seen in compare.py with functions for simpson, gaussian, and trapezoid methods. Generates Errors.png. 

The slope of the trapezoidal method on the log-log plot is around -2, and the slope of Simpson's method is arount -4. 
The number of digits of precision for trapezoid is around 1 for N < 10, around 5 for N ~ 100, and around 7 for N ~ 1000. There did not appear to be a round off regime, as the slope continued for the entire graph. 
The number of digits of precision for Simpson's is around 3 for N < 10, around 10 for N ~ 100, and around 14 for N ~ 1000. There did not appear to be a round off regime, as the slope continued for the entire graph. 

The gaussian method reached machine precision with only 5 steps, and the error shot up very quickly starting with N ~ 50. 

For a function that 'breaks' the integration methods, the best I could formulate was f(x) = e^-5xsin(50pix). I chose this because of three things, an analytically solveable integral value, the exponential decay, and the oscillatory nature.
The rapid oscillation combined with the exponential decay made it very difficult for the integration methods to approximate the integral. The integration methods try and approximate a smooth function, and thus aren't prepared for the rapid oscillation.
The value of the integral is also somewhat close to zero, and so is more sensitive to small errors. 

Some ways to better approximate this bad function: 
 - Much higher N value for trapezoid and Simpson's. Computationally expensive but will pick up more oscillations. 
 - Could potentially introduce a change of variable that makes the function more easily integrated. (integral of f(x(y)) * dx/dy * dy)