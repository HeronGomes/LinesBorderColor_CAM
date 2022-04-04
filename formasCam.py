# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np



def colorir(parametro_imagem):
    seedPic = np.random.randint(1,1e3)

    
    h,w = (480,640)
    c = 3
    
    imagem_exibicao = parametro_imagem.copy()
    
    cv.putText(imagem_exibicao,
              '#Imagem de amostra',
              (0,15),
              cv.FONT_HERSHEY_COMPLEX_SMALL,
              1,
              (255,0,255),
              1,
              cv.LINE_AA)   
    
        
    imagem_contorno = np.full((h,w,c),0,np.uint8)
    
    video = cv.VideoWriter('./colori_'+str(seedPic)+'.mp4',cv.VideoWriter.fourcc(*'mp4v'),15,(w*2,h))
    
    imagem_cinza = cv.cvtColor(parametro_imagem,cv.COLOR_BGR2GRAY)
        
    
    _,thresh2 = cv.threshold(imagem_cinza,126,255,cv.THRESH_OTSU) 
                
    
    contornos,_ = cv.findContours(thresh2,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    
    
    cv.putText(imagem_contorno,
              '#Algoritmo em funcionamento',
              (0,15),
              cv.FONT_HERSHEY_COMPLEX_SMALL,
              1,
              (255,0,255),
              1,
              cv.LINE_AA)   
    
    
    for contorno in contornos[::-1]:
    
    
        approx = cv.approxPolyDP(contorno,0.002*cv.arcLength(contorno,True),True)
        
                            
        
        cv.drawContours(image=imagem_contorno,
                    contours=[approx],
                    contourIdx = -1,
                    color=(np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)),
                    thickness=cv.FILLED)
        
        quadro=cv.hconcat([imagem_exibicao,imagem_contorno])
        
        
        cv.imshow('Colorindo',quadro)
        cv.waitKey(30)
        video.write(quadro)

        
        
    cv.putText(quadro,
              '#Algoritmo em funcionamento',
              (0,641),
              cv.FONT_HERSHEY_COMPLEX_SMALL,
              1,
              (255,0,255),
              1,
              cv.LINE_AA)
        
        
    cv.putText(quadro,
                '(Pressione uma tecla para sair.)',
              (0,470),
              cv.FONT_HERSHEY_COMPLEX_SMALL,
              1,
              (255,0,255),
              1,
              cv.LINE_AA)
    cv.line(quadro,
        (0,450),
        (630,450),
        (255,0,255),
        1,
        1)    
  
    cv.imshow('Colorindo',quadro)
    cv.waitKey()
    cv.destroyAllWindows()
    video.release()
    desenhaOriginal()

def desenhaOriginal():
    cap = cv.VideoCapture()
    cap.open(2,cv.CAP_DSHOW)
    while True:
        
        isFrame,imagem_original = cap.read()   
        
        if isFrame:
            imagem_resize = cv.resize(imagem_original,(640,480))   
            imagem_param_seguir = imagem_resize.copy()
            
            cv.line(imagem_resize,
                    (0,450),
                    (630,450),
                    (255,0,255),
                    1,
                    1)
            cv.putText(imagem_resize,
                       '(q - Sair) (c - colorir)',
                      (0,470),
                      cv.FONT_HERSHEY_COMPLEX_SMALL,
                      1,
                      (255,0,255),
                      1,
                      cv.LINE_AA)
              
                
            tecla = cv.waitKey(100)
            cv.imshow('Original',imagem_resize)
            
            if tecla == ord('q'):
                cap.release()
                cv.destroyWindow('Original')
                
                break
            elif tecla == ord('c'):
                # cap.release()
                # cv.destroyWindow('Original')
                colorir(imagem_param_seguir)
                break


       

desenhaOriginal() 



