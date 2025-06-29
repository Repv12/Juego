import random
#las opciones q hay las guardo en un diccionario para q en vez de escribir la palabra completa solo en numero que funciona como key
elegir = elegir = {
    "1": "piedra",
    "2": "papel",
    "3": "tijera"
}
estadisticas = {}

def elegiropciones(jugador):
    while True:
        print(f"\n{jugador}, escribe tu elección:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        opcion = input("Ingresa 1, 2 o 3: ")
        
        if opcion in elegir:
            return elegir[opcion]
        else:
            print("Opción inválida. Intenta nuevamente.")

#el modo contra pc y multijugador activa esta funcion para empezar el juego
            
            
def ganador(j1,j2):
    if j1 == j2:
        return "Empataron"
    elif (j1 == "piedra" and j2 == "tijera") or\
         (j1 == "papel" and j2 == "piedra") or\
         (j1 == "tijera" and j2 == "papel"):
             return "Jugador 1"
    else:
        return "Jugador 2"

#esta define quien gano
    
def jugar_contrapc():
    jugador = elegiropciones("jugador")
    pc = random.choice(list(elegir.values()))
    print(f"la computadora eligio: {pc}")

# en la libreria random se usa el list para que detecte el diccionario y el .value para q no escoja la key sino el valor q es piedra papel o tijera y no 1,2,3
    resultado = ganador(jugador, pc)
    if resultado == "Empataron":
        print("Empataron")
        print("_________________________________________")
    elif resultado == "Jugador 1":
        print("Ganaste")
        print("_________________________________________")
    else:
        print("Perdiste")
        print("_________________________________________")
        
    estadisticas['modo'] = "contra la computadora"
    estadisticas['jugador_1'] = jugador
    estadisticas['jugador_2'] = pc
    estadisticas['resultado'] = resultado
    
# esta activa la libreria random para jugar contra la pc y activa la funcion elegir opciones para dar las opciones en el juego tambien esta la logica para ver quien gana o pierde
    
def jugar_multijugador():
    print("Turno de Jugador 1")
    jugador1 = elegiropciones("Jugador 1")

    print("Turno de Jugador 2")
    jugador2 = elegiropciones("Jugador 2")

    resultado = ganador(jugador1, jugador2)
    if resultado == "Empate":
        print("¡Empataron")
        print("_________________________________________")
    else:
        print(f"{resultado} ha ganado")
        print("_________________________________________")

    estadisticas['modo'] = "Multijugador"
    estadisticas['jugador_1'] = jugador1
    estadisticas['jugador_2'] = jugador2
    estadisticas['resultado'] = resultado
    
# cuando en la funcion menu principal escogen multijugador esta libreria se activa hace lo mismo q contra pc pero sin el random xq no se debe escoger al azar el jugador dos sino manualmente
    

def ver_estadisticas():
    if not estadisticas:
        print("no hay partidas registradas")
    else:
        print("Estadísticas de la última partida")
        print(f"Modo de juego: {estadisticas['modo']}")
        print(f"Jugador 1 eligió: {estadisticas['jugador_1']}")
        print(f"Jugador 2 o computadora eligió: {estadisticas['jugador_2']}")
        print(f"Ganador: {estadisticas['resultado']}")
        print("_________________________________________")
    
# lo q haya resultado en la partida se guarda en un diccionario estadisticas y luego aqui lo abre
    
def menu_principal():
    while True:
        print("Menu Principal")
        print("1. Jugar contra la computadora")
        print("2. Modo de dos juagadores")
        print("3. Ver estadísticas")
        print("4. Salir")
        print("_________________________________________")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            jugar_contrapc()
        elif opcion == '2':
            jugar_multijugador()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            print("gracias por jugar")
            break
        else:
            print("Opción inválida escribe de nuevo")
            
    # esta es la primera funcion en ejecutarse y hace que se activen las demas segun lo q salga
            
menu_principal()
#Este opcion inicia el juego con la funcion definida 
