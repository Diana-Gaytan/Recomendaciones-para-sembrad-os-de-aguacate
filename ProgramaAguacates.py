import csv
Lat1= float(input("Introduzca latitud 1 en x: "))
Lon1= float(input("Introduzca longuitud 1 en y: "))
Lat2= float(input("Introduzca latitud 2 en x: "))
Lon2= float(input("Introduzca longuitud 2 en y: "))
#DY = Lat2-Lat1
#DY = Lon2-Lon1
#variables de para la georeferencias
Y = Lat1
X = Lon1
IncY = 1
IncX = 1
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
        print(coordx,",",coordy)
        salida.writerow((coordx,coordy))
    X = Lon1
    print("-------------------------")
del salida
ff.close()
    
#file="PuntosAGUACATE.csv"
#csv=open(file,"w")
#PuntosAGUACATE= [
#    ['coordx','coordy'],
#]
#with open('PuntosAGUACATE.csv', "w", newline= '') as file:
#    writer = csv.writer(file, delimiter= ",")
#    write.writerows(PuntosAGUACATE.csv) 
