import numpy as np
import matplotlib.pyplot as plt

print(" Disegnamo una retta del tipo y = mx+q. Per farlo, selezioniamo due punti \n per cui passa la retta \n")
var_x1 = input(" Seleziona la X del primo punto \n")
var_y1 = input(" Seleziona la Y del primo punto \n")
var_x2 = input(" Seleziona la X del secondo punto \n")
var_y2 = input(" Seleziona la Y del secondo punto \n")

var = input(" Che tipo di parabola vuoi disegnare?\n Premi 1 per una parabola con asse parallelo ad X, e 2 per una parabola con\n asse parallelo ad Y\n")
print("Hai selezionato " + str(var))

if int(var) == 1:
    var_a = input("Hai scelto una parabola con equazione del tipo \n x = a*y^2 + b*y + c. Scegli un valore per a: \n")
    var_b = input("Un valore per b: \n")
    var_c = input("Un valore per c: \n")

    # creiamo una serie di valori per y, che è la nostra variabile indipendente
    y = np.linspace(-10, 10, 1000)

    # calculate the x value for each element of the y vector
    x = int(var_a)*(y**2) + int(var_b)*y + int(var_c)

    # Disegniamo la parabola
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.title('Parabola con asse parallelo ad X')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Disegniamo il segmento passante per i due punti selezionati
    plt.plot([int(var_x1), int(var_x2)], [int(var_y1), int(var_y2)])

    plt.show()

if int(var) == 2:
    var_a = input("Hai scelto una parabola con equazione del tipo \n y = a*x^2 + bx + c. Scegli un valore per a: \n")
    var_b = input("Un valore per b: \n")
    var_c = input("Un valore per c: \n")

    # Creiamo una serie di valori per x, che è la nosra variabile indipendente
    x = np.linspace(-10, 10, 1000)

    # Calcoliamo il valore di y per ogni elemento del vettore x
    y = int(var_a)*(x**2) + int(var_b)*x + int(var_c)

    # Disegnamo la parabola
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.title('Parabola con asse parallelo ad Y')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Disegniamo il segmento passante per i due punti selezionati
    plt.plot([int(var_x1), int(var_x2)], [int(var_y1), int(var_y2)])

    # Uncommento to plot F, V and d
    # plt.scatter(-0.5, -3.25, facecolor="b", marker="o")
    # plt.scatter(-0.5, -2.25, facecolor="b", marker="o")
    # plt.axhline(y=-4.25, color='r', linestyle='-')

    plt.grid(True)
    plt.show()
