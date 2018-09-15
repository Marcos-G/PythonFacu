from scipy import misc
from PIL import Image
import numpy as np
import copy

def moverPieza(im,i1,j1,i2,j2):
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
moverPieza(outp,0,16,0,3)
moverPieza(outp,1,4,0,2)
moverPieza(outp,1,9,0,11)
moverPieza(outp,2,8,0,7)
moverPieza(outp,3,0,0,14)
moverPieza(outp,4,7,0,9)
moverPieza(outp,5,3,0,17)
moverPieza(outp,7,17,0,13)
moverPieza(outp,8,8,0,12)
moverPieza(outp,10,1,0,5)
moverPieza(outp,11,11,0,8)
moverPieza(outp,12,16,0,10)
moverPieza(outp,13,6,0,4)
moverPieza(outp,15,5,0,1)
moverPieza(outp,16,5,0,16)
moverPieza(outp,17,4,0,15)
moverPieza(outp,17,12,0,18)
moverPieza(outp,18,10,0,6)
moverPieza(outp,19,17,0,19)
moverPieza(outp,4,14,19,19)
moverPieza(outp,8,5,18,19)
moverPieza(outp,5,10,17,19)
moverPieza(outp,9,16,16,19)
moverPieza(outp,4,7,15,19)
moverPieza(outp,3,16,14,19)
moverPieza(outp,19,5,3,3)
moverPieza(outp,9,0,19,17)

for a in range(1):
    for i in range(1,20):
        for j in range(20):
            cortar=False
            for o in range(20):
                if(cortar):
                    break
                for k in range(20):
                    if(o>i or k>j):
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
                        else:
                            if(np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) and np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,3,i-1,j-1))and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))and np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j))):
                                moverPieza(outp,o,k,i,j)
                                cortar=True
                                break







img = Image.fromarray(outp, 'RGB')
img.save('my1.png')
