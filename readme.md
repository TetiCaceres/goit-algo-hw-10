# Homework: Computing a Definite Integral Using the Monte Carlo Method

## Task Description
Compute the definite integral of the function \( f(x) = x^2 \) over the interval [0, 2] using the Monte Carlo method and compare the result with the analytical solution and SciPy's `quad` method.

## Algorithm
1. Define the function \( f(x) \) and the integration interval [a, b].
2. Generate N random points inside the rectangle that bounds the function's graph.
3. Count the fraction of points that lie below the curve.
4. Compute the area under the curve as the rectangle's area multiplied by the fraction of points under the curve.
5. Verify the result analytically and using `scipy.integrate.quad`.

## Results
- Integral using Monte Carlo: **approximately 2.667**  
- Analytical value: \( \int_0^2 x^2 dx = \frac{8}{3} \approx 2.6667 \)  
- SciPy `quad` result: **2.666666666666667**, error ≈ 2.96e-14

## Conclusions
- The Monte Carlo method provides a result that **matches well** with the analytical solution and `quad` method.
- The error of the method decreases as the number of random points increases.
- Thus, the algorithm is **correctly implemented** and can be used for approximate integration when analytical integration is difficult or impossible.
