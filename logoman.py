import pygame
from modulos import *
import time 

#COLORES
colores = {
    "NEGRO" : (0,0,0),
    "ROJO" : (255,0,0),
    "VERDE" : (0,255,0)
}

resolucion_ventana = (1280,720)

#BANDERAS
bandera_juego = True
bandera_ig = False
bandera_ig_2 = False
while_juego = True
musica_bandera = False
bandera_sonido = 2

#LISTAS
lista_numeros_usados = set()
lista_marcas = []
score_max = []
matriz_banderas = [
    [True,False,False],
    [False,False,False]]
promedio = lambda x: int(x / len(lista_numeros_usados)) 

#CONTADORES
coins = 0
record_coins = -1000
coins_totales = 0
contador_gatos = 0

ventana = pygame.display.set_mode(resolucion_ventana)
pygame.init()

################FUENTES###################
fuente = pygame.font.SysFont("Courier",37)
pygame.display.set_caption("Logoman")
fuente_2 = pygame.font.SysFont("Fixedsys",60)

#################ELEMENTOS GRAFICOS################
corazones = pygame.image.load(r"elementos_graficos\corazonn.png")
silenciar = r"elementos_graficos\silenciar.png"
volumen_bajo = r"elementos_graficos\volumen-bajo.png"
volumen_alto = r"elementos_graficos\alto-volumen.png"
musica_on = r"elementos_graficos\musica.png"
musica_off = r"elementos_graficos\pixil-frame-0.png"
moneda = cargar_imagen(r"elementos_graficos\moneda.png",(45,45))
bruno = cargar_imagen(r"elementos_graficos\bruno.condarco.png",(240,60))
facu = cargar_imagen(r"elementos_graficos\facpow_.png",(200,60))
reset = cargar_imagen(r"elementos_graficos\reset.png",(250,45))
resume = cargar_imagen(r"elementos_graficos\resume.png",(300,45))
flecha_atras = cargar_imagen(r"elementos_graficos\3.png",(60,60))
rect_flecha_atras = get_rectangulo(flecha_atras,(200,100))

#################SONIDOS################
click_sound = pygame.mixer.Sound(r"sonidos\click.mp3")
error_sound = pygame.mixer.Sound(r"sonidos\ponele-voluntad.mp3")
bien_sound = pygame.mixer.Sound(r"sonidos\coin sound.wav")
loose_sound = pygame.mixer.Sound(r"sonidos\heart drop.wav")
incorrect_sound = pygame.mixer.Sound(r"sonidos\error_sound.wav")
gay_sound = pygame.mixer.Sound(r"sonidos\gay.mp3")
gay_sound.set_volume(0.080)
error_sound.set_volume(0.080)

sonidos_diccionario = {
    "click" : click_sound,
    "error" : error_sound,
    "moneda" :bien_sound,
    "perdiste" :loose_sound,
    "mal" : incorrect_sound,
    "gay" : gay_sound
}
#################MUSICA FONDO################
pygame.mixer.music.load(r"sonidos\musiquita.wav")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)  # Reproduce en bucle
musica = musica_on
sonido = volumen_bajo

with open ("score.csv","r") as archivo:
    for linea in archivo:
        registro = linea.split("\n")
        registro[0] = int(registro[0])
        score_max.append(registro[0])
archivo = open ("score.csv","w")

################CREACION JUEGO################
while bandera_juego == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            bandera_juego = False
            score_max = ordenar_lista(score_max)
            for score in score_max:
                archivo.write(f"{score}\n")
            archivo.close()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            if matriz_banderas[0][0] == True:                                           ################PANTALLA PRINCIPAL################
                if rect_start_menu.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,1)
                elif rect_opcion_menu.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,0)
                elif rect_quit_menu.collidepoint(evento.pos):
                    bandera_juego = False
                    score_max = ordenar_lista(score_max)
                    for score in score_max:
                        archivo.write(f"{score}\n")
                    archivo.close()
            elif matriz_banderas[1][0] == True:                                       ################OPCIONES################
                if rect_flecha_atras.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,0,0)
                elif rect_instagram1.collidepoint(evento.pos):
                    bandera_ig = switch_bool(bandera_ig)
                elif rect_instagram2.collidepoint(evento.pos):
                    bandera_ig_2 = switch_bool(bandera_ig_2)
                elif rect_musica.collidepoint(evento.pos):
                    if musica_bandera == False:                                     ################ALTERNAR MUSICA################
                        musica = musica_off
                        pygame.mixer.music.pause()
                        musica_bandera = True
                    elif musica_bandera == True:
                        musica = musica_on
                        pygame.mixer.music.unpause()
                        musica_bandera = False
                elif rect_sonido.collidepoint(evento.pos):                          ################ALTERNAR SONIDO################
                        bandera_sonido,sonido = sonido_alternar(sonidos_diccionario,bandera_sonido,volumen_bajo,silenciar,volumen_alto)
            elif matriz_banderas[1][1] == True:                         ################START################
                if rect_opcion_a_juego.collidepoint(evento.pos):
                    if rojo_1 != True:
                        juego_activo = 1
                        apreto = True
                elif rect_opcion_b_juego.collidepoint(evento.pos):
                    if rojo_2 != True:
                        juego_activo = 2
                        apreto = True
                elif rect_opcion_c_juego.collidepoint(evento.pos):
                    if rojo_3 != True:
                        juego_activo = 3
                        apreto = True
                elif rect_opcion_d_juego.collidepoint(evento.pos):
                    if rojo_4 != True:
                        juego_activo = 4
                        apreto = True
                elif rect_comodin_half.collidepoint(evento.pos):            ################COMODINES################
                    if bandera_comodin_half == True:
                        gay_sound.play()
                        match opcion_correcta:
                            case 1:
                                rojo_2,rojo_3 = True,True
                            case 2:
                                rojo_4,rojo_1 = True,True
                            case 3:
                                rojo_1,rojo_4 = True,True
                            case 4:
                                rojo_1,rojo_2 = True,True
                        bandera_comodin_half = False
                elif rect_comodin_next.collidepoint(evento.pos):
                    if bandera_comodin_next == True:
                        gay_sound.play()
                        match opcion_correcta:
                            case 1:
                                apreto = True
                                juego_activo = 1
                            case 2:
                                apreto = True
                                juego_activo = 2
                            case 3:
                                apreto = True
                                juego_activo = 3
                            case 4:
                                apreto = True
                                juego_activo = 4
                        bandera_comodin_next = False
                elif rect_comodin_reload.collidepoint(evento.pos):
                    if bandera_comodin_reload == True:
                        gay_sound.play()
                        match opcion_correcta:
                            case 1:
                                rojo_2,rojo_3,rojo_4 = True,True,True
                                apreto = True
                                juego_activo = 1
                            case 2:
                                rojo_1,rojo_3,rojo_4 = True,True,True
                                apreto = True
                                juego_activo = 2
                            case 3:
                                rojo_1,rojo2,rojo_4 = True,True,True
                                apreto = True
                                juego_activo = 3
                            case 4:
                                rojo_1,rojo2,rojo_3 = True,True,True
                                apreto = True
                                juego_activo = 4
                        comodin_reload = True
                        bandera_comodin_reload = False
                elif rect_opcion_pausa.collidepoint(evento.pos):    
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,2)
            elif matriz_banderas[0][2] == True:                                     ###############GAME OVER ############
                if rect_flecha_atras.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,0,0)
            elif matriz_banderas[1][2] == True:                                      ################PAUSA DEL JUEGO################
                if rect_opcion_pausa.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,1)
                elif rect_barra.collidepoint(evento.pos): 
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,1)           
                elif rect_barra_2.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,1,1)
                    vidas = 5
                    coins = 0
                    promedio_tiempo = 0
                    lista_numeros_usados = set()
                    while_juego = True
                    bandera_comodin_reload,bandera_comodin_half,bandera_comodin_next = True,True,True
                elif rect_musica.collidepoint(evento.pos):                             ################ALTERNA MUSICA DESDE EL JUEGO################
                    if musica_bandera == False:
                        musica = musica_off
                        pygame.mixer.music.pause()
                        musica_bandera = True
                    elif musica_bandera == True:
                        musica = musica_on
                        pygame.mixer.music.unpause()
                        musica_bandera = False
                elif rect_sonido.collidepoint(evento.pos):                               ################ALTERNA SONIDO DESDE EL JUEGO################
                    bandera_sonido,sonido = sonido_alternar(sonidos_diccionario,bandera_sonido,volumen_bajo,silenciar,volumen_alto)
            elif matriz_banderas[0][1] == True:                                                     
                if rect_flecha_atras.collidepoint(evento.pos):
                    matriz_banderas = cambiar_banderas(matriz_banderas,0,0)
    
    if matriz_banderas[0][0] == True:                                                              #################BANNER################
        comodin_reload = False
        bandera_1_vez = True
        cargar_imagen_rectangulo_blit(ventana,r"Logo_juego\Banner.png",resolucion_ventana,(0,0))
        vidas = 5
        coins = 0
        apreto = False
        juego_activo = 0
        promedio_tiempo = 0
        tiempo_printeable = 0
        bandera_comodin_half = True
        bandera_comodin_next = True
        bandera_comodin_reload = True
        lista_numeros_usados = set()
        rect_opcion_menu = cargar_imagen_rectangulo_blit(ventana,r"opciones_menu\menu_inicial\options.png",(300,83),(500,500))
        rect_start_menu = cargar_imagen_rectangulo_blit(ventana,r"opciones_menu\menu_inicial\start.png",(300,83),(500,400))
        rect_quit_menu = cargar_imagen_rectangulo_blit(ventana,r"opciones_menu\menu_inicial\quit.png",(300,83),(500,600))
        renderizados_coins = get_superficie(coins_totales,fuente_2,colores["NEGRO"])
        ventana.blit(moneda,(870,585))
        ventana.blit((renderizados_coins),(920,592))
        if contador_gatos >= 1:                                                                   ################EASTER EGG GATOS################
            cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato1.png",(80,80),(120,560))
            if contador_gatos >= 2:
                cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato2.png",(80,80),(795,560))
                cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato3.png",(80,80),(1045,560))
                if contador_gatos >= 4:
                    cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato4.png",(80,80),(40,560))
                    cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato5.png",(80,80),(1130,560))
                    if contador_gatos >= 6:
                        cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\gato7,8.png",(180,80),(305,560))

    elif matriz_banderas[1][0] == True: 
        cargar_imagen_rectangulo_blit(ventana,r"Logo_juego\Texto del párrafo.png",(600,650),(330,30))
        rect_flecha_atras = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\3.png",(60,60),(200,100))
        rect_instagram1 = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\instagram_2.png",(45,45),(400,500))
        rect_instagram2 = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\instagram_2.png",(45,45),(400,560))
        rect_musica = cargar_imagen_rectangulo_blit(ventana,musica,(100,100),(740,210))
        rect_sonido = cargar_imagen_rectangulo_blit(ventana,sonido,(100,100),(420,210))
        if bandera_ig == True:
            ventana.blit(bruno,(450,490))
        if bandera_ig_2 == True:
            ventana.blit(facu,(450,555))

    elif matriz_banderas[1][1] == True:                                    ################CORAZONES################
        lugar_corazones = 90
        cargar_imagen_rectangulo_blit(ventana,r"Logo_juego\VIDAS.png",resolucion_ventana,(0,0))
        while while_juego == True:
            comodin_reload = False
            inicio_de_tiempo = time.time()
            contador_errores = 0    
            promedio_tiempo += tiempo_printeable  
            if len(lista_numeros_usados) != 15:
                juego_activo = 0
                rojo_1,rojo_2,rojo_3,rojo_4 = False,False,False,False
                numero_random = random_numero(lista_numeros_usados,1,15)
                lista_numeros_usados.add(numero_random)
                for marca in marcas_diccionario:
                    if marca["numero"] == numero_random :
                        opcion_1,opcion_2,opcion_3,opcion_4 = marca["imagen1"],marca["imagen2"],marca["imagen3"],marca["imagen4"]
                        opcion_correcta = marca["opcion_correcta"]
                while_juego = False
            else:
                matriz_banderas = cambiar_banderas(matriz_banderas,0,1)
                while_juego = False
        rect_opcion_a_juego = cargar_imagen_rectangulo_blit(ventana,opcion_1,(322,213),(215,80))
        rect_opcion_b_juego = cargar_imagen_rectangulo_blit(ventana,opcion_2,(322,213),(703,80))
        rect_opcion_c_juego = cargar_imagen_rectangulo_blit(ventana,opcion_3,(322,213),(215,320))
        rect_opcion_d_juego = cargar_imagen_rectangulo_blit(ventana,opcion_4,(322,213),(703,320))
        rect_opcion_pausa = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\menu_real.png",(70,70),(50,50))
        if bandera_comodin_half == True:
            rect_comodin_half = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\half_comodin.png",(70,70),(1170,100))
        if bandera_comodin_next == True:
            rect_comodin_next = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\next_comodin.png",(70,70),(1170,200))
        if bandera_comodin_reload == True:
            rect_comodin_reload = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\reload_comodin.png",(70,70),(1170,300))
        if apreto == True:
            if juego_activo == opcion_correcta:
                    if comodin_reload == False :
                        coins += 20
                        bien_sound.play()
                    match juego_activo:
                        case 1:
                            pygame.draw.rect(ventana,colores["VERDE"],(215,80,325,215),13)
                        case 2:
                            pygame.draw.rect(ventana,colores["VERDE"],(703,80,325,215),13)
                        case 3:
                            pygame.draw.rect(ventana,colores["VERDE"],(215,320,325,215),13)
                        case 4:
                            pygame.draw.rect(ventana,colores["VERDE"],(703,320,325,215),13)
                    while_juego = True
            else:
                if juego_activo == 1 :                           
                    rojo_1 = True
                    contador_errores += 1
                    vidas -= 1
                    coins -= 10
                    incorrect_sound.play()
                if juego_activo == 2 :
                    rojo_2 = True
                    contador_errores += 1
                    vidas -= 1
                    coins -= 10
                    incorrect_sound.play()
                if juego_activo == 3 :
                    rojo_3 = True
                    contador_errores += 1
                    vidas -= 1
                    coins -= 10
                    incorrect_sound.play()
                if juego_activo == 4 :
                    rojo_4 = True
                    contador_errores += 1
                    vidas -= 1
                    coins -= 10
                    incorrect_sound.play()
                if vidas == 0:
                    matriz_banderas = cambiar_banderas(matriz_banderas,0,2)
                    loose_sound.play()
                elif contador_errores == 3:
                    error_sound.play()
                    while_juego = True
            apreto = False

        ###################### TIEMPO ################################
        tiempo_printeable = tiempo_cuenta_atras(30,inicio_de_tiempo) 
        tiempo = get_superficie(tiempo_printeable,fuente_2,colores["NEGRO"])
        ventana.blit((tiempo),(1060,645))
        if tiempo_printeable <= 0:
            while_juego = True
            vidas -= 1
            incorrect_sound.play()
            if vidas <= 0:
                matriz_banderas = cambiar_banderas(matriz_banderas,0,2)
        ############ COINS ###########################
        ventana.blit(moneda,(530,640))
        renderizados_coins = get_superficie(coins,fuente_2,colores["NEGRO"])
        ventana.blit((renderizados_coins),(580,645))
        ############# CORAZONES ##############################
        for corazon in range(vidas):             
            ventana.blit(corazones,(lugar_corazones,640))
            lugar_corazones += 50
        ################ RECTANGULO ROJO ################
        if rojo_1 == True:                           
            pygame.draw.rect(ventana,colores["ROJO"],(215,80,325,215),7)
        if rojo_2 == True:
            pygame.draw.rect(ventana,colores["ROJO"],(703,80,325,215),7)
        if rojo_3 == True:
            pygame.draw.rect(ventana,colores["ROJO"],(215,320,325,215),7)
        if rojo_4 == True:
            pygame.draw.rect(ventana,colores["ROJO"],(703,320,325,215),7)
        time.sleep(0.3)

    elif matriz_banderas[0][2] == True:                               ################GAME OVER ################
        juego_activo = 0
        rojo_1,rojo_2,rojo_3,rojo_4 = False,False,False,False
        cargar_imagen_rectangulo_blit(ventana,r"Logo_juego\game_over.png",(600,650),(330,30))
        ventana.blit(moneda,(677,480))
        ventana.blit(moneda,(700,527))
        if coins > record_coins:
            record_coins = coins
            score_max.append(record_coins)
        while bandera_1_vez == True:
            contador_gatos += 1
            coins_totales += coins
            bandera_1_vez = False
        bandera_comodin_reload,bandera_comodin_half,bandera_comodin_next = True,True,True
        #################COINS################
        renderizados_coins = get_superficie(coins,fuente_2,colores["NEGRO"])
        ventana.blit((renderizados_coins),(727,485))
        #################COINS RECORD################
        renderizados_record_coins = get_superficie(record_coins,fuente_2,colores["NEGRO"])
        ventana.blit((renderizados_record_coins),(750,530))
        ################# TIEMPO PROMEDIO #######################
        printeo_tiempo = promedio(promedio_tiempo)
        renderizado_promedio_tiempo = get_superficie(printeo_tiempo,fuente_2,colores["NEGRO"])
        ventana.blit((renderizado_promedio_tiempo),(565,435))
        rect_flecha_atras = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\3.png",(60,60),(200,100))
    
    elif matriz_banderas[1][2] == True:                                       ################PAUSA DENTRO DEL JUEGO################
        cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\pausa.png",(600,650),(330,30))
        rect_musica = cargar_imagen_rectangulo_blit(ventana,musica,(100,100),(740,210))
        rect_sonido = cargar_imagen_rectangulo_blit(ventana,sonido,(100,100),(420,210))
        rect_barra = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\barra.png",(400,70),(435,380))
        rect_barra_2 = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\barra.png",(400,70),(435,480))
        ventana.blit(reset,(510,495))
        ventana.blit(resume,(480,395))
    
    elif matriz_banderas[0][1] == True:                                       ################ #MAX WIN################
        cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\max win.png",(600,650),(330,30))
        ventana.blit(moneda,(677,480))
        ventana.blit(moneda,(700,527))
        if coins > record_coins:
            record_coins = coins
            score_max.append(record_coins)
        while bandera_1_vez == True:
            contador_gatos += 1
            coins_totales += coins
            bandera_1_vez = False
        #################COINS################
        renderizados_coins = get_superficie(coins,fuente_2,colores["NEGRO"])
        ventana.blit((renderizados_coins),(727,485))
        #################COINS RECORD################
        renderizados_record_coins = get_superficie(record_coins,fuente_2,colores["NEGRO"])
        ventana.blit((renderizados_record_coins),(750,530))
        ################# TIEMPO PROMEDIO #######################
        printeo_tiempo = int(promedio_tiempo / len(lista_numeros_usados))
        renderizado_promedio_tiempo = get_superficie(printeo_tiempo,fuente_2,colores["NEGRO"])
        ventana.blit((renderizado_promedio_tiempo),(565,435))
        rect_flecha_atras = cargar_imagen_rectangulo_blit(ventana,r"elementos_graficos\3.png",(60,60),(200,100))

    pygame.display.update()
pygame.quit()