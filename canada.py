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
outp=[[inp[i*10+3,j*10+3] for j in range(100)] for i in range(100)]
outp=np.asarray(outp)
img = Image.fromarray(outp, 'RGB')
img.save('my.png')
moverPieza(outp,7,17,0,19)
for i in range(1):
    for j in range(20):
        romper=False
        for o in range(i,20):
            if romper:
                break
            for k in range(j,20):
                if(i==0):
                    if(bon(getColor(outp,2,o,k)) or bon(getColor(outp,1,o,k))):
                        moverPieza(outp,o,k,i,j)
                        romper=True
                        break






img = Image.fromarray(outp, 'RGB')
img.save('my1.png')
