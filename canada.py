from scipy import misc
from PIL import Image
import numpy as np
import copy

def moverPieza(im,i1,j1,i2,j2):
    temp=copy.deepcopy(im[i1*5:i1*5+5,j1*5:j1*5+5])
    print(temp[0,0])
    im[i1*5:i1*5+5,j1*5:j1*5+5]=im[i2*5:i2*5+5,j2*5:j2*5+5]
    print(temp[0,0])
    im[i2*5:i2*5+5,j2*5:j2*5+5]=temp
def getColor(im,n,i,j):
    a=0
    b=0
    if(n==2 or n==3):
        a=4
    if(n==3 or n==4):
        b=4
    return im[5*i+a,5*j+b]

inp = misc.imread('rompecabezas.png')
print(inp[1,1])
outp=[[inp[i*10+5,j*10+5] for j in range(100)] for i in range(100)]
outp=np.asarray(outp)
print(getColor(outp,1,0,0))
print(getColor(outp,2,0,0))
print(getColor(outp,3,0,0))
print(getColor(outp,4,0,0))

img = Image.fromarray(outp, 'RGB')
img.save('my.png')






img = Image.fromarray(outp, 'RGB')
img.save('my1.png')
