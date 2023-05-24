#Primer parcial Lav1, Obregón Alex div E

import json 

with open('C:\\Users\\aobre\\OneDrive\\Documentos\\Prog_I_div_E\\Primer parcial\\datosDreamTeam.json') as archivo:
    data_dream_team = json.load(archivo)

lista_jugadores = data_dream_team["jugadores"]

def mostrar_jugadores(lista:list):
    '''
    Muestra la lista de jugadores con el formato Jugador - Posición.
    Recibe como parametro la lista de jugadores
    '''
    for jugador in lista:
        print("{} - {}".format(jugador["nombre"], jugador["posicion"]))



while True:
    print("\n--Menú de Ejercicios--",
          "\n\n1. Listar jugadores.",
          "\nEj 2.",
          "\nEj 3.",
          "\nEj 4.",
          "\nEj 5.",
          "\nEj 6.",
          "\nEj 7.",
          "\nEj 8.",
          "\nEj 9.",
          "\nEj 10.",
          "\nEj 11.",
          "\nEj 12.",
          "\nEj 13.",
          "\nEj 14.",
          "\nEj 15.",
          "\nEj 16.",
          "\nEj 17.",
          "\nEj 18.",
          "\nEj 19.",
          "\nEj 20.",
          "\nEj 21.",
          "\n0. Salir.")
    opcion = input("\nIngrese la opción deseada: ")

    
    match opcion:
        case "1":
            mostrar_jugadores(lista_jugadores)
        case "2":
            pass
        case "3":
           pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "14":
            pass
        case "15":
            pass
        case "16":
             pass
        case "17":
            pass
        case "18":
            pass
        case "19":
            pass
        case "20":
            pass
        case "21":
            pass
        case "0":
            break