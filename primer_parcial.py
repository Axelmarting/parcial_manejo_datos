from funciones_p_parcial import starwars_app
import json

def parse_json(nombre_archivo:str):
    """
    Un parametro: ruta de acceso a archivo con datos
    Toma los valores del archivo, carga los valores del archivo(dict) en una variable y luego lo retorna con la clave "results".
    """
    with open (nombre_archivo,"r") as archivo:
        dict_json = json.load(archivo)
    return dict_json["results"]

list_starwars = parse_json(r"C:\Users\Axel\Desktop\Programacion_1\PARCIAL_1\data.json")

starwars_app(list_starwars)