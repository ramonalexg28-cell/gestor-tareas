tareas = []

contador=0

while True:
            print("Agregar tarea")
            print("Ver tareas")
            print("Eliminar tareas")
            print("Salir")

            option = input("Elige una opción: " )

        #Agregar tarea
            if option == "1":
                nombre = input("Escripe el nombre de la tarea: " )
                if nombre.strip() =="":
                    print("Escribe un nombre a la tarea")
                tareas.append(nombre)
                print(f"✅ Tarea '{nombre}' agregada")
                
            elif option == "2":
                if len(tareas)==0:
                    print("no hay tareas")
                else:
                    print("\n Lista de tareas:") 
                    for i in range(len(tareas)):
                        print(f"{i + 1}. {tareas[i]}")
            elif option == "3":
                nombre = input("Escribe el nombre de la tarea: ")
                if nombre in tareas:
                    tareas.remove(nombre)
                else:
                    print("No existe esa tarea")
            elif option == "4":
                print("Hasta luego")
                break  # Termina el bucle y el programa
    
            # Opción inválida
            else:
                print("❌ Opción no válida, intenta del 1 al 4")