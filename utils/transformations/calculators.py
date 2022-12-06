import numpy as np
import math

def moyenneGris(matrice) : 
    somme = 0
    for i in range(0,matrice.shape[0]) :
        for j in range(0,matrice.shape[1]): 
            somme += int(matrice[i][j])
    
    return somme / (matrice.shape[0] * matrice.shape[1])

def ecartypeGris(matrice) :
    somme = 0
    moy = moyenneGris(matrice)
    for i in range(0,matrice.shape[0]) :
        for j in range(0,matrice.shape[1]): 
            somme += (int(matrice[i][j])- moy)**2
    
    return np.sqrt(somme / (matrice.shape[0] * matrice.shape[1]))

def histo(img):
    arr = np.zeros(256)
    for el in img:
        for num in el:
            arr[num]+=1;
    return arr

def cumule(img):
    arr = histo(img)
    arr_cumul = np.zeros(256)
    somm = 0
    for i,el in enumerate(arr):
        somm += el
        arr_cumul[i] = somm
    return arr_cumul

def calculate_rapport(img1, img2):
    varianceImg1 = ecartypeGris(img1)

    print(img1)
    vim2 = 0
    for i in range(0,img2.shape[0]) :
        for j in range(0,img2.shape[1]): 
            vim2 += (int(img2[i][j])- int(img1[i][j]))**2
    
    return varianceImg1/ math.sqrt(vim2)