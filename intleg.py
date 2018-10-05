import sys

if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    exit()
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    exit()
fileObj=open(sys.argv[1],'r')
filelines=fileObj.readlines()
estados=[]
reglas={}
alfabetoE={}
alfabetoT={}
lenguaje=[]
for n in range(len(filelines)):
    error=False
    errormsg=""
    line=filelines[n].rstrip()
    if(line.startswith("//")):
        continue
    terms=line.split("=>")
    if(not len(terms)==2):
        error=True
        errormsg="Mal definido el simbolo de transicion '=>'"
    if(not (terms[0].startswith("(") and terms[0].endswith(")") and terms[1].startswith("(") and terms[1].endswith(")"))):
        error=True
        errormsg="Faltan parentesis"
    if(error):
        print("ERROR:",errormsg,"en la linea",n,":",line)


fileObj.close()
