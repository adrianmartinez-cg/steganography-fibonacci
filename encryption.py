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
def inserirdados_encrypt(X,E):
    X_E=[[X[i][j] for j in range (len(X))] for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X)):
            if i <=len(E)-1 and j<=len(E)-1:
                X_E[i][j]=E[i][j]
    return X_E

################################################################

M=input() #Mensagem do usuário
N=len(M) #Tamanho da mensagem
C=[] #Lista dos codigos ascii dos caracteres da mensagem
for i in range(len(M)):
    C.append(ord(M[i]))
F=Fn(N-1)
S=[] # Soma dos elementos da lista C com a lista F
for i in range(len(C)):
    S.append(C[i]+F[i])
A = [[random.randint(1,100) for j in range (N)] for i in range(N)] #Nesse ponto na verdade estamos criando a matriz R. Colocando os elementos de S na diagonal temos A
for i in range(N):
    for j in range(N):
        if i == j:
            A[i][j]=S[i]
A=np.array(A) #declarando A como um array n-dimensional de numpy
X=cv2.imread('lena.bmp',0) #Lê a imagem em escala cinza , e armazena os valores da escala em uma matriz
Y=X[0:N,0:N] #Porção da matriz X, tamanho N x N (N=tamanho da mensagem)
E=[[0 for j in range(N)] for i in range(N)] #Soma das matrizes A e Y
for i in range(N):
    for j in range(N):
        E[i][j] = A[i][j]+Y[i][j]
E_q=[] #lista usada para armazenar alguns valores no arquivo key.txt (que serão lidos na hora de decriptar)
E_r=[] #lista usada para armazenar alguns valores no arquivo key.txt (que serão lidos na hora de decriptar)
calculosdiv255(E,E_q,E_r) #Obtem os valores para as duas listas anteriores
ajeitamatriz(E,E_r) #Irá ajeitar a matriz E , de modo que nao exista valores maiores que 255 na diagonal da matriz
E=np.array(E) #declarando E como um array n-dimensional de numpy
X_E=inserirdados_encrypt(X,E) # Armazena a porção da imagem encriptada na imagem em escala cinza original
X_E=np.array(X_E)
G=cv2.imwrite('lena_crop.bmp',Y) #Salva os dados na matriz Y (corte da imagem original) em uma imagem
encrypted_img=cv2.imwrite('lena_encrypted.bmp',X_E) #Salva os dados da matriz X_E em uma imagem
