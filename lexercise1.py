import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([1, 0, -1, 2], dtype=float)

# Sistema linear Ax = b
A = np.array([
    [0**3, 0**2, 0, 1],
    [1**3, 1**2, 1, 1],
    [2**3, 2**2, 2, 1],
    [3**3, 3**2, 3, 1]
], dtype=float)

coef = np.linalg.solve(A, y)

print(np.linalg.solve(A, y))
a, b, c, d = coef

print("Coeficientes:", coef)
print("A =\n", A)
print("y =", y)
print("coef =", coef)

xx = np.linspace(-1, 4, 100)
yy = a*xx**3 + b*xx**2 + c*xx + d


plt.scatter(x, y)
plt.plot(xx, yy)
plt.title("Polinômio interpolador")
plt.show()