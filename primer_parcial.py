#Primer parcial Lav1, Obregón Alex div E

import json 
import csv
import re

with open('C:\\Users\\aobre\\OneDrive\\Documentos\\Prog_I_div_E\\Primer parcial\\datosDreamTeam.json') as archivo:
    data_dream_team = json.load(archivo)

lista_jugadores = data_dream_team["jugadores"]

for jugador in lista_jugadores:
    for estadisticas, datos in jugador["estadisticas"].items():
        jugador.update({estadisticas: datos})
    del jugador["estadisticas"]    
print(lista_jugadores)    
        

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

def ingresar_float(frase:str):            
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




def mostrar_logros_jugador(lista:list, campo:str):
    nombre_ingresado = input("Ingrese el nombre del jugador: ").lower()
    lista_logros = []
    while len(nombre_ingresado) > 2:
        for jugador in lista:
            if len(re.findall("^{0}.*| {0}.*".format(nombre_ingresado), jugador[campo].lower())) != 0:
                lista_logros.append(jugador)

        if len(lista_logros) > 0:
            break
        nombre_ingresado = nombre_ingresado[:-1]

    return lista_logros            


'''def ordenar_posision(lista:list):
    lista_posiciones = []
    lista_aux_posicion = []'''


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

def seleccionar_jugador(lista:list) -> int:
    print("id   nombre")
    for id in range(len(lista)):
        print("{0}  {1}".format(id, lista[id]["nombre"]))  
    id_jugador = ingresar_int("Seleccione id del jugador: ")
    return id_jugador
  

#-------

def mostrar_estadisticas_jugador(lista:list, indice:int) -> list:
    lista_est = []
    for tipo_est, est in lista[indice].items():
        if type(est) != list:
            print("{0}: {1}".format(tipo_est, est))
            lista_est.append(str(est))
    
    lista_campos_est = []
    lista_campos_est.extend(lista[indice].keys())
    lista_campos_est.remove("logros")

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
    return lista_logros    

def buscar_mayor(lista:list, campo_a:str, campo_b:str, flag_orden = True, flag_logro = False):
    if flag_logro:
        lista = sumar_logros(lista, campo_a, campo_b)       
    lista_ordenada = quick_sort(lista, campo_b, flag_orden)
    texto = "{0} con {1} {2}.".format(
        lista_ordenada[0][campo_a],
        lista_ordenada[0][campo_b],
        campo_b.replace("_", " "))
    return texto
    

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
        return texto    
    else:
        texto = "\nNingún jugador supero ese valor."
        return texto     


#------

def calcular_promedio(lista:list, campo:str):
    acumulador_puntos = 0
    for indice in range(len(lista)):
        acumulador_puntos += lista[indice][campo]
    promedio_puntos = acumulador_puntos / len(lista)
    print("{0} del equipo: {1}".format(campo.replace("_", " "), promedio_puntos))


            
    

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
            lista_logros = mostrar_logros_jugador(lista_jugadores, "nombre")
            if len(lista_logros) > 0:
                for jugador in lista_logros:
                    print("\n{0}".format(jugador["nombre"]))
                    for logros in range(len(jugador["logros"])):
                        print("{0}".format(jugador["logros"][logros]))      
            else:
                print("\nIngreso invalido.")    
        case "5":
            lista_ordenada = quick_sort(lista_jugadores, True, "nombre")
            calcular_promedio(lista_ordenada, "promedio_puntos_por_partido")
            for jugador in lista_ordenada:
                print("{0}: {1}".format(jugador["nombre"], jugador["promedio_puntos_por_partido"]))
        case "6":
            lista_logros = mostrar_logros_jugador(lista_jugadores, "nombre")
            if len(lista_logros) > 0:
                  for jugador in lista_logros:
                      for logro in range(len(jugador["logros"])):
                          if comparar_patrones(jugador["logros"][logro], "^Miembro del Salon de la Fama del Baloncesto$"):
                              print("{0} es {1}.".format(jugador["nombre"], jugador["logros"][logro]))
                              break
            else:
                print("\nIngreso invalido.")
        case "7":
            texto = buscar_mayor(lista_jugadores,"nombre", "rebotes_totales")
        case "8":
            texto = buscar_mayor(lista_jugadores,"nombre", "porcentaje_tiros_de_campo")
        case "9":
            texto = buscar_mayor(lista_jugadores,"nombre", "asistencias_totales")
        case "10":
            texto = listar_mayores(lista_jugadores, "nombre", "promedio_puntos_por_partido")
        case "11":
            texto = listar_mayores(lista_jugadores, "nombre", "promedio_rebotes_por_partido")
        case "12":
            texto = listar_mayores(lista_jugadores, "nombre", "promedio_asistencias_por_partido")
        case "13":
            texto = buscar_mayor(lista_jugadores,"nombre", "robos_totales")
        case "14":
            texto = buscar_mayor(lista_jugadores,"nombre", "bloqueos_totales")
        case "15":
            texto = listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_libres")
        case "16":
            lista_ordenada = quick_sort(lista_jugadores,"promedio_puntos_por_partido", False)
            calcular_promedio(lista_ordenada[:-1], "promedio_puntos_por_partido")
        case "17":
            texto = buscar_mayor(lista_jugadores,"nombre", "logros", False, True)
        case "18":
            texto = listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_triples")
        case "19":
            texto = buscar_mayor(lista_jugadores,"nombre", "temporadas")
        case "20":
            lista_ordenada = quick_sort(lista_jugadores,"posicion", True)
            lista_mayores = mas_que_el_valor(lista_ordenada, "porcentaje_tiros_de_campo")
            if len(lista_mayores) > 0:
                posicion = lista_mayores[0]["posicion"]
                print("\n{0}:".format(posicion))
                for jugador in lista_mayores:
                    if posicion == jugador["posicion"]:
                        print("{0}: {1}".format(jugador["nombre"], jugador["porcentaje_tiros_de_campo"]))
                    else:
                        posicion = jugador["posicion"]
                        print("\n{0}:\n{1}: {2}".format(posicion, jugador["nombre"], jugador["porcentaje_tiros_de_campo"]))
            else:
                print("\nNingún jugador superó ese valor.")
        case "23":
            pass
        case "0":
            break
    print(texto)