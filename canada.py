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
#moverPieza(outp,7,17,0,0)
for a in range(10):
    for i in range(20):
        for j in range(20):
            for o in range(20):
                for k in range(20):
                    if(i==0):
                        if(np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1))):
                            moverPieza(outp,o,k,i,j)
                    elif(j==0):
                        if(np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))):
                            moverPieza(outp,o,k,i,j)
                    else:
                        if((np.array_equal(getColor(outp,2,o,k),getColor(outp,3,i-1,j)) and np.array_equal(getColor(outp,1,o,k),getColor(outp,4,i-1,j))) or (np.array_equal(getColor(outp,1,o,k),getColor(outp,2,i,j-1)) and np.array_equal(getColor(outp,4,o,k),getColor(outp,3,i,j-1)))):
                            moverPieza(outp,o,k,i,j)







img = Image.fromarray(outp, 'RGB')
img.save('my1.png')
