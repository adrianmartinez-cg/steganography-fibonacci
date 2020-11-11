import cv2
import random
import numpy as np
def calculosdiv255(E,E_q,E_r):
    N=len(E)
    for i in range(N):
        for j in range(N):
            if i == j:
                E_q.append(E[i][j]//255)
                E_r.append(E[i][j]%255)
    arquivo=open('key.txt','w')
    arquivo.write(str(E_q))
    arquivo.write('\n')
    arquivo.write(str(E_r))
    arquivo.close()    
def ajeitamatriz(E,E_r):
    for i in range(len(E)):
        for j in range(len(E)):
            if i == j:
                if E[i][j] > 255:
                    E[i][j]=E_r[i]
def Fn(n): 
    F=[0,1]
    indice=2
    soma=0
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        while True:
            if indice > n: break
            for i in range(len(F)-2,len(F)):
                soma+=F[i]
            F.append(soma)
            soma=0
            indice+=1
    return F
M=input() #Mensagem do usuário
N=len(M) #Tamanho da mensagem
C=[] #Lista dos codigos ascii dos caracteres da mensagem
for i in range(len(M)):
    C.append(ord(M[i]))
F=Fn(N-1)
S=[] # Soma dos codigos ascii com a sequencia Fn
for i in range(len(C)):
    S.append(C[i]+F[i])
R = [[random.randint(1,100) for j in range (N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            R[i][j]=S[i]
R=np.array(R)
#Depois desse procedimento, a matriz R é chamada de A
X=cv2.imread('lena.bmp',0) #Lê a imagem em escala cinza
Y=X[0:N,0:N] #Porção da matriz X, tamanho N x N
E=[[0 for j in range(N)] for i in range(N)] #Soma das matrizes A e Y
for i in range(N):
    for j in range(N):
        E[i][j] = R[i][j]+Y[i][j]
E_q=[]
E_r=[]
calculosdiv255(E,E_q,E_r)
ajeitamatriz(E,E_r)
E=np.array(E)
G=cv2.imwrite('lena_crop.bmp',Y)
encrypted_img=cv2.imwrite('lena_encrypted.bmp',E)
