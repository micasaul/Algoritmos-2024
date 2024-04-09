# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# A. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
# B. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;
# C. Utilizar un vector para representar la mochila.

from random import randint

def usar_la_fuerza (mochila, contador=0):
    objeto= mochila[randint(0, len(mochila))]

    if len(mochila)>0:
        if objeto == "sable de luz":
            print (f"encontró el sable de luz despues de {contador} objetos")
        else:
            print(f"el objeto encontrado fue: {objeto}")
            mochila.remove(objeto)
            return usar_la_fuerza(mochila, contador+1)
    else:
        print ("la mochila no contiene un sable de luz")

mochila=["botella", "sable de luz", "globo", "chocolate", "sahumerio"]

usar_la_fuerza(mochila)