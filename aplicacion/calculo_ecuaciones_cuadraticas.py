from math import *
import math as dx
a=int(input("Ingrese el termino cuadratico: "))
b=int(input("Ingrese el termino lineal, sino existe ponga 0 "))
c=int(input("Ingrese el termino independiente, sino existe ponga 0"))
discr= b**2-4*a*c
if discr>0:
    solpos= (-b+dx.sqrt(b**2-4*a*c))/2*a
    solneg= (-b-dx.sqrt(b**2-4*a*c))/2*a
    print("si hay solucion en el conjunto de los numeros reales, la primera es: ",solpos," y la segunda es: ",solneg)
elif discr<0:
    print("La ecuacion no tiene solucion en el conjunto de los numeros reales :(")