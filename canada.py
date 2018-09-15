from scipy import misc
from PIL import Image
import numpy as np

inp = misc.imread('rompecabezas.png')
print(inp[1,1])
outp=[[inp[i*10+5,j*10+5] for j in range(100)] for i in range(100)]
outp=np.asarray(outp)

img = Image.fromarray(outp, 'RGB')
img.save('my.png')
img.show()
temp=outp[0:4,0:4]
img = Image.fromarray(outp, 'RGB')
img.save('my.png')
def moverPieza(i1,j1,i2,j2):
    temp=outp[i1*5:i1*5+4,ij1*5:ij1*5+4]
