import matplotlib.pyplot as plt
import numpy as np

print(" Dato un punto ed un raggio, questo script disegna la circonferenza corrispondente \n")
cen_x1 = input(" Quel'è la X del primo fuoco? \n")
cen_y1 = input(" Quel'è la Y del primo fuoco \n")
cen_x2 = input(" Quel'è la X del secondo fuoco \n")
cen_y2 = input(" Quel'è la Y del secondo fuoco \n")
rad = input(" Qual'è la somma delle distanze dei punti dell'ellisse dai fuochi? \n")

# Example focii and sum-distance
a1 = int(cen_x1)
b1 = int(cen_y1)
a2 = int(cen_x2)
b2 = int(cen_y2)
c = int(rad)

# Compute ellipse parameters
a = c / 2                                # Semimajor axis
x0 = (a1 + a2) / 2                       # Center x-value
y0 = (b1 + b2) / 2                       # Center y-value
f = np.sqrt((a1 - x0)**2 + (b1 - y0)**2) # Distance from center to focus
b = np.sqrt(a**2 - f**2)                 # Semiminor axis
phi = np.arctan2((b2 - b1), (a2 - a1))   # Angle betw major axis and x-axis

# Parametric plot in t
resolution = 1000
t = np.linspace(0, 2*np.pi, resolution)
x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)

# Plot ellipse
plt.plot(x, y)

# Show focii
plt.plot(a1, b1, 'bo')
plt.plot(a2, b2, 'bo')

plt.axis('equal')
plt.grid(True)
plt.title('Ellisse')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
