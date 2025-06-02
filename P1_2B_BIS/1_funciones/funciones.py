"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas
pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

# 1.- Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    
nombre=input("Escribe tu nombre: ")
tel=input("Escribe tu telefono: ")

print("Soy funcion 1, Hola", nombre, "tu telefono es", tel)

# 3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos3(nombre, tel):
    nom=nombre
    telefono=tel
    print("Soy funcion 3, Hola", nombre, "tu telefono es", tel)

# 2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Escribe tu nombre: ")
    tel=input("Escribe tu telefono: ")

    return f("Hola {nombre} tu telefono es {tel}")

# 4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre, tel):
    nom=nombre
    telefono=tel
    return nom, telefono



#llamar mis funciones
solicitarDatos1()

nombre3=input("Escribe tu nombre: ")
tel3=input("Escribe tu telefono: ")
solicitarDatos3(nombre, tel)

nombre2,tel2=solicitarDatos2()
print(f"Nombre: {nombre2} \n Telefono: {tel2}")

nombre4=input("Escribe tu nombre: ")
tel4=input("Escribe tu telefono: ")
nombre2,tel2=solicitarDatos2(nombre4, tel4)
print(f"Nombre: {nombre4} \n Telefono: {tel4}")