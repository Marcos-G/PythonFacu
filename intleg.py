import sys

if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    return
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    return
print sys.argv[1]
