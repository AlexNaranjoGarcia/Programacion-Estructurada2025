import os

import agenda

opcion=True
while opcion:
    
    print("\n\t\t\t..::: Sistema de Gestion de Agenda de Contactos :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar contacto  \n\t\t 2.- Mostrar todos los contactos \n\t\t 3.- Buscar por nombre \n\t\t 4.- Salir")
    opcion=input("\n\t\tElige una opción (1-4): ").upper()

    match opcion:
        case "1":
            agenda.agregarContacto()
            agenda.esperarTecla()
        case "2":
            agenda.mostrarContactos()
            agenda.esperarTecla()
        case "3":
            agenda.buscarContactoPorNombre() 
            agenda.esperarTecla()
        case "4":
            opcion=False    
            agenda.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
            agenda.esperarTecla()


