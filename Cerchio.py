# This script plots, for a given centre and radius, the corresponding circle

from pylab import *
figure(figsize=(8,8))
ax=subplot(aspect='equal')

print(" Dato un punto ed un raggio, questo script disegna la circonferenza corrispondente \n")
cen_x = input(" Seleziona la X del centro \n")
cen_y = input(" Seleziona la Y del centro \n")
rad = input(" Seleziona il raggio della circonferenza \n")

#fig, ax = plt.subplots()
ax.add_patch(plt.Circle((int(cen_x), int(cen_y)), int(rad), color='r', alpha=0.5))

#Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.plot()   #Causes an autoscale update.
plt.grid(True)
plt.title('Circonferenza')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
