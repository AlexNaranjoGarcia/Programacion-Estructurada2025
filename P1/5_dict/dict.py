"""" 
dict.-
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos
 tiene alfanumericos. Es decir es algo parecido como los Objetos

Tambien se conoce como arreglo asociativo u Objeto JSON

El diccionario es una collecion ordenada y modificable. no hay miembros duplicados.
"""
import os
os.system("clear")

#Lista
#paises={"Mexico", "Brasil", "Canada", "España",}

#Dict o objeto
pais_mexico={
        "nombre":"Mexico",
        "capital":"CDMX",
        "poblacion":120000000,
        "idioma":"Español",
        "status":True
        }

pais_brasil={
            "nombre":"Brasil",
            "capital":"Brasilia",
            "poblacion":1000000,
            "idioma":"portugues",
            "status": True
        }

pais_canada={
            "nombre":"Canada",
            "capital":"Ottawa",
            "poblacion":9000000,
            "idioma":{"ingles","frances"},
            "status": True
        }

alumno1={
            "nombre":"Ramiro",
            "apellido_paterno":"Perez",
            "apellido_materno":"Lopez",
            "carrera":"Sistemas",
            "area":"Software Multiplataforma",
            "modalidad":"Bilingue",
            "matricula":"123456",
            "semestre": "2"
    }

#Mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo
alumno1["telefono"]="1234567890"
for i in alumno1:
    print(f"{i}={alumno1[i]}")