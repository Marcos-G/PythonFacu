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
temp=outp[0:5,0:5]
img = Image.fromarray(temp, 'RGB')
img.save('my1.png')
def moverPieza(i1,j1,i2,j2):
    temp=outp[i1*5:i1*5+5,j1*5:j1*5+5]
    outp[i1*5:i1*5+5,j1*5:j1*5+5]=outp[i2*5:i2*5+5,j2*5:j2*5+5]
