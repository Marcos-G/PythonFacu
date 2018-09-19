from scipy import misc
from PIL import Image
import numpy as np
import copy
colocados=[]
def moverPieza(im,i1,j1,i2,j2):
    global colocados
    print("m",i1,j1,i2,j2)
    temp=copy.deepcopy(im[i1*5:i1*5+5,j1*5:j1*5+5])
    im[i1*5:i1*5+5,j1*5:j1*5+5]=im[i2*5:i2*5+5,j2*5:j2*5+5]
    im[i2*5:i2*5+5,j2*5:j2*5+5]=temp
    colocados.append((i2,j2))
def moverPiezaP(im,i1,j1,i2,j2):
    print("m",i1,j1,i2,j2)
    temp=copy.deepcopy(im[i1*5:i1*5+5,j1*5:j1*5+5])
    im[i1*5:i1*5+5,j1*5:j1*5+5]=im[i2*5:i2*5+5,j2*5:j2*5+5]
    im[i2*5:i2*5+5,j2*5:j2*5+5]=temp
def getColor(im,n,i,j):
    a=0
    b=0
    if(n==4 or n==3):
        a=4
    if(n==3 or n==2):
        b=4
    return im[5*i+a,5*j+b]
def bon(col):
    if(np.array_equal(col,np.asarray([255,255,255])) or np.array_equal(col,np.asarray([0,0,0]))):
        return True
    return False


inp = misc.imread('rompecabezas.png')
outp=[[inp[i*10+5,j*10+5] for j in range(100)] for i in range(100)]
outp=np.asarray(outp)
img = Image.fromarray(outp, 'RGB')
img.save('my.png')
moverPieza(outp,18,1,0,0)
moverPieza(outp,0,16,0,12)
moverPieza(outp,1,4,0,3)
moverPieza(outp,1,9,0,16)
moverPieza(outp,2,8,0,5)
moverPieza(outp,3,0,0,18)
moverPieza(outp,4,7,0,11)
moverPieza(outp,5,3,0,7)
moverPieza(outp,7,17,0,17)
moverPieza(outp,8,8,0,1)
moverPieza(outp,10,1,0,13)
moverPieza(outp,11,11,0,4)
moverPieza(outp,12,16,0,9)
moverPieza(outp,13,6,0,15)
moverPieza(outp,15,5,0,2)
moverPieza(outp,16,5,0,6)
moverPieza(outp,17,4,0,10)
moverPieza(outp,17,12,0,8)
moverPieza(outp,18,10,0,14)
moverPieza(outp,19,17,0,19)
moverPiezaP(outp,19,5,3,3)
moverPiezaP(outp,4,14,19,13)
moverPiezaP(outp,5,10,19,17)
moverPiezaP(outp,5,2,19,18)
moverPiezaP(outp,5,14,19,16)
moverPiezaP(outp,5,12,19,15)
moverPiezaP(outp,18,14,19,14)
moverPiezaP(outp,17,15,19,19)
moverPiezaP(outp,7,18,19,19)
moverPiezaP(outp,16,2,19,13)
moverPiezaP(outp,10,16,19,12)
moverPiezaP(outp,19,3,19,12)

for a in range(1):
    for i in range(20):
        for j in range(20):
            cortar=False
            for o in range(20):
                if(cortar):
                    break
                for k in range(20):
                    if((o,k) not in colocados):
                        if(j==0 and i==0):
                            cortar=True
                            break
                        elif(j==0):
                            if(bon(getColor(outp,4,o,k)) and bon(getColor(outp,1,o,k)) and np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) ):
                                moverPieza(outp,o,k,i,j)
                                cortar=True
                                break
                        elif(i==0):
                            if(bon(getColor(outp,2,o,k)) and bon(getColor(outp,1,o,k)) and np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)) ):
                                moverPieza(outp,o,k,i,j)
                                cortar=True
                                break
                        elif(i==19 and j==19):
                                cortar=True
                                break
                        elif(i==19):
                                if(np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,3,i-1,j-1))and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))and np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j))):
                                    moverPieza(outp,o,k,i,j)
                                    cortar=True
                                    break
                        elif(j==19):
                                if(np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,3,i-1,j-1))and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))and np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j))):
                                    moverPieza(outp,o,k,i,j)
                                    cortar=True
                                    break
                        else:
                            #print(np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) , np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)) , np.array_equal(getColor(outp,1,o,k),getColor(outp,3,i-1,j-1)), np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j)), np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) , np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)))
                            if(np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) and np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,3,i-1,j-1))and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))and np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j))):
                                moverPieza(outp,o,k,i,j)
                                cortar=True
                                break



moverPieza(outp,12,19,15,19)
moverPieza(outp,13,19,18,19)
moverPieza(outp,14,19,17,19)
moverPieza(outp,16,19,15,19)
moverPieza(outp,19,19,16,19)
moverPieza(outp,19,19,18,19)
'''for a in range(20):
    for b in range(20):
        outp[a*5,b*5]=[0,0,0]
        outp[a*5,b*5+4]=[0,0,0]
        outp[a*5+4,b*5]=[0,0,0]
        outp[a*5+4,b*5+4]=[0,0,0]'''
img = Image.fromarray(outp, 'RGB')
img.save('my1.png')
