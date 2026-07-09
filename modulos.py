import random
import json
import pygame
import time

def creador_diccionario(marca,opcion1,opcion2,opcion3,opcion4,opcion_correcta,):
    diccionario = {
        "Marca" : marca,
        "opcion 1" :opcion1,
        "opcion 2" : opcion2,
        "opcion 3" : opcion3,
        "opcion 4" : opcion4, 
        "opcion correcta": opcion_correcta
        }
    return diccionario

def pone_lista(lista:list,marca:int,opcion1:str,opcion2:str,opcion3:str,opcion4:str,opcion_correcta):
    usu = creador_diccionario(marca,opcion1,opcion2,opcion3,opcion4,opcion_correcta)
    lista.append(usu)

marcas_diccionario =[
    {"numero": 1, "imagen1": r"Imagenes\apple\apple3.jpg", "imagen2": r"Imagenes\apple\apple2.jpg", "imagen3": r"Imagenes\apple\apple1.jpg", "imagen4": r"Imagenes\apple\apple4.jpg", "opcion_correcta": 3},
    {"numero": 2, "imagen1": r"Imagenes\chanel\chanel4.webp", "imagen2": r"Imagenes\chanel\chanel2.jpg", "imagen3": r"Imagenes\chanel\chanel3.jpg", "imagen4": r"Imagenes\chanel\chanel1.jpg", "opcion_correcta": 4},
    {"numero": 3, "imagen1": r"Imagenes\chrome\chrome3.jpg", "imagen2": r"Imagenes\chrome\chrome2.jpg", "imagen3": r"Imagenes\chrome\chrome5.jpg", "imagen4": r"Imagenes\chrome\chrome4.jpg", "opcion_correcta": 2},
    {"numero": 4, "imagen1": r"Imagenes\facebook\facebook1.jpg", "imagen2": r"Imagenes\facebook\facebook2.jpg", "imagen3": r"Imagenes\facebook\facebook3.jpg", "imagen4": r"Imagenes\facebook\facebook4.jpg", "opcion_correcta": 4},
    {"numero": 5, "imagen1": r"Imagenes\instagram\instagram2.jpg", "imagen2": r"Imagenes\instagram\instagram1.jpg", "imagen3": r"Imagenes\instagram\instagram3.jpg", "imagen4": r"Imagenes\instagram\instagram4.jpg", "opcion_correcta": 2},
    {"numero": 6, "imagen1": r"Imagenes\mcdonalds\mcdonalds1.jpg","imagen2": r"Imagenes\mcdonalds\mcdonalds2.jpg","imagen3": r"Imagenes\mcdonalds\mcdonalds3.jpg","imagen4": r"Imagenes\mcdonalds\mcdonalds4.jpg","opcion_correcta" : 1},
    {"numero": 7, "imagen1": r"Imagenes\nba\nba1.jpg","imagen2": r"Imagenes\nba\nba2.jpg","imagen3": r"Imagenes\nba\nba3.jpg","imagen4": r"Imagenes\nba\nba4.jpg","opcion_correcta" : 1},
    {"numero": 8, "imagen1": r"Imagenes\nike\nike4.jpg","imagen2": r"Imagenes\nike\nike2.jpg","imagen3": r"Imagenes\nike\nike3.jpg","imagen4": r"Imagenes\nike\nike1.jpg","opcion_correcta" : 4},
    {"numero": 9, "imagen1": r"Imagenes\pepsi\pepsi4.jpg","imagen2": r"Imagenes\pepsi\pepsi2.webp","imagen3": r"Imagenes\pepsi\pepsi3.jpg","imagen4": r"Imagenes\pepsi\pepsi1.webp","opcion_correcta" : 2},
    {"numero": 10,"imagen1": r"Imagenes\pinterest\pinterest3.jpg","imagen2": r"Imagenes\pinterest\pinterest2.jpg","imagen3": r"Imagenes\pinterest\pinterest1.jpg","imagen4": r"Imagenes\pinterest\pinterest4.jpg","opcion_correcta" : 3},
    {"numero": 11,"imagen1": r"Imagenes\python\python3.jpg","imagen2": r"Imagenes\python\python2.jpg","imagen3": r"Imagenes\python\python1.jpg","imagen4": r"Imagenes\python\python4.jpg","opcion_correcta" : 3},
    {"numero": 12,"imagen1": r"Imagenes\telegram\telegram1.jpg","imagen2": r"Imagenes\telegram\telegram2.jpg","imagen3": r"Imagenes\telegram\telegram3.jpg","imagen4": r"Imagenes\telegram\telegram4.jpg","opcion_correcta" : 1},
    {"numero": 13,"imagen1": r"Imagenes\twitter\twitter2.jpg","imagen2": r"Imagenes\twitter\twitter1.jpg","imagen3": r"Imagenes\twitter\twitter3.jpg","imagen4": r"Imagenes\twitter\twitter4.jpg","opcion_correcta" : 2},
    {"numero": 14,"imagen1": r"Imagenes\windows\windows2.jpg", "imagen2": r"Imagenes\windows\windows1.jpg","imagen3":r"Imagenes\windows\windows3.jpg","imagen4": r"Imagenes\windows\windows4.jpg","opcion_correcta" : 2},
    {"numero": 15,"imagen1": r"Imagenes\youtube\youtube3.jpg", "imagen2": r"Imagenes\youtube\youtube2.jpg","imagen3": r"Imagenes\youtube\youtube1.jpg","imagen4": r"Imagenes\youtube\youtube4.jpg","opcion_correcta" : 3}
]

def random_numero(lista_numeros_usados:set, inicio:int, fin:int) -> int:
    numero_random = random.randint(inicio, fin)
    while numero_random in lista_numeros_usados:
        numero_random = random.randint(inicio, fin)
    lista_numeros_usados.add(numero_random)
    return numero_random

def cargar_imagen(ruta, dimensiones):
    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen, dimensiones)

def get_superficie(printeable:int,fuente,color):
    printeable_str = str(printeable)          
    renderizado = fuente.render(printeable_str,True,color)
    return renderizado

def get_rectangulo(imagen,dimensiones:tuple):
    rectangulo_imagen = imagen.get_rect()
    rectangulo_imagen.topleft = dimensiones
    return rectangulo_imagen

def tiempo_cuenta_atras(tiempo_a_pasar:int,inicio_de_tiempo:float):
    tiempo_actual = time.time()    
    tiempo_que_paso = tiempo_actual - inicio_de_tiempo
    int_tiempo_que_paso = int(tiempo_que_paso)
    tiempo_printeable = tiempo_a_pasar - int_tiempo_que_paso 
    return tiempo_printeable

def cargar_imagen_rectangulo_blit(superficie,imagen,tamaño_imagen:tuple,ibicacion_imagen:tuple):
    imagen_1 = cargar_imagen(imagen,tamaño_imagen)
    rect_opcion_a_juego = get_rectangulo(imagen_1,ibicacion_imagen)
    superficie.blit(imagen_1,rect_opcion_a_juego.topleft)
    return rect_opcion_a_juego

def switch_bool(bandera:bool)->bool:
    if bandera == True:
        bandera = False
    else:
        bandera = True
    return bandera

def swap(a: int, b: int):
    '''
    Cambia el contendido de a con el de b
    '''
    return b,a 

def ordenar_lista(score:list) -> list:
    '''
    Ordena la lista otorgada segun los parametros 
    otorgados, en ascendente o en descendente. Si son INT
    '''
    for i in range(0, len(score)-1):
        for j in range(i + 1, len(score)):
                if score[i] < score[j] :
                    score[i],score[j] = swap(score[i],score[j])
    return score

def cambiar_banderas(matriz, indice_y, indice_x):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = False
    matriz[indice_y][indice_x] = True
    return matriz

def sonido_alternar(sonido_diccionario : dict,bandera_sonido,volumen_bajo,silenciar,volumen_alto):
    match bandera_sonido:
        case 3:
            bandera_sonido = 2
            sonido = volumen_bajo
            sonido_diccionario["click"].set_volume(0.9)
            sonido_diccionario["error"].set_volume(0.08)
            sonido_diccionario["moneda"].set_volume(0.09)
            sonido_diccionario["perdiste"].set_volume(0.09)
            sonido_diccionario["mal"].set_volume(0.09)
            sonido_diccionario["gay"].set_volume(0.080)
        case 2:
            bandera_sonido = 1
            sonido = silenciar
            sonido_diccionario["click"].set_volume(0)
            sonido_diccionario["error"].set_volume(0)
            sonido_diccionario["moneda"].set_volume(0)
            sonido_diccionario["perdiste"].set_volume(0)
            sonido_diccionario["mal"].set_volume(0)
            sonido_diccionario["gay"].set_volume(0)
        case 1: 
            bandera_sonido = 3
            sonido = volumen_alto
            sonido_diccionario["click"].set_volume(5)
            sonido_diccionario["error"].set_volume(5)
            sonido_diccionario["moneda"].set_volume(5)
            sonido_diccionario["perdiste"].set_volume(5)
            sonido_diccionario["mal"].set_volume(5)
            sonido_diccionario["gay"].set_volume(3)
    return bandera_sonido,sonido