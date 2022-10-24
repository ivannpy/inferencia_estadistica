import numpy as np
from utils import *


def T_1(X):
        """ Calcula la media muestral de una muestra aleatoria X=(X_1,...X_n)
        :param X: X es un arreglo de Numpy.
        :return: La media aritmética de las entradas del vector X.
        """

        return around2(X.mean())


def T_2(X):
        """ Calcula la media muestral y la estadística S^2.
        :param X: X es un arreglo de Numpy.
        :return: (media, s^2)
        """

        t_1 = X.mean()
        coef = 1 / (X.size - 1)
        t_2 = coef * ((X - X.mean()) ** 2).sum()
        
        return around2(t_1), around2(t_2)