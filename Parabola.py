import numpy as np
import matplotlib.pyplot as plt

var = input(" Che tipo di parabola vuoi disegnare?\n Premi 1 per una parabola con asse parallelo ad X, e 2 per una parabola con\n asse parallelo ad Y\n")
print("Hai selezionato " + str(var))

if int(var) == 1:
    var_a = input("Hai scelto una parabola con equazione del tipo \n x = a*y^2 + b*y + c. Scegli un valore per a\n")
    var_b = input("Un valore per b\n")
    var_c = input("Un valore per c\n")

    # creiamo una serie di valori per y, che è la nostra variabile indipendente
    y = np.linspace(-10, 10, 1000)

    # calculate the x value for each element of the y vector
    x = int(var_a)*(y**2) + int(var_b)*y + int(var_c)

    # Disegniamo la parabola
    fig, ax = plt.subplots()
    ax.plot(y,x)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

if int(var) == 2:
