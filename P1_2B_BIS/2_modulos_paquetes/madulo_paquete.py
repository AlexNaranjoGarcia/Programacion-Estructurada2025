#un modulo es simplemente un archivo con extension pyque contiene codigo de python (funciones, clases, variables, etc)

#un paquete es una carpeta que contiene varios moduos (archivos .py) y un archivo __init__.py que indica que la carpeta es un paquete

import os

def solicitarDatos1():
    nombre=input("Escribe tu nombre: ")
    tel=input("Escribe tu telefono: ")
    print("Soy funcion 1, Hola", nombre, "tu telefono es", tel)

def solicitarDatos3(nombre, tel):
    nom=nombre
    telefono=tel
    print("Soy funcion 3, Hola", nombre, "tu telefono es", tel)

def solicitarDatos2():
    nombre=input("Escribe tu nombre: ")
    tel=input("Escribe tu telefono: ")
    return (f"Hola {nombre} tu telefono es {tel}")

def solicitarDatos4(nombre, tel):
    nom=nombre
    telefono=tel
    return nom, telefono

def borrarPantalla():
    import os

def esperetecla():
    input("Presiona una tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido {nom}"