import re

def menu_principal() -> str:
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
        "\n21. BONUS",
        "\n0. Finalizar programa.")


def ingresar_int(frase:str) -> int:
    '''
    Funcion que convierte una cadena de caracteres en un numero entero
    Recibe como parámetro una cadena de caracteres para usar como frase de input
    Devuelve un numero entero
    '''
    while True:
        numero = input(frase)
        if comparar_patrones(numero, '^[0-9]+$'):
            return int(numero)
        else:
            print("Ingreso invalido.")


def ingresar_float(frase:str) -> float:  
    '''
    Funcion que convierte una cadena de caracteres en un numero flotante
    Recibe como parámetro una cadena de caracteres para usar como frase de input
    Devuelve un numero flotante
    '''          
    while True:
        numero = input(frase)
        if comparar_patrones(numero, '^([0-9]*)(\.|,*)([0-9]+)$'):
            return float(numero.replace(",","."))
        else:
            print("Ingreso invalido.")

def mostrar_en_pantalla(texto:str):
    '''
    Funcion que muestra un texto en pantalla
    Recibe como parámetro una cadena de caracteres para usar como texto a mostrar
    '''
    print(texto)  



def comparar_patrones(texto:str, patron:str) -> bool:
    '''
    Funcion que compara una cadena de caracteres con un patron
    Recibe como parámetro una cadena de caracteres y un patron
    Devuelve True si el patron coincide con la cadena de caracteres
    '''
    if len(re.findall(patron, texto)) != 0:
        return True
    else:
        return False    
    

def mostrar_jugadores(lista:list, campo_a:str, campo_b:str):
    '''
    Muestra la lista de jugadores con el formato Jugador - Posición.
    Recibe como parametro la lista de jugadores y dos strings que definen los campos de la lista a mostrar
    '''
    texto = "\n"
    for jugador in lista:
        texto += "{} - {}\n".format(jugador[campo_a], jugador[campo_b])
    mostrar_en_pantalla(texto)    



def seleccionar_jugador(lista:list, campo_a:str) -> int:
    '''
    Funcion que muestra los jugadores con el formato Id - Jugador
    Recibe como parámetro la lista de jugadores y un string que define el campo de la lista a seleccionar
    Devuelve el id del jugador seleccionado
    '''
    texto = "id     {0}\n".format(campo_a)
    for id in range(len(lista)):
        texto += "{0} - {1}\n".format(id, lista[id][campo_a])
    print(texto)    
    id_jugador = ingresar_int("Seleccione id del jugador: ")
    return id_jugador    


def mostrar_estadisticas_jugador(lista:list, campo_a:str, campo_b:str) -> list:
    '''
    Funcion que muestra las estadísticas del jugador seleccionado mediante id, y preparar una lista con los datos para un archivo CSV.
    Recibe como parámetro la lista de jugadores y dos strings que definen los campos del jugador a mostrar(rebotes totales, puntos totales, asistencias totales, etc)
    Devuelve una lista con los datos del jugador seleccionado para poder generar un archivo CSV
    '''
    id_jugador = seleccionar_jugador(lista, campo_a)
    texto = "\n"
    lista_csv = []
    if id_jugador < len(lista):
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
    mostrar_en_pantalla(texto)    

    return lista_csv



def preparar_lista_csv(lista:list) -> str:
    '''
    Funcion que prepara una lista en formato CSV 
    Recibe como parámetro una lista
    Devuelve una cadena de caracteres en formato CSV: "dato_a,dato_b,dato_c\n"
    '''
    return "{0}\n".format(",".join(lista))



def guardar_csv(lista_datos:list, nombre_archivo:str):
    '''
    Funcion que guarda datos en formato CSV
    Recibe como parámetro una lista con los datos a guardar y un string para definir el nombre del archivo
    '''
    nombre_archivo += ".csv"
    with open(nombre_archivo,"w") as file:
        for lista in lista_datos:
            file.write(preparar_lista_csv(lista))
        mostrar_en_pantalla("\nDatos guardados en archivo csv.")



def quick_sort(lista:list, campo:str, flag_orden:bool) -> list:
    '''
    Funcion que genera una lista ordenada mediante el metodo quick_sort
    Recibe como parámetro la lista a ordenar, la key para saber el campo mediante el cual ordenar(rebotes totales, puntos totales, asistencias totales, etc)
    y un flag que define si se ordena de manera ascendente o descendente
    Devuelve la lista recivida de manera ordenada
    '''
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



def calcular_promedio(lista:list, campo:str) -> str:
    '''
    Funcion que calcula el promedio de una lista mediante el campo indicado
    Recibe la lista de jugadores y el campo el cual promediar
    Devuelve una string con el formato: "campo del equipo: promedio"
    '''
    acumulador_puntos = 0
    for indice in range(len(lista)):
        acumulador_puntos += lista[indice][campo]
    promedio_puntos = acumulador_puntos / len(lista)
    texto = "\n{0} del equipo: {1}\n".format(campo.replace("_", " ").capitalize(), promedio_puntos)
    return texto



def buscar_nombre(lista:list, campo:str) -> list:
    '''
    Funcion que compara una lista de strings con el patron ingresado
    Recibe como parametro una lista y un string que define el campo de la lista, en este caso el nombre
    Devuelve una lista con las coincidencias encontradas
    '''
    nombre_ingresado = input("Ingrese el nombre del jugador: ").lower()
    lista_nombres = []
    while len(nombre_ingresado) > 2:
        for jugador in lista:
            if comparar_patrones(jugador[campo].lower(), "^{0}.*| {0}.*".format(nombre_ingresado)):
                lista_nombres.append(jugador)

        if len(lista_nombres) > 0:
            break
        else:
            nombre_ingresado = nombre_ingresado[:-1]

    return lista_nombres  



def sumar_logros(lista:list, campo_a:str, campo_b:str) -> list:
    '''
    Funcion que suma los logros de los jugadores en una lista y busca cual es mayor
    Recibe como parámetro la lista de jugadores y dos strings que definen los campos de la lista a sumar, en este caso los logros
    Devuelve una lista ordenada de en base a los logros
    '''
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



def buscar_mayor(lista:list, campo_a:str, campo_b:str, flag_orden = False) -> list:
    '''
    Funcion que toma el elemnto mayor de una lista y lo muestra en pantalla
    Recibe como parametro la lista de jugadores, dos strings que definen los campos a ordenar(rebotes totales, puntos totales, asistencias totales, etc),
    y un flag para determinar si se ordena de manera ascendente o descendente
    Devuelve la lista ordenada en base al campo de que recibe
    '''    
    lista_ordenada = quick_sort(lista, campo_b, flag_orden)
    texto = "{0} con {1} {2}.".format(
        lista_ordenada[0][campo_a],
        lista_ordenada[0][campo_b],
        campo_b.replace("_", " "))
    mostrar_en_pantalla(texto)
    return lista_ordenada




def mas_que_el_valor(lista:list, campo:str) -> list:
    '''
    Funcion que genera una lista en base a los que superen el valor del input
    Recibe como parametro la lista y el campo el cual va a comparar con el input(promedio de rebotes, promedio de puntos, promedio de asistencias, etc)
    Devuelve una lista con los jugadores que superen el valor del input
    '''
    valor = ingresar_float("Ingrese el valor a superar: ")

    lista_mayores = []

    for jugador in lista:
        if jugador[campo] > valor:
            lista_mayores.append(jugador)

    return lista_mayores 




def listar_mayores(lista:list, campo_a:str, campo_b:str):
    '''
    Funcion que muestra en pantalla los jugadores que superen el input, puede no haber ninguno
    Recibe como parametro la lista de jugadores y dos strings que definen los campos a ordenar(promedio de rebotes, promedio de puntos, promedio de asistencias, etc)
    '''
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



def mostrar_posicion(lista, campo_a:str, campo_b:str, campo_c:str) -> str:
    '''
    Funcion que muestra en pantalla los jugadores con el formato:
        posicion:
        nombre_a: dato_a
        nombre_b: dato_b
    Recibe como parametro la lista de jugadores, y 3 strings que definen los campos a mostrar(posicion, nombre y porcentaje de tiros de campo)
    Retorna un string en el formato establecido
    '''
    posicion = lista[0][campo_b]
    texto = "\n{0}:".format(posicion)
    for jugador in lista:
        if posicion == jugador[campo_b]:
            texto += "\n{0}: {1}".format(jugador[campo_a], jugador[campo_c])
        else:
            posicion = jugador[campo_b]
            texto += "\n\n{0}:\n{1}: {2}".format(posicion, jugador[campo_a], jugador[campo_c])
    return texto





def acoplar_rankings(puntos:list, rebotes:list, asistencias:list, robos:list, lista_encabezado:list):
    '''
    Funcion que ordena el ranking de los jugadores de manera que se prepare para guardar en un archivo CSV
    Recibe como parametro 5 listas, las primeras 4 corresponden a los jugadores ordenados en campos diferentes(puntos, rebotes, asistencias, robos)
    la quinta lista corresponde al "encabezado" del archivo CSV
    Una vez generada la lista pide generar un CSV con el formato:
    nombre      puntos      rebotes     asistencias     robos
    nombre_A    punto_A     rebote_A    asistencias_A   robos_A
    nombre_B    punto_B     rebote_B    asistencias_B   robos_B
    '''
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
    '''
    Funcion que busca el indice de un nombre en una lista
    Recibe como parametro el nombre a comparar, una lista con los jugadores y el campo "nombre"
    Retorna el indice del nombre en la lista
    '''
    for indice in range(len(lista)):
        if nombre == lista[indice][campo]:
            return str(indice + 1)    