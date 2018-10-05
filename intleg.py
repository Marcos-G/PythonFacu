import sys

if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    exit()
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    exit()
filelines=open(sys.argv[1],'r').readLines()
print (str(filelines))
