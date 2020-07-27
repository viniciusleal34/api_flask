# -*- coding: utf-8 -*-
import os
import dlib
import cv2
import numpy as np


PATH_DETECTOR = os.path.join(os.getcwd(), 'IA','shape.dat')
PATH_RECONHECIMENTO = os.path.join(os.getcwd(), 'IA','dlib_face.dat')
class DescritorImagem:
    def __init__(self,imagem="IMG_20200524_155231.png", detectorPontos = PATH_DETECTOR, reconhecimentoFacial = PATH_RECONHECIMENTO):
        self.detectorFace = dlib.get_frontal_face_detector()
        self.detectorPontos =dlib.shape_predictor(detectorPontos)
        self.reconhecimentoFacial = dlib.face_recognition_model_v1(reconhecimentoFacial)
        self.imagem = cv2.imread(imagem,1)

    def gerarMatriz(self):
        indice = {}
        idx = 0
        descritoresFaciais = None

        facesDetectadas = self.detectorFace(self.imagem, 1)
        numeroFacesDetectadas = len(facesDetectadas)

        if numeroFacesDetectadas > 1:
            print("Há mais de uma face na imagem")
            exit(0)
        elif numeroFacesDetectadas < 1:
            print("Nenhuma face encontrada no arquivo")
            exit(0)

        for face in facesDetectadas:
            pontosFaciais = self.detectorPontos(self.imagem, face)
            descritorFacial = self.reconhecimentoFacial.compute_face_descriptor(self.imagem, pontosFaciais)
            #print(format(arquivo))
            #print(len(descritorFacial))
            #print(descritorFacial)

            listaDescritorFacial = [df for df in descritorFacial]
            #print(listaDescritorFacial)

            npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
            #print(npArrayDescritorFacial)

            npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
            #print(npArrayDescritorFacial)

            if descritoresFaciais is None:
                descritoresFaciais = npArrayDescritorFacial
            else:
                descritoresFaciais = np.concatenate((descritoresFaciais, npArrayDescritorFacial), axis=0)

        return (descritoresFaciais)