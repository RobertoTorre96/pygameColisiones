import pygame,sys,time
from pygame import *

pygame.init()

blanco=(255,255,255)
negro=(0,0,0)
verde=(0,255,0)
rojo=(255,0,0)

ventana=pygame.display.set_mode((400,400))

rectangulo1=pygame.Rect(0,0,15,400)
rectangulo2=pygame.Rect(35,0,365,100)
rectangulo3=pygame.Rect(70,100,330,100)
rectangulo4=pygame.Rect(150,200,250,100)

#meta
meta=pygame.Rect(15,0,20,10)

#enemigo
posX=15
enemigo=pygame.Rect(posX,140,20,20)
derecha=True
velocidad=0.020

#enemigo2
posy2=300
enemigo2=pygame.Rect(150,posy2,20,20)
subir=False


#jugador
jugador=pygame.Rect(380,20,10,10)
jugador2=pygame.Rect(380,380,10,10)

#fuente
fuente=pygame.font.SysFont("Arial",30)

perder=False


zona=pygame.Rect(375,375,20,20)
empezar=False
pepe=pygame.Rect(10,10,10,10)
codeX=0
codeY=0
zona2=False
while True:
    if empezar==False:
        perder=False
        ventana.fill(negro)

        guia=fuente.render("para comenzar colocate en la zona verde",0, blanco,negro )
        ventana.blit(guia,(0,20))
        pygame.draw.rect(ventana,verde,zona)

        pygame.draw.rect(ventana,rojo,jugador)
        jugador.left,jugador.top=pygame.mouse.get_pos()
        jugador.left-=5
        jugador.top-=5

        if jugador.colliderect(zona):
            empezar=True


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    if empezar==True:

        ventana.fill((blanco))

        # meta y paredes

        pygame.draw.rect(ventana,verde,meta)
        pygame.draw.rect(ventana,negro,rectangulo1)
        pygame.draw.rect(ventana,negro,rectangulo2)
        pygame.draw.rect(ventana,negro,rectangulo3)
        pygame.draw.rect(ventana,negro,rectangulo4)

    #enemigo
        pygame.draw.rect(ventana,negro,enemigo)
        if derecha==True:
            if posX<50:
                enemigo.left=posX
                posX+=velocidad
            else:
                derecha=False
        else:
            if posX>15:
                enemigo.left=posX
                posX-=velocidad
            else:derecha=True

    #enemigo2
        pygame.draw.rect(ventana,negro,enemigo2)
        if subir==True:
            if posy2<=400:
                enemigo2.top=posy2
                posy2+=velocidad+0.1

            else:
                subir=False
        else:
            if posy2>=300:
                enemigo2.top=posy2
                posy2-=velocidad +0.1
            else:subir=True

    #jugador
        pygame.draw.rect(ventana,rojo,jugador)
        jugador.left,jugador.top=pygame.mouse.get_pos()
        jugador.left-=5
        jugador.top-=5

    #perder
        if jugador.colliderect(rectangulo1):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))
            perder=True
            empezar=False

        if jugador.colliderect(rectangulo2):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))
            perder=True
            empezar=False


        if jugador.colliderect(rectangulo3):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))
            perder=True
            empezar=False

        if jugador.colliderect(rectangulo4):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))
            empezar=False





        #perder con enemigo
        if jugador.colliderect(enemigo):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))

            perder=True
            empezar=False

        if jugador.colliderect(enemigo2):
            ventana.fill((negro))
            perdiste=fuente.render("perdiste",0,rojo,blanco)
            ventana.blit(perdiste,(150,170))

            perder=True
            empezar=False


    #ganar
        if jugador.colliderect(meta):
            ventana.fill((negro))
            ganaste=fuente.render("ganaste",0,rojo,blanco)
            ventana.blit(ganaste,(150,170))




    #    print (empezar)


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.display.update()