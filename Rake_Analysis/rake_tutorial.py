from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'

import rake
import operator
import io
from os import listdir

def escribirKeys( pathFicheros, rake_object ):
    f=open(pathFicheros+"palabras.csv","w",encoding="iso-8859-1")
    #f2=open(pathFicheros+"pruebas-ConPesos.csv","w")
    for cosa in listdir(pathFicheros):
        #print(pathFicheros+cosa)
        if cosa=="palabras.csv":
            print("estoy en priebas")
        else:
            sample_file = io.open(pathFicheros+cosa, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            #print(keywords)
            nombreFichero = cosa[:-4]+"-Pesos.key"
            #f=open(pathFicheros+nombreFichero,"w")
            #f2=open(pathFicheros+nombreFichero,"w")
            i=0
            enc=False
            try:
                f.write(cosa+";")
                for key in keywords:
                      
                        if i==0:
                            f.write(key[0])
                            enc=True
                            #print("entro "+cosa)
                        if i>0 and i<15:
                            print(key[0])
                            f.write(","+key[0])
                            #f2.write(key[0]+" "+str(key[1])+"\n")
                        i=i+1
            except Exception:
                print("error")
            
            #f2.flush()
            #f2.close()
            if enc:
                f.write("\n")
    f.flush()
    f.close()

def escribirKeysListado( pathFicheros, rake_object ):
    f=open(pathFicheros+"palabras.csv","w",encoding="iso-8859-1")
    #f2=open(pathFicheros+"pruebas-ConPesos.csv","w")
    for cosa in listdir(pathFicheros):
        #print(pathFicheros+cosa)
        if cosa=="palabras.csv":
            print("estoy en priebas")
        else:
            sample_file = io.open(pathFicheros+cosa, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            #print(keywords)
            nombreFichero = cosa[:-4]+"-Pesos.key"
            #f=open(pathFicheros+nombreFichero,"w")
            #f2=open(pathFicheros+nombreFichero,"w")
            i=0
            enc=False
            try:
                
                for key in keywords:
                        if i<15:
                            print(key[0])
                            f.write(key[0]+"\n")
                            #f2.write(key[0]+" "+str(key[1])+"\n")
                        i=i+1
            except Exception:
                print("error")
            
            #f2.flush()
            #f2.close()
            if enc:
                f.write("\n")
    f.flush()
    f.close()

def escribirKeysUnicas( pathFicheros, rake_object, dictPalabras ):
    f=open(pathFicheros+"palabras.csv","w",encoding="iso-8859-1")
    #f2=open(pathFicheros+"pruebas-ConPesos.csv","w")
    for cosa in listdir(pathFicheros):
        #print(pathFicheros+cosa)
        if cosa=="palabras.csv":
            print("estoy en priebas")
        else:
            sample_file = io.open(pathFicheros+cosa, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            #print(keywords)
            #f=open(pathFicheros+nombreFichero,"w")
            i=0
            enc=False
            for key in keywords:
                try:  
                    clave=key[0]
                    if i==0:
                        if clave in dictPalabras:
                            print("Escribo")
                            f.write(dictPalabras[clave])
                            i=i+1
                            enc=True
                        #print("entro "+cosa)
                    if i>0:
                        if clave in dictPalabras:
                            print("Escribo2")
                            f.write(","+dictPalabras[clave])
                        i=i+1
                except Exception:
                    print("error")
            if enc:
                f.write("\n")
    f.flush()
    f.close()


def escribirMatriz(pathFicheros, rake_object ):
    item_list = []
    seen = set(item_list)
    for cosa in listdir(pathFicheros):
        sample_file = io.open(pathFicheros+cosa, 'r', encoding="iso-8859-1")
        text = sample_file.read()
        keywords = rake_object.run(text)
        i=0
        for key in keywords:
            if key[0] not in seen and i<15:
                seen.add(key[0])
            i=i+1
    print(seen)
    f=open("results/Docs.csv","w", encoding="iso-8859-1")
    for keys in seen:
        f.write(str(keys)+",")
    f.write("doc\n")
    for cosa in listdir(pathFicheros):
        sample_file = io.open(pathFicheros+cosa, 'r', encoding="iso-8859-1")
        text = sample_file.read()
        keywords = rake_object.run(text)
        for palabra in seen:
            valor=0
            for key in keywords:
                if palabra == key[0]:
                    valor=key[1]
                    print(cosa + " " + key[0] + " " + str(valor))
            f.write(str(valor)+",")
        f.write(cosa+"\n")
    f.flush()
    f.close()
        
    
def normalizarDoc():
    fichFinal= open("results/DocsNormalizados.csv","w", encoding="iso-8859-1")
    i=0
    for linea in open("results/Docs.csv","r", encoding="iso-8859-1"):
        if i==0:
            fichFinal.write(linea)
        else:        
            valores = linea.split(",")
            suma=0
            for valor in range(0,len(valores)-1):
                suma = suma+float(valores[valor])
            print("SUMA: "+str(suma))
            for valor in range(0,len(valores)-1):
                escrituraValor=0
                if suma!=0:
                    escrituraValor = float(valores[valor])/suma
                print("VALOR ANTERIOR: "+str(valores[valor])+" VALOR AHORA: "+str(escrituraValor))
                fichFinal.write(str(escrituraValor)+",")
            fichFinal.write(valores[len(valores)-1])
        i=i+1
    fichFinal.flush()
    fichFinal.close()
    
def leerFicheroCSV(palabrasClave):
    i=0
    dictionaryPalabras={}
    #for linea in open("results/palabrasCLAVERIS.csv","r", encoding="iso-8859-1"):
    for linea in open(palabrasClave,"r", encoding="iso-8859-1"):
        clave,valor = linea.split(";")
        valor = valor.rstrip()
        if valor!="": 
            dictionaryPalabras[clave] = valor
    return dictionaryPalabras
    
            
# EXAMPLE ONE - SIMPLE
stoppath = "stops/Stopwords.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 3, 8, 6)
#"data/docs/fao_test/"
pathFicheros ="textos/"
#pathFicheros ="textosINDUSTRIAL/"
#pathFicheros ="textosLEARNING/"
#pathFicheros ="textosLOCAL/"
#pathFicheros ="textosMILIEU/"
#pathFicheros ="textosNEWINDUSTRIAL/"
#pathFicheros = "textosRIS/"

palabrasClave="palabrasCuartoCluster.csv"
#palabrasClave="results/Palabras/palabrasCLAVEID.csv"
#palabrasClave="results/Palabras/palabrasCLAVELPS.csv"
#palabrasClave="results/Palabras/palabrasCLAVELR.csv"
#palabrasClave="results/Palabras/palabrasCLAVEMI.csv"
#palabrasClave="results/Palabras/palabrasCLAVENIS.csv"
#palabrasClave="results/Palabras/palabrasCLAVERIS.csv"
#palabrasClave="results/Palabras/palabrasMAXICLUSTER.csv"
#palabrasClave="results/Palabras/palabrasMAXIID.csv"
#palabrasClave="results/Palabras/palabrasMAXILPS.csv"
#palabrasClave="results/Palabras/palabrasMAXILR.csv"
#palabrasClave="results/Palabras/palabrasMAXIMI.csv"
#palabrasClave="results/Palabras/palabrasMAXINIS.csv"
#palabrasClave="results/Palabras/palabrasMAXIRIS.csv"


dicPalabras = leerFicheroCSV(palabrasClave)
print(dicPalabras)
escribirKeysUnicas( pathFicheros, rake_object, dicPalabras)
#escribirKeysListado( pathFicheros, rake_object )






#escribirKeys( pathFicheros, rake_object )
#escribirMatriz(pathFicheros, rake_object )

#textos="0,0,0,0,0,0,0,0,5.307509881422925,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5.025510204081632,0,0,5.0301184990125085,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5.141317109616821,0,0,0,0,0,0,0,0,4.890267090525565,5.835540308747856,0,0,0,0,0,0,0,0,0,0,0,0,5.567243035542747,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5.141317109616821,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6.112206975414523,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9.04348509867657,0,0,0,0,0,0,0,0,0,0,0,0,0,6.142908729800487,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6.309826023033571,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.8181818181818181,0,25.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9.771792353299613,0,0,0,6.871215984423532,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5.560049019607844,0,0,0,0,0,0,0,0,0,0,0,0,0,5.4434335117332235,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5.657078770286318,8.953259534766794,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.890267090525565,10.txt"
#normalizarDoc()
#escribirKeys( pathFicheros, rake_object )




