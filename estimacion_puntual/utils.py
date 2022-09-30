"""
    Funciones comunes para el Notebook sobre Estimación puntual
"""
import numpy as np
from IPython.display import display, Latex


def load_data(filename):
    """ Carga los datos de un archivo cvs a un arreglo de Numpy.
    
    :param filename: Nombre del archivo .csv a cargar.
    :return: Numpy array.
    """
    data = np.genfromtxt(filename, delimiter=',', dtype=float)
    return data


def save_data(data, filename):
    """ Guarda un arreglo de Numpy a un archivo .cvs
    
    :param data: Numpy array a guardar.
    :param filename: Nombre del archivo donde se va a guardar.
    :return: None
    """
    np.savetxt(filename, data, delimiter=",", fmt="%.2f")
    
    
def around2(number):
    return np.around(number, 2)


def print_pretty_sample(X):
    print("Realización de la muestra aleatoria.")
    print(f"Tamaño de la muestra: {X.size}.")

    n = X.size
    
    for i in range(1, n + 1):
        display(Latex("$x_{%s}$"%str(i) + f" = {X[i-1]}"))
