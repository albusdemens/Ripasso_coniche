# Questo script disegna un'iperbole partendo dai valori di a e b
# ATTENZIONE: il grafico funziona per valori piccoli di a e b. Per valori
# elevati, può essere necessario ridefinire gli intervalli di x e y (l 15, 16)

# Ispirato da http://blog.mmast.net/conics-matplotlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

# Per disegnare meglio la parabola, può essere necessario ridefinire gli intervalli di x e y
x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

print(" Dati due valori a e b, questo script disegna un'iperbole con fuochi sull'asse X \n Equazione dell'iperbole: x^2/a^2 + y^2/b^2 = 1 \n")
a = int(input(" Seleziona il valore di a \n"))
b = int(input(" Seleziona il valore di b \n"))

axes()
plt.contour(x, y,(x**2/a**2 - y**2/b**2), [1], colors='k', alpha=.1)
# Eccentricity.
e = np.sqrt(1 + b**2/a**2)
# Foci.
plt.plot(a*e, 0, '.', -a*e, 0, '.')
# Asymptotes.
plt.plot(x[0,:], b/a*x[0,:], '--')
plt.plot(x[0,:], -b/a*x[0,:], '--')

#plt.grid(True)
plt.title('Iperbole con fuochi su X')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
