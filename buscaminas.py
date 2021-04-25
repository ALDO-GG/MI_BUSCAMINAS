import pygame
import random
import time
import threading
import numpy

pygame.init()

ventana = pygame.display.set_mode((600,600))
ejecutar = True
cantidad_celdasx = 10
cantidad_celdasy = 9
longitud_celdas = 60
blanco = (255,255,255)
azul = (0,0,250)
rojo = (255,0,0)
verde = (0,255,0)
amarillo = (241,217,7)
rosa = (247, 5,173)
cian = (47, 188,202)
morado = (202, 16,205)
naranja = (247, 129,5)
contador_tiempo = 0
casillas_ocultas = 0
estado_partida = None
hilo_tiempo = None
mapa = []
mapa_x = []

def cronometro():

	global contador_tiempo

	while estado_partida is None:

		time.sleep(1)
		contador_tiempo += 1

def iniciar():

	global contador_tiempo,mapa,casillas_ocultas,estado_partida,mapa,mapa_x
	mapa = []

	contador_tiempo = 0
	casillas_ocultas = 0
	estado_partida = None

	for y in range(cantidad_celdasy):
		ar = []
		for x in range(cantidad_celdasx):
			numero = random.randint(1,5)
			if numero == 5:
				ar.append('*')
			else:
				ar.append('')
				casillas_ocultas += 1

		mapa.append(ar)

	mapa_x = numpy.array(mapa,dtype=object)
	mapa = numpy.array(mapa,dtype=object)
	

	for y in range(len(mapa)):
		for x in range(len(mapa[y])):

			if mapa[y][x] != '*':

				celdas = (mapa[(y+1)%cantidad_celdasy][x%cantidad_celdasx],
						 mapa[(y+1)%cantidad_celdasy][(x+1)%cantidad_celdasx],
						 mapa[(y+1)%cantidad_celdasy][(x-1)%cantidad_celdasx],
						 mapa[y%cantidad_celdasy][(x+1)%cantidad_celdasx],
						 mapa[y%cantidad_celdasy][(x-1)%cantidad_celdasx],
						 mapa[(y-1)%cantidad_celdasy][x%cantidad_celdasx],
						 mapa[(y-1)%cantidad_celdasy][(x+1)%cantidad_celdasx],
						 mapa[(y-1)%cantidad_celdasy][(x-1)%cantidad_celdasx])

				celda = celdas.count('*')
				mapa[y][x] = str(celda)

	hilo_tiempo = threading.Thread(target=cronometro)
	hilo_tiempo.start()

def celdas_cercanas(x,y):

	global mapa,casillas_ocultas

	if type(mapa[y%cantidad_celdasy][(x+1)%cantidad_celdasx]) == type(''):		
			casillas_ocultas -= 1

	if type(mapa[(y+1)%cantidad_celdasy][(x-1)%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[(y+1)%cantidad_celdasy][(x+1)%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[(y+1)%cantidad_celdasy][x%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[y%cantidad_celdasy][(x-1)%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[(y-1)%cantidad_celdasy][(x+1)%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[(y-1)%cantidad_celdasy][(x-1)%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	if type(mapa[(y-1)%cantidad_celdasy][x%cantidad_celdasx]) == type(''):
		casillas_ocultas -= 1

	mapa[y%cantidad_celdasy][(x+1)%cantidad_celdasx] = int(mapa[y%cantidad_celdasy][(x+1)%cantidad_celdasx])
	mapa[y%cantidad_celdasy][(x-1)%cantidad_celdasx] = int(mapa[y%cantidad_celdasy][(x-1)%cantidad_celdasx])
	mapa[(y+1)%cantidad_celdasy][(x+1)%cantidad_celdasx] = int(mapa[(y+1)%cantidad_celdasy][(x+1)%cantidad_celdasx])
	mapa[(y+1)%cantidad_celdasy][(x-1)%cantidad_celdasx] = int(mapa[(y+1)%cantidad_celdasy][(x-1)%cantidad_celdasx])
	mapa[(y+1)%cantidad_celdasy][x%cantidad_celdasx] = int(mapa[(y+1)%cantidad_celdasy][x%cantidad_celdasx])
	mapa[(y-1)%cantidad_celdasy][(x-1)%cantidad_celdasx] = int(mapa[(y-1)%cantidad_celdasy][(x-1)%cantidad_celdasx])
	mapa[(y-1)%cantidad_celdasy][(x+1)%cantidad_celdasx] = int(mapa[(y-1)%cantidad_celdasy][(x+1)%cantidad_celdasx])
	mapa[(y-1)%cantidad_celdasy][x%cantidad_celdasx] = int(mapa[(y-1)%cantidad_celdasy][x%cantidad_celdasx])	
	
def celda_cero(x,y):

	global mapa,casillas_ocultas

	if mapa[y][x] == '0':

		mapa[y][x] = 0
		casillas_ocultas -= 1

		if mapa[y%cantidad_celdasy][(x+1)%cantidad_celdasx] == '0':				
			celda_cero((x+1)%cantidad_celdasx,y%cantidad_celdasy)			

		if mapa[(y+1)%cantidad_celdasy][(x-1)%cantidad_celdasx] == '0':			
			celda_cero((x-1)%cantidad_celdasx,(y+1)%cantidad_celdasy)			

		if mapa[(y+1)%cantidad_celdasy][(x+1)%cantidad_celdasx] == '0':			
			celda_cero((x+1)%cantidad_celdasx,(y+1)%cantidad_celdasy)			

		if mapa[(y+1)%cantidad_celdasy][x%cantidad_celdasx] == '0':			
			celda_cero(x%cantidad_celdasx,(y+1)%cantidad_celdasy)
			
		if mapa[y%cantidad_celdasy][(x-1)%cantidad_celdasx] == '0':			
			celda_cero((x-1)%cantidad_celdasx,y%cantidad_celdasy)
			
		if mapa[(y-1)%cantidad_celdasy][(x+1)%cantidad_celdasx] == '0':			
			celda_cero((x+1)%cantidad_celdasx,(y-1)%cantidad_celdasy)			

		if mapa[(y-1)%cantidad_celdasy][(x-1)%cantidad_celdasx] == '0':			
			celda_cero((x-1)%cantidad_celdasx,(y-1)%cantidad_celdasy)			

		if mapa[(y-1)%cantidad_celdasy][x%cantidad_celdasx] == '0':
			celda_cero(x%cantidad_celdasx,(y-1)%cantidad_celdasy)
			
		celdas_cercanas(x,y)	

def seleccionar():

	global casillas_ocultas,estado_partida

	raton = pygame.mouse.get_pressed()
	if raton[0]:

		posicion_raton = pygame.mouse.get_pos()
		x = posicion_raton[0] // longitud_celdas
		y = (posicion_raton[1] - 60) // longitud_celdas
		celda = mapa[y][x]

		if celda == '*' or celda == '#':

			mapa[y][x] = '#'
			if estado_partida is None:
				estado_partida = False

		elif celda == '0':

			celda_cero(x,y)

		else:
			if type(mapa[y][x]) == type(''):
				casillas_ocultas -= 1
			mapa[y][x] = int(mapa[y][x])
	if raton[2]:

		posicion_raton = pygame.mouse.get_pos()
		x = posicion_raton[0] // longitud_celdas
		y = (posicion_raton[1] - 60) // longitud_celdas
		celda = mapa[y][x]

		if type(celda) == type('') and celda != '#':

			if mapa_x[y][x] == '?':

				mapa_x[y][x] = ''

			else: 

				mapa_x[y][x] = '?'
		time.sleep(.1)


		
def dibujar():


	for y in range(len(mapa)):
		for x in range(len(mapa[y])):
			if type(mapa[y][x]) == type(''):

				if mapa[y][x] == '#':

					fuente = pygame.font.Font(None,50)
					texto = fuente.render('X',1,(255,255,255))
					ventana.blit(texto,(x*longitud_celdas+20,y*longitud_celdas + 70))
					pygame.draw.rect(ventana,rojo,[x*longitud_celdas,(y*longitud_celdas)+60,longitud_celdas,longitud_celdas],1)

				else:

					if mapa_x[y][x] == '?':

						fuente = pygame.font.Font(None,50)
						texto = fuente.render('?',1,(255,255,255))
						ventana.blit(texto,(x*longitud_celdas+20,y*longitud_celdas + 70))
					pygame.draw.rect(ventana,amarillo,[x*longitud_celdas,(y*longitud_celdas)+60,longitud_celdas,longitud_celdas],1)

			else:

				color1 = ()

				if mapa[y][x] == 0:
					color1 = blanco

				if mapa[y][x] == 1:
					color1 = cian

				if mapa[y][x] == 2:
					color1 = morado

				if mapa[y][x] == 3:
					color1 = azul

				if mapa[y][x] == 4:
					color1 = rosa

				if mapa[y][x] == 5:
					color1 = verde

				if mapa[y][x] == 6:
					color1 = amarillo

				if mapa[y][x] == 7:
					color1 = naranja

				if mapa[y][x] == 8:
					color1 = rojo

				fuente = pygame.font.Font(None,50)
				texto = fuente.render(str(mapa[y][x]),1,color1)
				ventana.blit(texto,(x*longitud_celdas+20,y*longitud_celdas + 70))
				pygame.draw.rect(ventana,color1,[x*longitud_celdas,(y*longitud_celdas)+60,longitud_celdas,longitud_celdas],1)

	fuente = pygame.font.Font(None,60)
	texto = fuente.render(str(contador_tiempo),2,azul)
	ventana.blit(texto,(510,15))

iniciar()

tiempo = pygame.time.Clock()

while ejecutar:

	tiempo.tick(30)

	ventana.fill((0,0,0))

	fuente = pygame.font.Font(None,60)
	texto = fuente.render('BUSCAMINAS',2,verde)
	ventana.blit(texto,(220,15))
	
	dibujar()
	try:
		seleccionar()
	except Exception as e:
		pass

	fuente = pygame.font.Font(None,60)
	if estado_partida is not None:

		if estado_partida:
			texto = fuente.render('GANASTE',2,azul)
			ventana.blit(texto,(10,15))
		else:
			texto = fuente.render('PERDISTE',3,rojo)
			ventana.blit(texto,(10,15))
		
		pygame.draw.rect(ventana,(127, 140, 141),[100,230,385,120])

		fuente = pygame.font.Font(None,35)
		texto = fuente.render('PRECIONA "R" PARA REINICIAR',1,(46, 64, 83))
		ventana.blit(texto,(100,280))

	if not casillas_ocultas and estado_partida is None:
		estado_partida = True

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			ejecutar = False
			estado_partida = not None
			time.sleep(1)
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_ESCAPE:
				ejecutar = False
				estado_partida = not None
				time.sleep(1)

			if i.key == pygame.K_r:

				estado_partida = not None
				time.sleep(1)
				iniciar()

	pygame.display.update()



