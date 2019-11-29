import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import csv
import math 
#from math import *
Lat1= float(input("Introduzca latitud 1 en x: "))
Lon1= float(input("Introduzca longuitud 1 en y: "))
Lat2= float(input("Introduzca latitud 2 en x: "))
Lon2= float(input("Introduzca longuitud 2 en y: "))
#DY = Lat2-Lat1
#DY = Lon2-Lon1
#variables de para la georeferencias
x1=[]
y1=[]
Y = Lat1
X = Lon1
IncY = 0.34124547
IncX = 0.24315497
#Variables paras el CSV
ff=open("PuntosAGUACATES.csv","w")
salida=csv.writer(ff)
print("Coordenadas para plantar arbolitos")
while Y < Lat2:
    Y = (Y + IncY)
    while X < Lon2:
        X=(X +IncX)
        coordx=X
        coordy=Y
        x1.append(coordx)
        y1.append(coordy)
        print(coordx,",",coordy)
        salida.writerow((coordx,coordy))
    X = Lon1
    print("-------------------------")
del salida
ff.close()

print (x1)
print (y1)


plt.plot(x1,y1, 'o', Label='Aguacates')
plt.xlabel('x1')
plt.ylabel('y1')
plt.title('Aguacates Cliente')
plt.legend()
plt.show()

#file="PuntosAGUACATE.csv"
#csv=open(file,"w")
#PuntosAGUACATE= [
#    ['coordx','coordy'],
#]
#with open('PuntosAGUACATE.csv', "w", newline= '') as file:
#    writer = csv.writer(file, delimiter= ",")
#    write.writerows(PuntosAGUACATE.csv) 
