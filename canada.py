from scipy import misc
from PIL import Image

inp = misc.imread('rompecabezas.png')
print(inp[1,1])
outp=[for i in range(100):[for j in range(100):inp[i*50+5,j*50+5]]]
img = Image.fromarray(outp, 'RGB')
img.save('my.png')
img.show()
