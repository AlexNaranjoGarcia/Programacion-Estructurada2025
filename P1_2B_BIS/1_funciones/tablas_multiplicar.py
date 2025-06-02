"""
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Requisitos:
    Con funciones que regrese valor y utilice parametros
"""
# Tabla del 2
numero=input("Dame un numero para calcular la tabla de multiplicar: ")
multi=numero*1
print(f"2 x 1 = {multi}" )
multi=numero*2
print(f"2 x 2 = {multi}" )
multi=numero*3
print(f"2 x 3 = {multi}" )
multi=numero*4
print(f"2 x 4 = {multi}" )
multi=numero*5
print(f"2 x 5 = {multi}" )
multi=numero*6
print(f"2 x 6 = {multi}" )
multi=numero*7
print(f"2 x 7 = {multi}" )
multi=numero*8
print(f"2 x 8 = {multi}" )
multi=numero*9
print(f"2 x 9 = {multi}" )
multi=numero*10
print(f"2 x 10 = {multi}" )
#version 2

numero=input("Dame un numero para calcular la tabla de multiplicar: ")
for i in range(1,11):
    multi=numero*i
    print(f"{numero} x {i} = {multi}" )

numero=int(input("Dame un numero para calcular la tabla de multiplicar: "))
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}" )
    i+=1

# version 3

def calcular_tabla(numero, limite=10):
    tabla = []
    for i in range(1, limite + 1):
        resultado = numero * i
        tabla.append(resultado)
    return tabla

def imprimir_tabla(numero, resultados):
    print(f"\nTabla de multiplicar del {numero}:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        numero = int(input("Ingrese el número para la tabla de multiplicar: "))
        limite = int(input("Ingrese hasta qué múltiplo desea calcular (por defecto 10): ") or 10)
        
        resultados = calcular_tabla(numero, limite)
        

        imprimir_tabla(numero, resultados)
        
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    main()