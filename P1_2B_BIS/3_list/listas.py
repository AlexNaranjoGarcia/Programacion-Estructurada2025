#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numeros)

for i in numeros:
    print(i)

for i in range(0, len(numeros)):
    print(numeros[i])


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras = [ "Pez", "Gol", "Azul", "Sushi", "Xilofono", "Migaja", "Cavernicola"]
print(palabras)

palabras[0]="Pez"
palabras[1]="Gol"
palabras[2]="Azul"
palabras[3]="Sushi"
palabras[4]="Xilofono"
palabras[5]="Migaja"
palabras[6]="Cavernicola"

print(palabras)

#1er forma
palabra_buscar = input("Ingrese la palabra a buscar: ")
if palabra_buscar in palabras:
    print(f"La palabra '{palabra_buscar}' se encuentra en la lista.")
    print(f"El numero de veces que se encontro la palabra es:{palabras.count}")
else:
    print(f"La palabra '{palabra_buscar}' no se encuentra en la lista.")

#2da forma
encontro = False
for i in palabras:
    if i == palabra_buscar:
        encontro= True
        print(f"La palabra '{palabra_buscar}' se encuentra en la posición {i} de la lista.")
    else:
        print(f"La palabra '{palabra_buscar}' no se encuentra en la posición {i} de la lista.")

if encontro:
    print(f"Si encontro la palabra")
else:
    print(f"No encontro la palabra")


input("Oprima cualquier tecla:")



#Ejemplo 3 Agregar elementos a una lista
import os

os.system("clear")
numeros=[]
print(numeros)

opc=True

while opc:
    numero=float(input("Dame un numero entero o decimal"))
    numeros.append(numero)
    resp=input("Deseas agregar otro numero?").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)
input("Oprima cualquier tecla para continuar...")

#Ejmeplo 4 Crear una lista multidimensional que sea una agenda

agenda=[
        ["Carlos", "6181234567"]
        ["Alberto", "6671234567"]
        ["Martin", "6785678923"]
        ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0, 3):
    for c in range(0, 2):
       # print(agenda[r][c])
        cadena+=f"[{agenda[r][c]}]"
    cadena+="\n"
        
        #print(f"Nombre: {agenda[r][0]}, Telefono: {agenda[r][1]}")