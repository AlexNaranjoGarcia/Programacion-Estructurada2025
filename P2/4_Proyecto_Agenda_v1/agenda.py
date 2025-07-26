def borrarPantalla():
    import os
    # Comando para limpiar la pantalla en Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para limpiar la pantalla en sistemas Unix/Linux/MacOS
    else:
        os.system('clear')

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def menu_principal():
    borrarPantalla()
    print("\n\t\t\t..::: Sistema de Gestion de Agenda de Contactos :::...\n\t\t 1.- Agregar contacto\n\t\t 2.- Mostrar todos los contactos\n\t\t 3.- Buscar por nombre\n\t\t 4.- Salir")
    opcion = input("\n\t\tElige una opción (1-4): ").upper()
    return opcion

def agregarContacto():
    borrarPantalla()
    print("\t..:: Agregar Contacto ::..")
    nombre = input("\nIngrese el nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("El contacto ya existe. Por favor, ingrese un nombre diferente.")
    else:
        telefono = input("Ingrese el número de teléfono: ").strip()
        email = input("Ingrese el E-mail: ").lower().strip()
        #Agregar el atributo "nombre" al diccionario con los valores de telefono y email en una lista
        agenda[nombre] = [telefono, email]
        print(f"\n\t\t Contacto {nombre} agregado exitosamente.")
    
    print("Contacto agregado exitosamente.")

def mostrarContactos():
    borrarPantalla()
    print("\n\t\t..:: Mostrar Contactos ::..")
    if not agenda:
        print("No hay contactos registrados.")
    else:
        for nombre, datos in agenda.items():
            print(f"\n\t{'nombre:' +nombre}\n\t{'Telefono:'+datos[0]}\n\t{'Email:'+datos[1]}")
    try:
        with open("contactos.txt", "r") as file:
            contactos = file.readlines()
        
        if not contactos:
            print("No hay contactos registrados.")
            return
        
        print("\nContactos registrados:")
        for contacto in contactos:
            nombre, telefono, email = contacto.strip().split(",")
            print(f"Nombre: {nombre}, Teléfono: {telefono}, Email: {email}")
    
    except FileNotFoundError:
        print("No se encontraron contactos registrados.")

def buscarContactoPorNombre():
    borrarPantalla()
    print("\t..:: Buscar Contacto por Nombre ::..")
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ").upper().strip()
    
    try:
        with open("contactos.txt", "r") as file:
            contactos = file.readlines()
        
        encontrado = False
        for contacto in contactos:
            nombre, telefono, email = contacto.strip().split(",")
            if nombre == nombre_buscar:
                print(f"Contacto encontrado: Nombre: {nombre}, Teléfono: {telefono}, Email: {email}")
                encontrado = True
                break
        
        if not encontrado:
            print("Contacto no encontrado.")
    
    except FileNotFoundError:
        print("No se encontraron contactos registrados.")

def modificarContacto():

    borrarPantalla()
    print("\t..:: Modificar Contacto ::..")
    nombre_modificar = input("Ingrese el nombre del contacto a modificar: ").upper().strip()
    
    if nombre_modificar not in agenda:
        print("Contacto no encontrado.")
        return
    
    telefono = input("Ingrese el nuevo número de teléfono: ").strip()
    email = input("Ingrese el nuevo E-mail: ").lower().strip()
    
    agenda[nombre_modificar] = [telefono, email]
    print(f"\n\t\t Contacto {nombre_modificar} modificado exitosamente.")

def eliminarContacto():    
    borrarPantalla()
    print("\t..:: Eliminar Contacto ::..")
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
    
    if nombre_eliminar not in agenda:
        print("Contacto no encontrado.")
        return
    
    del agenda[nombre_eliminar]
    print(f"\n\t\t Contacto {nombre_eliminar} eliminado exitosamente.")