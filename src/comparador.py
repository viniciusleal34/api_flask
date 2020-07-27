# -*- coding: utf-8 -*-
import os
import numpy as np
import glob
import pickle as cPickle

PATH_DESCRITOR = os.path.join(os.getcwd(),'Descritor','descritores.npy')
PATH_INDICE = os.path.join(os.getcwd(), 'Descritor','indices.pickel')
class Reconhecer:

    def __init__(self, matriz, limiar = 0.5, indice = PATH_INDICE, descritorFace=PATH_DESCRITOR):
        self.indice = np.load(indice)
        self.descritoresFaciais= np.load(descritorFace)
        self.limiar = limiar
        self.matriz = matriz

    def recoding(self):
        distancias = np.linalg.norm(self.matriz - self.descritoresFaciais, axis=1)
        minimo = np.argmin(distancias)
        distanciaMinima = distancias[minimo]

        if distanciaMinima <= self.limiar:
            nome = os.path.split(self.indice[minimo])[1].split(".")[0]

        else:
            nome = "Fase não foi reconhecida no sistema"
        return nome