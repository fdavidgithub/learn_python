import cv2
import sys

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

imagem = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

faces = faceCascade.detectMultiScale(
    imagem,
    minNeighbors=5,
    minSize=(30, 30),
	maxSize=(200,200)
)

''' 
Desenha um retangulo nas faces detectadas
'''
for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Imagem', imagem) 

'''
o trecho seguinte e apenas para parar o ccdigo e fechar a janela
'''

cv2.waitKey(0)
cv2.destroyAllWindows() 


