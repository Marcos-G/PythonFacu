from scipy import misc
from PIL import Image

inp = misc.imread('rompecabezas.png')
print(inp[1,1])
outp[100,100]=[255,255,255]
img = Image.fromarray(outp, 'RGB')
img.save('my.png')
img.show()
