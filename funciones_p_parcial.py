import re
#-----------------------------------------------------PUNTO 1--------------------------------------      

def obtener_alturas(lista:list):  #1.1
    """
    Un parametro: lista de datos.
    Esta funcion crea una lista con solo las alturas de todos los personajes.
    """
    lista_copia = lista.copy()
    lista_alturas = []

    for elemento in lista_copia:
        lista_alturas.append(int(elemento["height"]))
    return lista_alturas

def preguntar_usuario_orden(): #1.2
    """
    Pregunta al usuario el orden "asc" o "desc" y retorna la respuesta
    """
    respuesta = input("Ingrese el orden que quiera(asc o desc): ").lower()
    while respuesta != "asc" and respuesta !="desc":
        respuesta = input("Error ingrese el orden que quiera(asc o desc): ").lower()
    return respuesta


def ordenar_alturas(lista_a_ordenar:list, orden:str)->list: #1.3
    """
    Dos parametros: lista de alturas(obtenida en 1.1) y orden("asc" o "desc")(obtenido en 1.2)
    Valida que la lista no este vacia.
    Hace el metodo de ordenamiento quicksort para ordenar la lista de alturas.
    retorna la lista ordenada.
    """
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        lista_copia = lista_a_ordenar.copy() 
        lista_iz = []
        lista_de = []
        pivot = lista_a_ordenar[0]

        if orden == "asc":                
            for elemento in lista_copia[1:]:
                if elemento > pivot:
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
        if orden == "desc":                
            for elemento in lista_copia[1:]:
                if elemento < pivot:
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
        lista_iz = ordenar_alturas(lista_iz, orden)
        lista_iz.append(pivot)
        lista_de = ordenar_alturas(lista_de, orden)

    return lista_iz + lista_de

def starwars_imprimir_alturas_ordenadas(lista: list): #1.4
    """
    Un paramentro: lista de datos
    Le asigna los parametros correscpondientes a cada funcion.
    Imprime lo que retorno la funcion 1.3 
    """
    lista_alturas = obtener_alturas(lista) #1.1
    orden = preguntar_usuario_orden() #1.2
    lista_ordenada = ordenar_alturas(lista_alturas, orden) #1.3
    print(lista_ordenada)

#-----------------------------------------------------PUNTO 3------------------------------------------
def obtener_pesos(lista:list)->list:  #3.1
    """
    Un parametro: lista de datos.
    Esta funcion crea una lista con solo los pesos de todos los personajes.
    """
    lista_copia = lista.copy()
    lista_pesos = []

    for elemento in lista_copia:
        lista_pesos.append(int(elemento["mass"]))
    return lista_pesos

def starwars_imprimir_pesos_ordenados(lista:list): #3.2
    """
    Un paramentro: lista de datos
    Le asigna los parametros correscpondientes a cada funcion.
    Imprime la lista ordenada obtenida de la funcion 1.3.
    """
    lista_pesos = obtener_pesos(lista) #3.1
    orden = preguntar_usuario_orden() #1.2
    lista_ordenada = ordenar_alturas(lista_pesos, orden) #1.3
    print(lista_ordenada)

#-----------------------------------------------------PUNTO 2-------------------------------------------

def buscar_max_altura(lista:list, sexo:str): #2.1
    """
    Recibe como parametro la lista de datos y la clave sexo("male", "female", "n/a").
    Crea una bandera para buscar el nombre del personaje mas alto.
    Retorna el nombre.
    """
    lista_copia = lista.copy()
    bandera_max = 0
    for elemento in lista_copia:
        if elemento["gender"] == sexo:
            if bandera_max == 0:
                max_altura = float(elemento["height"])
                max_nombre = elemento["name"]
                bandera_max = 1
            elif float(elemento["height"]) > float(max_altura):
                max_altura = float(elemento["height"])
                max_nombre = elemento["name"]

    return max_nombre

def starwars_imprimir_max_altura_sexo(lista:list): #2.2
    """
    Un parametro: lista de datos
    Le asigna los parametros correscpondientes a cada funcion.
    Imprime los nombres mas altos de cada sexo.
    """
    male_altura_max = buscar_max_altura(lista, "male") #2.1
    print("\nEl mas alto masculino es: ", male_altura_max)

    female_altura_max = buscar_max_altura(lista, "female") #2.1
    print("El mas alto femenino es: ", female_altura_max)

    na_altura_max = buscar_max_altura(lista, "n/a") #2.1
    print("El mas alto n/a es: ", na_altura_max)

#------------------------------------------------------PUNTO 4--------------------------------------------

def validar_personaje(personaje:str)->bool: #4.1
    """
    Un parametro: nombre del personaje.
    Valida que sea un nombre valido.
    Retorna True de serlo, False de lo contrario.
    """
    if personaje in["luke skywalker", "c-3po", "r2-d2", "darth vader", "leia organa", "owen lars", "beru whitesun lars",
                    "r5-d4", "biggs darklighter", "obi-wan kenobi"]:
        return True
    else:
        return False

def preguntar_usuario_personaje()->str: #4.2
    """
    Le pregunta al usuario el nombre del personaje que desea buscar.
    Lo valida con la funcion 4.1.
    De ser correcto, retorna la respuesta.
    """
    respuesta = input("Que personaje desea buscar? ").lower()
    while validar_personaje(respuesta) == False: #4.1
        respuesta = input("Error, ingrese un personaje valido: ").lower()
    return respuesta

def buscador_personaje(lista:list): #4.3
    """
    Un parametro: lista de datos.
    Itera la lista copiada y pregunta si la variable retornada de la funcion 4.2 es igual al elemento["name"], de serlo
    retorna el dict del personaje. Si no, sigue con el siguiente.
    """
    lista_copiada = lista.copy()
    personaje = preguntar_usuario_personaje() #4.2

    for elemento in lista_copiada:
        if elemento["name"].lower() == personaje:
            return elemento
        else:
            continue

def starwars_imprimir_personaje_buscado(lista:list): #4.4
    """
    Un parametro: lista de datos
    Le asigna los parametros correscpondientes a cada funcion.
    Imprime el dict del personaje buscado en la funcion 4.3 formateado de una forma mas linda.
    """
    personaje_buscado = buscador_personaje(lista) #4.3
    print("\nNombre: {0}\nAltura: {1}\nPeso: {2}\nGenero: {3}".format(personaje_buscado["name"],personaje_buscado["height"],
                                                                        personaje_buscado["mass"],personaje_buscado["gender"]))

#------------------------------------------------------PUNTO 5--------------------------------------------
def starwars_importar_csv(nombre_archivo:str, lista:list): #5
    """
    Dos parametros: ruta de acceso y lista de datos.
    Le asigna los parametros correscpondientes a cada funcion.
    Exporta la lista de alturas casteada a str al archivo csv.
    """
    lista_alturas = obtener_alturas(lista) #1.1
    orden = preguntar_usuario_orden() #1.2
    lista_ordenada = ordenar_alturas(lista_alturas, orden) #1.3

    elementos_convertidos = map(str, lista_ordenada)

    string = ",".join(elementos_convertidos)

    with open(nombre_archivo,"w") as archivo:
        archivo.write(string)

    print("\nLista exportada al archivo csv.")

# -----------------------------------------------ACA EMPIEZA EL MENU DE OPCIONES------------------------------------------
def imprimir_menu():
        menu = ("\n1-Alturas ordenadas\n2-Mas alto de cada sexo\n3-Pesos ordenados\n4-Buscador personajes\n"
                "5-Importar lista personajes ordenada(punto 1) a csv\n6-Salir del programa")
        print(menu)

def validar_entero(numero:str)->bool:
    if numero.isdigit():
        return True
    else:
        return False


def starwars_menu_principal():
    imprimir_menu()
    opcion = input("Seleccione una opcion(1-6): ")

    if validar_entero(opcion) == False:
        print("No es digito")
    else:
        opcion = int(opcion)
        while opcion < 1 or opcion > 6:
            opcion = input("Error, seleccione una opcion(1-6): ")
    return int(opcion)        


def starwars_app(lista:list):
    """
    Unico parametro es la lista de datos
    Esta funcion es el menu
    """
    while True:

        opcion = starwars_menu_principal()

        if opcion == 1:
            starwars_imprimir_alturas_ordenadas(lista) #1

        if opcion == 2:
            starwars_imprimir_max_altura_sexo(lista) #2
        
        if opcion == 3:
            starwars_imprimir_pesos_ordenados(lista) #3

        if opcion == 4:
            starwars_imprimir_personaje_buscado(lista) #4

        if opcion == 5:
            starwars_importar_csv(r"C:\Users\Axel\Desktop\Programacion_1\PARCIAL_1\punto_5_parcial.csv", lista) #5

        if opcion == 6:
            print("FIN DEL PROGRAMA")
            break


        
      


