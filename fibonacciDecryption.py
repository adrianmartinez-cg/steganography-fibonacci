import numpy as np
import cv2
import random
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
def obtervetores():
    arquivo=open('key.txt','r')
    linhas=[]
    vet1=''
    vet2=''
    for linha in arquivo:
        linhas.append(linha)
    for j in range(len(linhas[0])-1):
        if linhas[0][j] != " " and linhas[0][j] != "[" and linhas[0][j] != "]":
            vet1+=linhas[0][j]
    for j in range(len(linhas[1])):
        if linhas[1][j] != " " and linhas[1][j] != "[" and linhas[1][j] != "]":
            vet2+=linhas[1][j]
    return [vet1,vet2]
def ajeita_D(D,E_q,E_r):
    for i in range(len(D)):
        for j in range(len(D)):
            if i == j:
                D[i][j] = 255*int(E_q[i]) + int(E_r[i])
    return D
D=cv2.imread('lena_encrypted.bmp',0)
vetores=obtervetores()
E_q=vetores[0].split(",")
E_r=vetores[1].split(",")
D=np.array(D).tolist()
D=ajeita_D(D,E_q,E_r)
D=np.array(D)
B=cv2.imread('lena_crop.bmp',0)
Z=D-B
N1=len(Z)
M=[]
for i in range(N1):
    for j in range(N1):
        if i == j:
            M.append(Z[i][j])
E=Fn(N1-1)
M=np.array(M)
E=np.array(E)
P=M-E
msg=''
for i in range(len(P)):
    msg+=chr(P[i])
print(msg)
