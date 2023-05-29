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
  
texto = ""  
flag_csv = False
lista_csv = []
ranking_robos = []
ranking_rebotes = []
ranking_asistencias = []

while True:
    fp.menu_principal()
    opcion = fp.ingresar_int("\nIngrese la opción deseada: ")
    if opcion < 22:
        match opcion:
            case 1:
                lista_ordenada = fp.quick_sort(lista_jugadores,"posicion", True)
                fp.mostrar_jugadores(lista_ordenada, "nombre", "posicion")
            case 2:
                lista_estadisticas = fp.mostrar_estadisticas_jugador(lista_jugadores, "nombre", "posicion")
                flag_csv = True
                lista_csv = lista_estadisticas
            case 3:
                if flag_csv and len(lista_csv) > 0:
                    fp.guardar_csv(lista_csv, lista_csv[1][0])
                else:
                    fp.mostrar_en_pantalla("\nNo se mostró ninguna estadística.")     
            case 4:
                lista_logros = fp.buscar_nombre(lista_jugadores, "nombre")
                if len(lista_logros) > 0:
                    texto = ""
                    for jugador in lista_logros:
                        texto += "\n\n{0}".format(jugador["nombre"])
                        for logros in range(len(jugador["logros"])):
                            texto += "\n{0}".format(jugador["logros"][logros])     
                else:
                    texto = "\nIngreso invalido."  
                fp.mostrar_en_pantalla(texto)     
            case 5:
                lista_ordenada = fp.quick_sort(lista_jugadores,"nombre", True)
                texto = fp.calcular_promedio(lista_ordenada, "promedio_puntos_por_partido")
                for jugador in lista_ordenada:
                    texto += "{0}: {1}\n".format(jugador["nombre"], jugador["promedio_puntos_por_partido"])
                fp.mostrar_en_pantalla(texto)     
            case 6:
                lista_logros = fp.buscar_nombre(lista_jugadores, "nombre")
                if len(lista_logros) > 0:
                    texto = "\n"
                    for jugador in lista_logros:
                            if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                                texto += "{0} es Miembro del Salon de la Fama del Baloncesto.\n".format(jugador["nombre"])
                            else:
                                texto += "{0} NO es Miembro del Salon de la Fama del Baloncesto.\n".format(jugador["nombre"])      
                else:
                    texto = "\nIngreso invalido."
                fp.mostrar_en_pantalla(texto)   
            case 7:
                ranking_rebotes = fp.buscar_mayor(lista_jugadores,"nombre", "rebotes_totales")
            case 8:
                fp.buscar_mayor(lista_jugadores,"nombre", "porcentaje_tiros_de_campo")
            case 9:
                ranking_asistencias = fp.buscar_mayor(lista_jugadores,"nombre", "asistencias_totales")
            case 10:
                fp.listar_mayores(lista_jugadores, "nombre", "promedio_puntos_por_partido")
            case 11:
                fp.listar_mayores(lista_jugadores, "nombre", "promedio_rebotes_por_partido")
            case 12:
                fp.listar_mayores(lista_jugadores, "nombre", "promedio_asistencias_por_partido")
            case 13:
                ranking_robos = fp.buscar_mayor(lista_jugadores,"nombre", "robos_totales")
            case 14:
                fp.buscar_mayor(lista_jugadores,"nombre", "bloqueos_totales")
            case 15:
                fp.listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_libres")
            case 16:
                lista_ordenada = fp.quick_sort(lista_jugadores,"promedio_puntos_por_partido", False)
                texto = fp.calcular_promedio(lista_ordenada[:-1], "promedio_puntos_por_partido")
                fp.mostrar_en_pantalla(texto)
            case 17:
                fp.sumar_logros(lista_jugadores, "nombre", "logros")
            case 18:
                fp.listar_mayores(lista_jugadores, "nombre", "porcentaje_tiros_triples")
            case 19:
                fp.buscar_mayor(lista_jugadores,"nombre", "temporadas")
            case 20:
                lista_mayores = fp.mas_que_el_valor(lista_jugadores, "porcentaje_tiros_de_campo")
                if len(lista_mayores) > 0:
                    lista_ordenada = fp.quick_sort(lista_mayores,"posicion", True)
                    texto = fp.mostrar_posicion(lista_ordenada, "nombre", "posicion", "porcentaje_tiros_de_campo")
                else:
                    texto = "\nNingún jugador superó ese valor."
                fp.mostrar_en_pantalla(texto)     
            case 21:
                ranking_puntos = fp.quick_sort(lista_jugadores, "puntos_totales", False)
                if ranking_rebotes == list():
                    ranking_rebotes = fp.quick_sort(lista_jugadores, "rebotes_totales", False)
                if ranking_asistencias == list():
                    ranking_asistencias = fp.quick_sort(lista_jugadores, "asistencias_totales", False)
                if ranking_robos == list():
                    ranking_robos = fp.quick_sort(lista_jugadores, "robos_totales", False)    

                lista_encabezado = ["nombre", "puntos totales", "rebotes totales", "asistencias totales", "robos totales"]    
                fp.acoplar_rankings(ranking_puntos, ranking_rebotes, ranking_asistencias, ranking_robos, lista_encabezado)    
            case 0:
                break
    else:
        fp.mostrar_en_pantalla("\nOpcion no valida.")    
    input("\nOprima cualquier tecla para continuar...")