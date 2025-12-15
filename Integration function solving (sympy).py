# CLCODING
# Integral of a Trigonometric function

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define a trigonometric function
g = sp.sin(x)

# Compute the indefinite integral
G = sp.integrate(g, x)

# Display the result
print("∫ sin(x) dx =", G)
