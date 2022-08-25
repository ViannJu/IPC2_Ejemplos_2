from estructura import ListaCircular

#listaCircular = ListaCircular()

if __name__ == "__main__":
    listaCircular = ListaCircular() 
    nodoActual = None
    while True:
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Imprimir")
        print("4. Graficar")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            valor = input("Ingrese un valor: ")
            listaCircular.insertar(valor)

        elif opcion == "2":
            valor = input("Ingrese un valor: ")
            listaCircular.eliminar(valor)

        elif opcion == "3":
            listaCircular.imprimir()

        elif opcion == "4":
            listaCircular.graficar()
        
        elif opcion == "5":
            break
        
        else:
            print("Opcion incorrecta")