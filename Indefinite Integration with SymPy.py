import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define the function
f = sp.sin(x) + x**2

# Compute the indefinite integral
indef_integral = sp.integrate(f, x)

# Display results
print("f(x) =", f)
print("∫f(x) dx =", indef_integral)
# Output:
# f(x) = sin(x) + x**2