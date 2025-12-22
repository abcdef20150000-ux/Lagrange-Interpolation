# Lagrange Interpolation GUI (Python)
This project is a Python-based GUI application that implements Lagrange Interpolation
to approximate functions from discrete data points.

The application allows the user to:
- Enter a set of (x, y) data points
- Evaluate the interpolated function at a given point
- Compute the first derivative at that point
- Visualize the interpolation polynomial graphically

## Why Lagrange Interpolation?

Lagrange interpolation was chosen for this project due to its strong mathematical properties
and flexibility in numerical analysis.

Key reasons include:

- **Direct polynomial construction** without solving linear systems
- **Exact fitting** of all given data points
- **Symbolic polynomial form**, which allows:
  - Easy evaluation at any point
  - Direct computation of derivatives


### Compatibility with Newton–Raphson Method

One of the most important advantages of Lagrange interpolation is that it produces
an explicit polynomial function.

This makes it fully compatible with root-finding methods such as **Newton–Raphson**, since:
- The interpolated function is continuous and differentiable
- Its derivative can be computed analytically
- Newton–Raphson can be applied directly to the resulting polynomial

This allows the interpolation polynomial to be used not only for approximation,
but also for solving nonlinear equations numerically.

## Additional Features

- Automatic derivative computation using the interpolated polynomial
- Graphical visualization using Matplotlib
- User-friendly GUI built with Tkinter
- Dynamic table generation based on the number of input points

## Technologies Used

- Python
- NumPy
- SciPy
- Tkinter
- Matplotlib
