#Primer parcial Lav1, Obregón Alex div E

import json 
import csv
import re
import funciones_parcial as fp

with open('C:\\Users\\aobre\\OneDrive\\Documentos\\Prog_I_div_E\\Primer parcial\\datosDreamTeam.json') as archivo:
    data_dream_team = json.load(archivo)

lista_jugadores = data_dream_team["jugadores"]

for jugador in lista_jugadores:
    for estadisticas, datos in jugador["estadisticas"].items():
        jugador.update({estadisticas: datos})
    del jugador["estadisticas"]    
print(lista_jugadores)    
        

flag_csv = False
lista_csv = []
ranking_robos = []
ranking_rebotes = []
ranking_asistencias = []


#-------

def comparar_patrones(texto:str, patron:str):
    if len(re.findall(patron, texto)) != 0:
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

def ingresar_float(frase:str):            
    while True:
        numero = input(frase)
        if comparar_patrones(numero, '^([0-9]*)(\.|,*)([0-9]+)$'):
            return float(numero.replace(",","."))
        else:
            print("Ingreso invalido.")

def mostrar_en_pantalla(texto:str):
    print(texto)            

#-------
def mostrar_jugadores(lista:list):
    '''
    Muestra la lista de jugadores con el formato Jugador - Posición.
    Recibe como parametro la lista de jugadores
    '''
    texto = "\n"
    for jugador in lista:
        texto += "{} - {}\n".format(jugador["nombre"], jugador["posicion"])
    mostrar_en_pantalla(texto)   




def mostrar_logros_jugador(lista:list, campo:str):
    nombre_ingresado = input("Ingrese el nombre del jugador: ").lower()
    lista_logros = []
    while len(nombre_ingresado) > 2:
        for jugador in lista:
            if comparar_patrones(jugador[campo].lower(), "^{0}.*| {0}.*".format(nombre_ingresado)):
                lista_logros.append(jugador)

        if len(lista_logros) > 0:
            break
        nombre_ingresado = nombre_ingresado[:-1]

    return lista_logros            




def quick_sort(lista:list, campo:str, flag_orden:bool):
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0][campo]
        for dato in lista[1:]:
            if flag_orden:
                if dato[campo] > pivot:
                    lista_de.append(dato)
                else:
                    lista_iz.append(dato) 
            else:
                if dato[campo] < pivot:
                    lista_de.append(dato)
                else:
                    lista_iz.append(dato)
    lista_iz = quick_sort(lista_iz,campo, flag_orden)
    lista_iz.append(lista[0])              
    lista_de = quick_sort(lista_de,campo, flag_orden)
    lista_iz.extend(lista_de)       
    return lista_iz           

#-------

def seleccionar_jugador(lista:list, campo_a:str) -> int:
    texto = "id     {0}\n".format(campo_a)
    for id in range(len(lista)):
        texto += "{0} - {1}\n".format(id, lista[id][campo_a])
    print(texto)    
    id_jugador = ingresar_int("Seleccione id del jugador: ")
    return id_jugador
  

#-------

def mostrar_estadisticas_jugador(lista:list, campo_a:str, campo_b:str) -> list:
    id_jugador = seleccionar_jugador(lista_jugadores, campo_a)
    texto = "\n"
    lista_csv = []
    if id_jugador < len(lista_jugadores):
        lista_est = []
        for tipo_est, est in lista[id_jugador].items():
            if type(est) != list:
                if tipo_est != campo_b:
                    texto += "{0}: {1}\n".format(tipo_est.replace("_", " ").capitalize(), est)
                lista_est.append(str(est))
        lista_campos_est = []
        lista_campos_est.extend(lista[id_jugador].keys())
        lista_campos_est.remove("logros")
        lista_csv.append(lista_campos_est)
        lista_csv.append(lista_est)
    else:
        texto += "Id invalido."    

    return lista_csv, texto    

#-------

def preparar_lista_csv(lista:list) -> str:
    return "{0}\n".format(",".join(lista))

def guardar_csv(lista_datos:list, nombre_archivo:str):
    nombre_archivo += ".csv"
    with open(nombre_archivo,"w") as file:
        for lista in lista_datos:
            file.write(preparar_lista_csv(lista))
            
#--------  

def sumar_logros(lista:list, campo_a:str, campo_b:str):
    lista_logros = []
    for jugador in lista:
        dict_logros = {}
        acumulador_logros = 0
        for logro in jugador[campo_b]:
            if comparar_patrones(logro, "([0-9]+) veces"):
                numero_str = re.sub(" veces.*", "", logro)
                acumulador_logros += int(numero_str)
            else:
                acumulador_logros += 1
        dict_logros[campo_a] = jugador[campo_a]
        dict_logros[campo_b] = acumulador_logros
        lista_logros.append(dict_logros) 
    lista_ordenada = buscar_mayor(lista_logros, campo_a, campo_b) 
    return lista_ordenada

def buscar_mayor(lista:list, campo_a:str, campo_b:str, flag_orden = False):    
    lista_ordenada = quick_sort(lista, campo_b, flag_orden)
    texto = "{0} con {1} {2}.".format(
        lista_ordenada[0][campo_a],
        lista_ordenada[0][campo_b],
        campo_b.replace("_", " "))
    mostrar_en_pantalla(texto)
    return lista_ordenada

#----------

def mas_que_el_valor(lista:list, campo:str):
    valor = ingresar_float("Ingrese el valor a superar: ")

    lista_mayores = []

    for jugador in lista:
        if jugador[campo] > valor:
            lista_mayores.append(jugador)

    return lista_mayores  
    

def listar_mayores(lista:list, campo_a:str, campo_b:str):
    lista_mayores = []
    lista_mayores = mas_que_el_valor(lista, campo_b)
    texto = "\n{0}    {1}\n".format(campo_a, campo_b.replace("_", " "))
    if len(lista_mayores) > 0:
        for jugador in lista_mayores:
            texto += "{0}: {1}\n".format(jugador[campo_a], jugador[campo_b])
        mostrar_en_pantalla(texto)    
    else:
        texto = "\nNingún jugador supero ese valor."
        mostrar_en_pantalla(texto) 


#------

def calcular_promedio(lista:list, campo:str):
    acumulador_puntos = 0
    for indice in range(len(lista)):
        acumulador_puntos += lista[indice][campo]
    promedio_puntos = acumulador_puntos / len(lista)
    texto = "\n{0} del equipo: {1}\n".format(campo.replace("_", " ").capitalize(), promedio_puntos)
    return texto


def mostrar_posicion(lista, campo_a:str, campo_b:str, campo_c:str):
    posicion = lista[0][campo_b]
    texto = "\n{0}:".format(posicion)
    for jugador in lista:
        if posicion == jugador[campo_b]:
            texto += "\n{0}: {1}".format(jugador[campo_a], jugador[campo_c])
        else:
            posicion = jugador[campo_b]
            texto += "\n{0}:\n{1}: {2}".format(posicion, jugador[campo_a], jugador[campo_c])
    mostrar_en_pantalla(texto)       

    

def acoplar_rankings(puntos:list, rebotes:list, asistencias:list, robos:list, lista_encabezado:list):
    lista_rankings = []
    lista_rankings.append(lista_encabezado)
    for indice in range(len(puntos)):
        lista_auxiliar = []
        lista_auxiliar.append(puntos[indice][lista_encabezado[0]])
        lista_auxiliar.append(str(indice + 1))
        lista_auxiliar.append(buscar_indice(puntos[indice][lista_encabezado[0]], rebotes, lista_encabezado[0]))
        lista_auxiliar.append(buscar_indice(puntos[indice][lista_encabezado[0]], asistencias, lista_encabezado[0]))
        lista_auxiliar.append(buscar_indice(puntos[indice][lista_encabezado[0]], robos, lista_encabezado[0]))
        lista_rankings.append(lista_auxiliar)
    guardar_csv(lista_rankings, "BONUS")    


def buscar_indice(nombre:str, lista:list, campo:str):
    for indice in range(len(lista)):
        if nombre == lista[indice][campo]:
            return str(indice + 1)

while True:
    print("\n--Menú de Ejercicios--",
          "\n\n1. Listar jugadores.",
          "\n2. Mostrar estadísticas de un jugador.",
          "\n3. Guardar estadísticas en un archivo CSV",
          "\n4. Permitir al usuario buscar un jugador por su nombre y mostrar sus logros.",
          "\n5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.",
          "\n6. Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.",
          "\n7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.",
          "\n8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.",
          "\n9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.",
          "\n10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.",
          "\n11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.",
          "\n12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.",
          "\n13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.",
          "\n14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.",
          "\n15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.",
          "\n16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.",
          "\n17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.",
          "\n18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.",
          "\n19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas",
          "\n20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.",
          "\n23.",
          "\n0. Salir.")
    opcion = input("\nIngrese la opción deseada: ")

    
    match opcion:
        case "1":
            lista_ordenada = quick_sort(lista_jugadores,"posicion", True)
            mostrar_jugadores(lista_ordenada)
        case "2":
            lista_estadisticas, texto = mostrar_estadisticas_jugador(lista_jugadores, "nombre", "posicion")
            flag_csv = True
            lista_csv = lista_estadisticas
            mostrar_en_pantalla(texto)
        case "3":
            if flag_csv and len(lista_csv) > 0:
                guardar_csv(lista_csv, lista_csv[1][0])
                texto = "\nDatos guardados en archivo csv."
            else:
                texto = "\nNo se mostró ninguna estadística."   
            mostrar_en_pantalla(texto)     
        case "4":
            lista_logros = mostrar_logros_jugador(lista_jugadores, "nombre")
            if len(lista_logros) > 0:
                texto = ""
                for jugador in lista_logros:
                    texto += "\n\n{0}".format(jugador["nombre"])
                    for logros in range(len(jugador["logros"])):
                        texto += "\n{0}".format(jugador["logros"][logros])     
            else:
                texto = "\nIngreso invalido."  
            mostrar_en_pantalla(texto)     
        case "5":
            lista_ordenada = quick_sort(lista_jugadores,"nombre", True)
            texto = calcular_promedio(lista_ordenada, "promedio_puntos_por_partido")
            for jugador in lista_ordenada:
                texto += "{0}: {1}\n".format(jugador["nombre"], jugador["promedio_puntos_por_partido"])
            mostrar_en_pantalla(texto)     
        case "6":
            lista_logros = mostrar_logros_jugador(lista_jugadores, "nombre")
            if len(lista_logros) > 0:
                  texto = "\n"
                  for jugador in lista_logros:
                        if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                            texto += "{0} es Miembro del Salon de la Fama del Baloncesto.\n".format(jugador["nombre"])
                        else:
                            texto += "{0} NO es Miembro del Salon de la Fama del Baloncesto.\n".format(jugador["nombre"])      
            else:
                texto = "\nIngreso invalido."
            mostrar_en_pantalla(texto)     
        case "7":
            ranking_rebotes = buscar_mayor(lista_jugadores,"nombre", "rebotes_totales")
        case "8":
            buscar_mayor(lista_jugadores,"nombre", "porcentaje_tiros_de_campo")
        case "9":
            ranking_asistencias = buscar_mayor(lista_jugadores,"nombre", "asistencias_totales")
        case "10":
            listar_mayores(lista_jugadores, "nombre", "promedio_puntos_por_partido")
        case "11":
            listar_mayores(lista_jugadores, "nombre", "promedio_rebotes_por_partido")
        case "12":
            listar_mayores(lista_jugadores, "nombre", "promedio_asistencias_por_partido")
        case "13":
            ranking_robos = buscar_mayor(lista_jugadores,"nombre", "robos_totales")
        case "14":
            buscar_mayor(lista_jugadores,"nombre", "bloqueos_totales")
        case "15":
            listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_libres")
        case "16":
            lista_ordenada = quick_sort(lista_jugadores,"promedio_puntos_por_partido", False)
            texto = calcular_promedio(lista_ordenada[:-1], "promedio_puntos_por_partido")
            mostrar_en_pantalla(texto)
        case "17":
            sumar_logros(lista_jugadores, "nombre", "logros")
        case "18":
            listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_triples")
        case "19":
            buscar_mayor(lista_jugadores,"nombre", "temporadas")
        case "20":
            lista_mayores = mas_que_el_valor(lista_jugadores, "porcentaje_tiros_de_campo")
            if len(lista_mayores) > 0:
                lista_ordenada = quick_sort(lista_mayores,"posicion", True)
                texto = mostrar_posicion(lista_ordenada, "nombre", "posicion", "porcentaje_tiros_de_campo")
            else:
                texto = "\nNingún jugador superó ese valor."
            mostrar_en_pantalla(texto)     
        case "23":
            ranking_puntos = quick_sort(lista_jugadores, "puntos_totales", False)
            if ranking_rebotes == list():
                ranking_rebotes = quick_sort(lista_jugadores, "rebotes_totales", False)
            if ranking_asistencias == list():
                ranking_asistencias = quick_sort(lista_jugadores, "asistencias_totales", False)
            if ranking_robos == list():
                ranking_robos = quick_sort(lista_jugadores, "robos_totales", False)    

            lista_encabezado = ["nombre", "puntos totales", "rebotes totales", "asistencias totales", "robos totales"]    
            acoplar_rankings(ranking_puntos, ranking_rebotes, ranking_asistencias, ranking_robos, lista_encabezado)    
        case "0":
            break
    input("...")