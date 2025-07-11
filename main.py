import os

notas = []

while True:
    titulo = "TO-DO LIST"
    print("\n" + titulo)
    print("-" * len(titulo))
    print("""
1. Crear una nueva nota
2. Ver tus notas
3. Gestionar notas
4. Salir\n""")

    
    try:
        opcion = int(input("Elige que quieres hacer: "))
    except ValueError:
        print("Número no válido...")
        input("Pulsa alguna tecla para continuar... ")
        continue

    if opcion == 1:
        nota = input("Escribe tu nota: ")
        if nota.strip() == "":
            print("Nota vacía")
        else:
            notas.append(nota)
            print("Nota guardada")
            input("Pulsa alguna tecla para continuar... ")
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        print("Saliendo...")
        break