from scipy import misc
from PIL import Image

arr = misc.imread('rompecabezas.png')
print(arr[1,1])
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
