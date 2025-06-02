"""

List(Array)
son colleciones o conjuntos de datos/valores bajo un mismo nombre, para acceder a los valores se utiliza un indice numerico

Nots: sus valores si son modificables

La lista es una colección ordenada y mutable de elementos, que permite almacenar múltiples valores en una sola variable.

"""
#Funciones mas comunes de las listas

paises=["Mexico", "Brasil", "España", "Canada"]

numeros=[23, 12, 100, 34]

#Ordenar ascendentemente

print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Ingresar elementos a una lista

#1er forma: append
paises.append("Honduras")

#2da forma: insert
paises.insert(1, "Honduras")
print(paises)

#Eliminar elementos de una lista

#1er forma: pop
paises.pop(1)
print(paises)

#2da forma: remove
paises.remove("Honduras")
print(paises)

#Buscar un elemento en una lista

#1er forma

resp="Brasil" in paises
if resp:
    print("El pais se encuentra en la lista")
else:
    print("No se encuentra el pais")


#2da forma

for i in range(0,len(paises)):
    if paises[i]=="Brasil":
        print("Si encontre el pais")
    else:
        print("No encontre el pais")

#Buscar cuantas veces aparece un elemento dentro de una lista

#numeros=[23,12,100,34]

print(f"Este numero 12 aparece:{numeros.count(12)} veces")

numeros.append(12)
print(f"Este numero 12 aparece:{numeros.count(12)} veces")


#Identificar y conocer el indice de un valor

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de la lista

#1er forma con valores
for i in paises:
    print(i)

#2da forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es:{paises[i]}")

#Unir contenido de listas

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)