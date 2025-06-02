#primer forma de utilizar los modulos
import modulos

modulos.borrarPantalla()
print(modulos.saludar("Marko Alexander Garcia Naranjo"))

#segunda forma de utilizar los modulos

from modulos import saludar, borrarPantalla

#borrarPantalla()
print(saludar("Marko Alexander Garcia Naranjo"))


nombre=input("Escribe tu nombre: ")
tel=input("Escribe tu telefono: ")
nom,tel=modulos.solicitarDatos4(nombre, tel)
print(f"\tHola {nom}\n\t Tu telefono es {tel}")