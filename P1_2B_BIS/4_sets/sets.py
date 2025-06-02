"""
Sets
Es un tipo de datos para tener una coleccion de valores peo no tiene ni indice ni orden

Set es una coleccion desordenada, inmutable y no indexada. No permite miembros duplicados."""

import os
os.system("clear")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)
#personas.pop()
#print(personas)
#personas.clear()
#print(personas)

varios={3.12,3,True,"Hola"}
print(varios)


#ejemplo crear un programa que solicite los 
#email de los alumnos de la utd almacenar en un lista y posteriormente mostrar en pantalla los email sin duplicados

os.system("clear")
opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame el email: "))
    print(emails)
    opc=input("Deseas agregar otro email? (si/no): ").lower()

#imprimir los emails sin duplicados

print(emails)