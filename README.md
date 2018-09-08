# Ripasso sulle coniche

##### Filippo Tonietto & Alberto Cereser

Le coniche sono quattro curve determinate dall'intersezione di un piano con un un cono. In questo modulo verranno presentate parabola, ellisse, circonferenza ed iperbole sia da un punto di vista teorico che tramite esercizi e grafici.

### Risoluzione di un'equazione di secondo grado

Forma canonica dell'equazione di secondo grado:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?ax%5E2%2Bbx%2Bc%3D0">
</p>

*Perchè ci serve?* Il *discriminante* di un'equazione di secondo grado (che si indica con la lettera greca maiuscola *delta*), ci permette di distinguere se l'equazione di secondo grado data ha o meno soluzioni e, in caso affermativo, di riconoscere se esse sono distinte o coincidenti. La formula del discriminante è:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5CDelta%3D%5Csqrt%7Bb%5E2-4ac%7D">
</p>

Una volta calcolato il valore del discriminante, dobbiamo distinguere tre casi:
  1. <img src="https://latex.codecogs.com/svg.latex?%5CDelta%3D%5Csqrt%7Bb%5E2-4ac%7D%3E0">.
    In questo caso la radice quadrata esiste, dunque l'equazione di secondo grado ha *due soluzioni distinte*:
    <p align="center">
      <img src="https://latex.codecogs.com/svg.latex?x_%7B1%2C2%7D%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D">
  </p>

  2. <img src="https://latex.codecogs.com/svg.latex?%5CDelta%3Db%5E2-4ac%3D0">.
    In questo caso, la radice quadrata del discriminante è uguale a zero, e l'equazione di secondo grado avrà *due soluzioni coincidenti*:
    <p align="center">
      <img src="https://latex.codecogs.com/svg.latex?x_%7B1%7D%3Dx_%7B2%7D%3D-%5Cfrac%7Bb%7D%7B2a%7D">;
  </p>

  3. <img src="https://latex.codecogs.com/svg.latex?%5CDelta%3D%5Csqrt%7Bb%5E2-4ac%7D%3C0">.
    In questo caso l'equazione è *impossibile*, perché qualsiasi numero reale elevato al quadrato risulterà maggiore o uguale a zero e non potrà essere minore del secondo membro, che è negativo.

Quando più avanti parleremo di intersezioni o di sistemi di secondo grado *impossibili* o *con soluzioni coincidenti*, sarà attraverso il calcolo del *delta* che potremmo verificare se e come una retta, ad esempio, interseca una parabola.

## Parabola

### Introduzione

<img src="Figure_1.png" width="800">

La parabola è il luogo geometrico dei punti equidistanti da un punto fisso, detto _fuoco_, e da una retta data, detta _direttrice_.

L'equazione di una parabola con l'asse parallelo all'asse delle Y è:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?y%3Dax%5E2%2Bbx%2Bc">
</p>

L'equazione di una parabola con l'asse parallelo all'asse delle X è:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?x%3Day%5E2%2Bby%2Bc">
</p>

Per disegnare una parabola, è importante considerare altri tre elementi: il *vertice*, il *fuoco* e la *direttrice*.

Per una parabola con asse parallelo ad Y, le coordinate del *vertice* si possono calcolare in questo modo:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?V%28-%5Cfrac%7Bb%7D%7B2a%7D%3B-%5Cfrac%7B%5CDelta%7D%7B4a%7D%29">
</p>

Le coordinate del *fuoco* si possono calcolare in questo modo:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?F%28-%5Cfrac%7Bb%7D%7B2a%7D%3B%5Cfrac%7B1-%5CDelta%7D%7B4a%7D%29">
</p>

Infine, l'equazione della *direttrice* è:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?y%3D-%5Cfrac%7B1%2B%5CDelta%7D%7B4a%7D">
</p>

Nel caso di parabola con asse parallelo ad X, le coordinate di fuoco e vertice hanno le componenti invertite.

Vuoi disegnare una parabola con asse paralello all'asse Y o all'asse X? Prova [questo](https://github.com/albusdemens/Ripasso_coniche/blob/master/Parabola.py) script in Python!

Con [quest'altro script](https://github.com/albusdemens/Ripasso_coniche/blob/master/Intersezione_parabola_retta.py) puoi disegnare l'intersezione di una parabola con un segmento.

### Intersezioni retta-parabola

Data una parabola ed una retta con equazione *y = mx+q*, per trovare gli eventuali punti di intersezione si segue il seguente procedimento:
1. Mettere a sistema l'equazione della retta e l'equazione della parabola;
2. Risolvere il sistema di secondo grado così formato e ricavare gli eventuali valori delle incognite x ed y:

    A. Se il sistema risulta *impossibile*, quindi non è possibile ricavare né il valore di x né quello di y, allora vuol dire         che la retta e la parabola non hanno punti in comune: si dice che la retta è *esterna* alla parabola;

    B. Se il sistema ha *due soluzioni coincidenti*, cioè *una soluzione doppia*, la retta e la parabola sono *tangenti*;

    C. Se il sistema ha *due soluzioni distinte*, la retta e la parabola sono *secanti*;

3. Eventualmente, rappresentare graficamente la soluzione.    


### Determinazione della retta tangente

Una retta si dice tangente ad una curva quando *tocca ma non interseca* la curva stessa. Dunque, per calcolare l'equazione di una retta passante per un punto e tangente ad una parabola, la procedura è la seguente:

1. Dato il punto A, di coordinate <img src="https://latex.codecogs.com/svg.latex?%28x_A%2C+y_A%29">, si calcola l'equazione generale della retta passante per A, ossia
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?y-y_A%3Dm%28x-x_A%29">
</p>
2. Messo a sistema l'equazione generia della retta con l'equazione della parabola, si risolve il sistema ponendo <img src="https://latex.codecogs.com/svg.latex?%5CDelta%3D%5Csqrt%7Bb%5E2-4ac%7D%3C0">

## Ellisse

<img src="Ellisse.png" width="800">

### Introduzione

L'ellisse è il luogo geometrico dei punti di un piano per i quali è costante la somma delle distanze da due punti fissi, detti _fuochi_.

Essendo i due fuochi dei punti fissi, la distanza tra loro, detta **distanza focale**, è nota.

L'equazione dell'ellisse è:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cfrac%7Bx%5E2%7D%7Ba%5E2%7D%2B%5Cfrac%7By%5E2%7D%7Bb%5E2%7D%3D1">
</p>

Le formule per calcolare la posizione dei fuochi di un'ellisse sono:

Per disegnare un'ellisse dati i fuochi e la distanza dei punti della curva da questi, prova [questo](https://github.com/albusdemens/Ripasso_coniche/blob/master/Ellisse.py) script.

## Circonferenza

<img src="Crf.png" width="800">

Per disegnare una circonferenza dato il centro ed il raggio, prova [questo](https://github.com/albusdemens/Ripasso_coniche/blob/master/Circonferenza.py) script.

## Iperbole
