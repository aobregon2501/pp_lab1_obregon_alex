#Primer parcial Lav1, Obregón Alex div E

import json 
import csv
import re

with open('C:\\Users\\aobre\\OneDrive\\Documentos\\Prog_I_div_E\\Primer parcial\\datosDreamTeam.json') as archivo:
    data_dream_team = json.load(archivo)

lista_jugadores = data_dream_team["jugadores"]
flag_csv = False


#-------

def comparar_patrones(texto:str, patron:str):
    if re.search(patron, texto):
        return True
    else:
        return False

def ingresar_int(frase:str):
    while True:
        numero = input(frase)
        if comparar_patrones(numero, '^[0-9]+$'):
            return int(numero)
        else:
            print("Ingreso invalido.")

def ingreso_float(frase:str):            
    while True:
        numero = input(frase)
        if comparar_patrones(numero, '^([0-9]*)(\.|,*)([0-9]+)$'):
            return float(numero.replace(",","."))
        else:
            print("Ingreso invalido.")

#-------
def mostrar_jugadores(lista:list):
    '''
    Muestra la lista de jugadores con el formato Jugador - Posición.
    Recibe como parametro la lista de jugadores
    '''
    for jugador in lista:
        print("{} - {}".format(jugador["nombre"], jugador["posicion"]))



def mostrar_logros_jugador(lista):
    mostrar_jugadores(lista)
    nombre_ingresado = input("Ingrese el nombre del jugador: ")
    dict_logros = {}
#-------

def seleccionar_jugador(lista:list) -> int:
    print("id   nombre")
    for id in range(len(lista)):
        print("{0}  {1}".format(id, lista[id]["nombre"]))  
    id_jugador = ingresar_int("Seleccione id del jugador: ")
    return id_jugador
  

#-------

def mostrar_estadisticas_jugador(lista:list, indice:int) -> list:
    lista_est = []
    lista_est.append(lista[indice]["nombre"])
    lista_est.append(lista[indice]["posicion"])
    print(lista_est[0])
    for tipo_est, est in lista[indice]["estadisticas"].items():
        print("{0}: {1}".format(tipo_est, est))
        lista_est.append(str(est))
    
    lista_campos_est = []
    lista_campos_est.extend(lista[indice].keys())
    lista_campos_est.remove("estadisticas")
    lista_campos_est.remove("logros")
    lista_campos_est.extend(lista[indice]["estadisticas"].keys())

    return lista_est, lista_campos_est    

#-------

def preparar_csv(lista:list) -> str:
    return "{0}\n".format(",".join(lista))

def guardar_csv(lista_datos:list, lista_encabezado:list):
    nombre_archivo = lista_datos[0] + ".csv"
    with open(nombre_archivo,"w") as file:
        file.write(preparar_csv(lista_encabezado))
        file.write(preparar_csv(lista_datos))
            
#--------

def buscar_mayor_estadistica(lista:list, campo:str):
    dict_est = {}
    for jugador in lista:
        dict_est[jugador["nombre"]] = jugador["estadisticas"][campo]
    calcular_mayor(dict_est, campo.replace("_", " "))  

def calcular_mayor(dict_est:dict, campo:str):
    flag_primero = True
    for nombre, dato in dict_est.items():
        if flag_primero or dato > mayor:
            mayor = dato
            nombre_mayor = nombre
            flag_primero = False
    print("{0} con {1} {2}.".format(nombre_mayor, mayor, campo))    

def buscar_mayores_logros(lista:list, campo:str):
    dict_logros = {}
    for jugador in lista:
        acumulador_logros = 0
        for logro in jugador[campo]:
            if comparar_patrones(logro, "([0-9]+) veces"):
                numero_str = re.sub(" veces.*", "", logro)
                acumulador_logros += int(numero_str)
            else:
                acumulador_logros += 1
        dict_logros[jugador["nombre"]] = acumulador_logros
    calcular_mayor(dict_logros, campo)                
    

#----------

def mas_que_el_valor(lista:list, campo:str):
    valor = ingreso_float("Ingrese el valor a superar: ")

    dict_jugadores = {}

    for jugador in lista:
        if jugador["estadisticas"][campo] > valor:
            dict_jugadores[jugador["nombre"]] = jugador["estadisticas"][campo]

    if len(dict_jugadores) > 0:
        for nombre, dato in dict_jugadores.items():
            print("{0}: {1}".format(nombre, dato))
    else:
        print("Ningún jugador superó ese valor.")

#------

def calcular_promedio(lista:list):
    flag_primero = True
    acumulador_puntos = 0
    for indice in range(len(lista)):
        acumulador_puntos += lista[indice]["estadisticas"]["promedio_puntos_por_partido"]
        if flag_primero or lista[indice]["estadisticas"]["promedio_puntos_por_partido"] < lista[indice_menor]["estadisticas"]["promedio_puntos_por_partido"]:
            indice_menor = indice
            flag_primero = False
    acumulador_puntos -= lista[indice_menor]["estadisticas"]["promedio_puntos_por_partido"]
    promedio_puntos = acumulador_puntos / (len(lista) - 1)
    print(promedio_puntos)
            
    

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
          "\n17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.",
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
            if indice_jugador < len(lista_jugadores):
                lista_csv, lista_campos = mostrar_estadisticas_jugador(lista_jugadores, indice_jugador)
            else:
                print("Id invalido.")    
        case "3":
           if flag_csv:
               guardar_csv(lista_csv, lista_campos)
           else:
               print("\nNo se mostró ninguna estadística.")   
        case "4":
            mostrar_logros_jugador(lista_jugadores)
        case "5":
            pass
        case "6":
            pass
        case "7":
            buscar_mayor_estadistica(lista_jugadores, "rebotes_totales")
        case "8":
            buscar_mayor_estadistica(lista_jugadores, "porcentaje_tiros_de_campo")
        case "9":
            buscar_mayor_estadistica(lista_jugadores, "asistencias_totales")
        case "10":
            mas_que_el_valor(lista_jugadores, "promedio_puntos_por_partido")
        case "11":
            mas_que_el_valor(lista_jugadores, "promedio_rebotes_por_partido")
        case "12":
            mas_que_el_valor(lista_jugadores, "promedio_asistencias_por_partido")
        case "13":
            buscar_mayor_estadistica(lista_jugadores, "robos_totales")
        case "14":
            buscar_mayor_estadistica(lista_jugadores, "bloqueos_totales")
        case "15":
            mas_que_el_valor(lista_jugadores, "porcentaje_tiros_libres")
        case "16":
            calcular_promedio(lista_jugadores)
        case "17":
            buscar_mayores_logros(lista_jugadores, "logros")
        case "18":
            mas_que_el_valor(lista_jugadores, "porcentaje_tiros_triples")
        case "19":
            buscar_mayor_estadistica(lista_jugadores, "temporadas")
        case "20":
            pass
        case "23":
            pass
        case "0":
            break