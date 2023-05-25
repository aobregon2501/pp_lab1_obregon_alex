#Primer parcial Lav1, Obregón Alex div E

import json 
import csv
import re

with open('C:\\Users\\aobre\\OneDrive\\Documentos\\Prog_I_div_E\\Primer parcial\\datosDreamTeam.json') as archivo:
    data_dream_team = json.load(archivo)

lista_jugadores = data_dream_team["jugadores"]
flag_csv = False

#-------
def mostrar_jugadores(lista:list):
    '''
    Muestra la lista de jugadores con el formato Jugador - Posición.
    Recibe como parametro la lista de jugadores
    '''
    for jugador in lista:
        print("{} - {}".format(jugador["nombre"], jugador["posicion"]))

#-------

def seleccionar_jugador(lista:list) -> int:
    print("id   nombre")
    for id in range(len(lista)):
        print("{0}  {1}".format(id, lista[id]["nombre"]))

    return int(input("Seleccione el id del jugador: "))    

#-------

def mostrar_estadisticas_jugador(lista:list, indice:int) -> list:
    lista_est = []
    lista_est.append(lista[indice]["nombre"])
    lista_est.append(lista[indice]["posicion"])

    print("\nEstadisticas de ", lista[indice]["nombre"])
    for tipo_est, est in lista[indice]["estadisticas"].items():
        print("{0}: {1}".format(tipo_est, est))
        lista_est.append(str(est))
    return lista_est    

#-------

def guardar_estadisticas_csv(lista:list):
    nombre_archivo = lista[0] + ".csv"
    with open(nombre_archivo,"w") as file:
        file.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(
                "nombre","posicion",
                "temporadas","puntos totales",
                "promedio de puntos por partido","rebotes totales",
                "romedio de rebotes por partido","asistencias totales",
                "promedio de asistencias por partido","robos totales",
                "bloqueos totales","porcentaje de tiros de campo",
                "porcentaje de tiros libres","porcentaje de tiros triples"
            ))
        
        file.write("{0}\n".format(",".join(lista)))
            
#--------

def calcular_mayor(lista_jugadores:list, campo:str):
    flag_mayor = True
    for indice in range(len(lista_jugadores)):
        if flag_mayor or lista_jugadores[indice]["estadisticas"][campo] > lista_jugadores[indice_mayor]["estadisticas"][campo]:
            indice_mayor = indice
            flag_mayor = False
    print("El jugador con mayor {0} es {1} con {2}.".format(
        campo,
        lista_jugadores[indice_mayor]["nombre"],
        lista_jugadores[indice_mayor]["estadisticas"][campo]
        ))        
    

#----------

def mas_que_el_valor(lista:list, campo:str):
    valor_str = input("Ingrese el valor a superar: ")
    valor = float(valor_str)

    dict_jugadores = {}

    for jugador in lista_jugadores:
        if jugador["estadisticas"][campo] > valor:
            dict_jugadores[jugador["nombre"]] = jugador["estadisticas"][campo]

    if len(dict_jugadores) > 0:
        for nombre, dato in dict_jugadores.items():
            print("{0}: {1}".format(nombre, dato))
    else:
        print("Ningún jugador superó ese valor.")        

while True:
    print("\n--Menú de Ejercicios--",
          "\n\n1. Listar jugadores.",
          "\n2. Mostrar estadísticas de un jugador.",
          "\n3. Guardar estadísticas en un archivo CSV",
          "\n4.",
          "\n5.",
          "\n6.",
          "\n7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.",
          "\n8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.",
          "\n9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.",
          "\n10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.",
          "\n11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.",
          "\n12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.",
          "\n13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.",
          "\n14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.",
          "\n15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.",
          "\n16.",
          "\n17.",
          "\n18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.",
          "\n19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas",
          "\n20.",
          "\n23.",
          "\n0. Salir.")
    opcion = input("\nIngrese la opción deseada: ")

    
    match opcion:
        case "1":
            mostrar_jugadores(lista_jugadores)
        case "2":
            indice_jugador = seleccionar_jugador(lista_jugadores)
            flag_csv = True
            lista_csv = mostrar_estadisticas_jugador(lista_jugadores, indice_jugador)
        case "3":
           if flag_csv:
               guardar_estadisticas_csv(lista_csv)
           else:
               print("\nNo se mostró ninguna estadística.")   
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            calcular_mayor(lista_jugadores, "rebotes_totales")
        case "8":
            calcular_mayor(lista_jugadores, "porcentaje_tiros_de_campo")
        case "9":
            calcular_mayor(lista_jugadores, "asistencias_totales")
        case "10":
            mas_que_el_valor(lista_jugadores, "promedio_puntos_por_partido")
        case "11":
            mas_que_el_valor(lista_jugadores, "promedio_rebotes_por_partido")
        case "12":
            mas_que_el_valor(lista_jugadores, "promedio_asistencias_por_partido")
        case "13":
            calcular_mayor(lista_jugadores, "robos_totales")
        case "14":
            calcular_mayor(lista_jugadores, "bloqueos_totales")
        case "15":
            mas_que_el_valor(lista_jugadores, "porcentaje_tiros_libres")
        case "16":
             pass
        case "17":
            pass
        case "18":
            mas_que_el_valor(lista_jugadores, "porcentaje_tiros_triples")
        case "19":
            calcular_mayor(lista_jugadores, "temporadas")
        case "20":
            pass
        case "23":
            pass
        case "0":
            break