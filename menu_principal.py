# -*- coding: utf-8 -*-

import zlib, pygame
from random import randint
from sys import exit
from pygame.locals import*
pygame.init()

#Contador referente a compactação das imagens, realiza um laço de repetição, adicionando + 1 ao contador, sendo assim selecionando todas as 25 cartas do jogo para serem descomprimidas.
contador = 1
while contador < 26:
    readFile = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
    decompressed = zlib.decompress(readFile)
    readFile = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
    readFile.write(decompressed)
    readFile.close()
    contador = contador + 1



#Importa todas as funções necessárias para o funcionamento do menu do jogo.
import pygame, os
from pygame import KEYDOWN, KEYUP, QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_RETURN, K_ESCAPE, K_a, K_s, K_d, K_n
from pygame.locals import*
from sys import exit
from random import randint
clock = pygame.time.Clock()


#Inicia o Pygame, as configurações do Pygame como tela, imagens de fundo e a musica adicionada ao menu do jogo.
pygame.init()
fixo = True
tela = pygame.display.set_mode ((1920,1080), 0, 32)
fundo = 'Fundo/Fundo.png'
fundo_selecionado = pygame.image.load(fundo)
pygame.display.set_caption ('PyRamses Card Game')
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play()
pygame.mixer.music.rewind()

#Máquina de estado do jogo, proporcionando um menu de opções.
def fixo ():
    fonte = pygame.font.SysFont ("Metrolox", 40, False, False)
    fixo = fonte.render("> ", True, (0,0,0))
    fundo_selecionado.blit(fixo,((400)+200, (300)+35))


def selecao ():
    global menu_selecao
    if (menu_selecao ==1):
        
        fonte = pygame.font.SysFont("Metrolox", 40, False, False)
        iniciar = fonte.render(" Iniciar", True, (0,0,0))
        tela.blit(iniciar, ((400)+215, (300)+35))
        pygame.display.flip()
        pygame.display.update()
        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        regras = fonte.render(" Regras", True, (80, 80, 80))
        tela.blit(regras, ((400) + 215, (300) + 75))
        pygame.display.flip()

        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        creditos = fonte.render(" Creditos", True, (80, 80, 80))
        tela.blit(creditos, ((400) + 215, (300) + 105))
        pygame.display.flip()
   
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        sair = fonte.render(" Sair", True, (80, 80, 80))
        tela.blit(sair, ((400) + 215, (300)+135))
        pygame.display.flip()


    if (menu_selecao ==2):
        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        iniciar = fonte.render (" Iniciar", True, (80,80,80))
        tela.blit(iniciar, ((400)+215, (300)+5))
        pygame.display.flip()
        pygame.display.update()
        
        fonte = pygame.font.SysFont("Metrolox", 40, False, False)
        regras = fonte.render(" Regras", True, (0, 0, 0))
        tela.blit(regras, ((400) + 215, (300) + 35))
        pygame.display.flip()
        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        creditos = fonte.render(" Creditos", True, (80, 80, 80))
        tela.blit(creditos, ((400) + 215, (300) + 75))
        pygame.display.flip()
                
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        sair = fonte.render(" Sair", True, (80, 80, 80))
        tela.blit(sair, ((400) + 215, (300)+105))
        pygame.display.flip()



    if (menu_selecao ==3):
        
        tela.blit(fundo_selecionado,(0,0))

        #tela_menu.fill((255,255,255))
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        iniciar = fonte.render (" Iniciar", True, (80,80,80))
        tela.blit(iniciar, ((400)+215, (300)-25))
        pygame.display.flip()
        pygame.display.update()

        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        regras = fonte.render(" Regras", True, (80, 80, 80))
        tela.blit(regras, ((400) + 215, (300) + 5))
        pygame.display.flip()

        
        fonte = pygame.font.SysFont("Metrolox", 40, False, False)
        creditos = fonte.render(" Creditos", True, (0, 0, 0))
        tela.blit(creditos, ((400) + 215, (300) + 35))
        pygame.display.flip()

        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        sair = fonte.render(" Sair", True, (80, 80, 80))
        tela.blit(sair, ((400) + 215, (300)+75))
        pygame.display.flip()


    if (menu_selecao ==4):
        
        tela.blit(fundo_selecionado,(0,0))

        
        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        iniciar = fonte.render (" Iniciar", True, (80,80,80))
        tela.blit(iniciar, ((400)+215, (300)-55))
        pygame.display.flip()
        pygame.display.update()

        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        regras = fonte.render(" Regras", True, (80, 80, 80))
        tela.blit(regras, ((400) + 215, (300)-25))
        pygame.display.flip()

        
        fonte = pygame.font.SysFont("Metrolox", 30, False, False)
        creditos = fonte.render(" Creditos", True, (80, 80, 80))
        tela.blit(creditos, ((400) + 215, (300) +5))
        pygame.display.flip()

        
        fonte = pygame.font.SysFont("Metrolox", 40, False, False)
        sair = fonte.render(" Sair", True, (0, 0, 0))
        tela.blit(sair, ((400 + 215), (300)+35))
        pygame.display.flip()


    if menu_selecao == 5:
       menu_selecao = 4
    if menu_selecao <= 0:
       menu_selecao = 1
    if menu_selecao == 6:
       menu_selecao = 1
    if menu_selecao == 11:
    




        #Inicia o PyGame, configuração de resolução da tela e carregamento do background em modo random.
        pygame.init()
                
        display = pygame.display.Info()
        screen = pygame.display.set_mode((display.current_w, display.current_h))
        
        PyRamses_Background_number = randint(1, 5)
        PyRamses_Background = 'PyRamses_Background' + str(PyRamses_Background_number) + '.png'
        PyRamses_Background_Selecionado = pygame.image.load(PyRamses_Background)
        
        
        

        #Inicializa a fonte que será usada no jogo
        font = pygame.font.SysFont('Metrolox', 30, True, True)


        #Carrega as imagens vencer e perder, avatares, imagens serão apresentadas no final de cada partida, sendo o jogador o vencedor ou o perdedor.
        vencer = 'Jogador_Vencedor.png'
        perder = 'Jogador_Perdedor.png'
        avatar_jog = 'Avatar/jogador.png'
        avatar_ini = 'Avatar/inimigo.png'  
        Jogador_Vencedor = pygame.image.load(vencer)
        Jogador_Perdedor = pygame.image.load(perder)
        avatar_jogador = pygame.image.load(avatar_jog)
        avatar_inimigo = pygame.image.load(avatar_ini)               

        #Insere o titulo do jogo na janela do pygame
        pygame.display.set_caption ('PyRamses Card Game')
        
        

        #Trecho de código responsável por definir a quantidade de energia do jogador e do oponente.
        Energia_Jogador = 20000
        Energia_Jogador_Inimigo = 20000
                   
        #Imagem carregada enquanto uma carta não for escolhida pelo algoritmo, o jogador não vê essa carta, apenas define o valor booleano verdadeiro ou falso.
        Carta_Nao_Escolhida = 'Carta_Nao_Escolhida.png'
        Carta_Selecionada = False
        Jogador_Inimigo = False
        dano_jogador = 0
        dano_inimigo = 0
        #contador = 0

        #Código responsável pelo carregamento das cartas do jogador, as cartas são de 1 a 25 em modo random e essas cartas são as cartas de batalha, sendo que 5 cartas são apresentadas ao jogador.            
                        
        carta_1 = randint(1, 25)
        sprite_carta_1 = 'Deck/PyRamses_Carta' + str(carta_1) + '.png'
        carta1 = pygame.image.load(sprite_carta_1)
            

        carta_2 = randint(1, 25)
        sprite_carta_2 = 'Deck/PyRamses_Carta' + str(carta_2) + '.png'
        carta2 = pygame.image.load(sprite_carta_2)

        carta_3 = randint(1, 25)
        sprite_carta_3 = 'Deck/PyRamses_Carta' + str(carta_3) + '.png'
        carta3 = pygame.image.load(sprite_carta_3)

        carta_4 = randint(1, 25)
        sprite_carta_4 = 'Deck/PyRamses_Carta' + str(carta_4) + '.png'
        carta4 = pygame.image.load(sprite_carta_4)

        carta_5 = randint(1, 25)
        sprite_carta_5 = 'Deck/PyRamses_Carta' + str(carta_5) + '.png'
        carta5 = pygame.image.load(sprite_carta_5)
        
                                            
        #Posição das cartas do jogador na tela:
        #Carta1
        x1 = 310
        y1 = 580

        #Carta2
        x2 = 630
        y2 = 580

        #Carta3
        x3 = 940
        y3 = 580

        #Carta4
        x4 = 1250
        y4 = 580

        #Carta5
        x5 = 1560
        y5 = 580
                
        
       #Modifica a posição das cartas, conforma tipo de seleção da carta, TRUE or FALSE.
        possition = 500
        possition_original = 580
                
        musica = randint(1, 3)
        musica_selecionada = 'musica' + str(musica) + '.mp3'
        pygame.mixer.music.load(musica_selecionada)
        pygame.mixer.music.play(-1)
        
        
        #Laço principal, função QUIT para sair do jogo, define quais teclas serão usadas no jogo
        contador = 1
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    
                    while contador < 26:
                        imagem = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
                        compressed = zlib.compress(imagem,9)
                        imagemsave = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
                        imagemsave.write(compressed)
                        imagemsave.close()
                        contador = contador + 1
                        
                   
                    exit()
                    
            
            
            Carta_Batalha = pygame.image.load(Carta_Nao_Escolhida)
            tecla = pygame.key.get_pressed()
            
            #Contador utilizado na função de compressão das cartas ao fechar o jogo.
            
            contador = 1  

            #Teclas a serem utilizadas no jogo, essas teclas são responsáveis pela seleção das cartas.
            if tecla[K_1]: 
                if Carta_Selecionada == False:                                  
                    Carta_Nao_Escolhida = sprite_carta_1                    
                    carta1 = pygame.image.load(sprite_carta_1)
                    Carta_Selecionada = True
                    y1 = possition
                    
                    
                
            if tecla[K_2]: 
                if Carta_Selecionada == False:                                  
                    Carta_Nao_Escolhida = sprite_carta_2
                    carta2 = pygame.image.load(sprite_carta_2)
                    Carta_Selecionada = True
                    y2 = possition
                   
                    
                    
            if tecla[K_3]: 
                if Carta_Selecionada == False:                                  
                    Carta_Nao_Escolhida = sprite_carta_3
                    carta3 = pygame.image.load(sprite_carta_3)
                    Carta_Selecionada = True
                    y3 = possition
                    
                   
                   
            if tecla[K_4]: 
                if Carta_Selecionada == False:                                  
                    Carta_Nao_Escolhida = sprite_carta_4
                    carta4 = pygame.image.load(sprite_carta_4)
                    Carta_Selecionada = True
                    y4 = possition
                    
            if tecla[K_5]: 
                if Carta_Selecionada == False:                                  
                    Carta_Nao_Escolhida = sprite_carta_5
                    carta5 = pygame.image.load(sprite_carta_5)
                    Carta_Selecionada = True
                    y5 = possition
                    
            
                 
            
            #Tecla T, responsável por atribuir o valor FALSE as cartas em batalha. Ação necessária para realização de troca de cartas durante o jogo.
            if tecla[K_t]:
                if Carta_Selecionada == True:
                    Carta_Selecionada = False
                    y1 = possition_original 
                    y2 = possition_original 
                    y3 = possition_original 
                    y4 = possition_original 
                    y5 = possition_original 
                    
            if tecla[K_ESCAPE]:
                    
                    #Código responsável pela compactação das imagens das cartas ao encerrar o jogo através da tecla ESCAPE.
                    while contador < 26:
                        imagem = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
                        compressed = zlib.compress(imagem,9)
                        imagemsave = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
                        imagemsave.write(compressed)
                        imagemsave.close()
                        contador = contador + 1

                    exit()
                
        
                        
            #Código responsável por atribuir uma carta para o jogador inimigo.
            if Jogador_Inimigo == False:
                escolha_aleatoria = randint(1, 25)
                sprite_Inimigo = 'Deck/PyRamses_Carta' + str(escolha_aleatoria) + '.png'
                Carta_Inimigo = pygame.image.load(sprite_Inimigo)   
                Jogador_Inimigo = True

            #Comparação de força entre as cartas do jogo, permitindo definir a quantidade de energia que o jogador vai levar de dano ou o oponente iŕa receber de dano.
            if tecla[K_SPACE] and Jogador_Inimigo == True and Carta_Selecionada == True:
                if Carta_Nao_Escolhida=='Deck/PyRamses_Carta1.png':
                    Forca=570
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta2.png':
                    Forca=540
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta3.png':
                    Forca=630
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta4.png':
                    Forca=810
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta5.png':
                    Forca=300
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta6.png':
                    Forca=540
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta7.png':
                    Forca=870
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta8.png':
                    Forca=300
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta9.png':
                    Forca=330
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta10.png':
                    Forca=220
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta11.png':
                    Forca=890
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta12.png':
                    Forca=760
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta13.png':
                    Forca=110
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta14.png':
                    Forca=340
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta15.png':
                    Forca=560
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta16.png':
                    Forca=730
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta17.png':
                    Forca=570
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta18.png':
                    Forca=630
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta19.png':
                    Forca=120
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta20.png':
                    Forca=760
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta21.png':
                    Forca=280
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta22.png':
                    Forca=120
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta23.png':
                    Forca=780            
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta24.png':
                    Forca=850
                elif Carta_Nao_Escolhida=='Deck/PyRamses_Carta25.png':
                    Forca=450
                
                
                if sprite_Inimigo=='Deck/PyRamses_Carta1.png':
                    Inimigo_Forca=570
                elif sprite_Inimigo=='Deck/PyRamses_Carta2.png':
                    Inimigo_Forca=540
                elif sprite_Inimigo=='Deck/PyRamses_Carta3.png':
                    Inimigo_Forca=630
                elif sprite_Inimigo=='Deck/PyRamses_Carta4.png':
                    Inimigo_Forca=810
                elif sprite_Inimigo=='Deck/PyRamses_Carta5.png':
                    Inimigo_Forca=300
                elif sprite_Inimigo=='Deck/PyRamses_Carta6.png':
                    Inimigo_Forca=540
                elif sprite_Inimigo=='Deck/PyRamses_Carta7.png':
                    Inimigo_Forca=870
                elif sprite_Inimigo=='Deck/PyRamses_Carta8.png':
                    Inimigo_Forca=300
                elif sprite_Inimigo=='Deck/PyRamses_Carta9.png':
                    Inimigo_Forca=330
                elif sprite_Inimigo=='Deck/PyRamses_Carta10.png':
                    Inimigo_Forca=220
                elif sprite_Inimigo=='Deck/PyRamses_Carta11.png':
                    Inimigo_Forca=890
                elif sprite_Inimigo=='Deck/PyRamses_Carta12.png':
                    Inimigo_Forca=760
                elif sprite_Inimigo=='Deck/PyRamses_Carta13.png':
                    Inimigo_Forca=110
                elif sprite_Inimigo=='Deck/PyRamses_Carta14.png':
                    Inimigo_Forca=340
                elif sprite_Inimigo=='Deck/PyRamses_Carta15.png':
                    Inimigo_Forca=560
                elif sprite_Inimigo=='Deck/PyRamses_Carta16.png':
                    Inimigo_Forca=730
                elif sprite_Inimigo=='Deck/PyRamses_Carta17.png':
                    Inimigo_Forca=570
                elif sprite_Inimigo=='Deck/PyRamses_Carta18.png':
                    Inimigo_Forca=630
                elif sprite_Inimigo=='Deck/PyRamses_Carta19.png':
                    Inimigo_Forca=120
                elif sprite_Inimigo=='Deck/PyRamses_Carta20.png':
                    Inimigo_Forca=760
                elif sprite_Inimigo=='Deck/PyRamses_Carta21.png':
                    Inimigo_Forca=280
                elif sprite_Inimigo=='Deck/PyRamses_Carta22.png':
                    Inimigo_Forca=120
                elif sprite_Inimigo=='Deck/PyRamses_Carta23.png':
                    Inimigo_Forca=780
                elif sprite_Inimigo=='Deck/PyRamses_Carta24.png':
                    Inimigo_Forca=850
                elif sprite_Inimigo=='Deck/PyRamses_Carta25.png':
                    Inimigo_Forca=450
                    
                
                #Comparações de forma após a utilização da carta escolhida, sendo responsável por atribuir um novo valor a váriavel energia, tanto do jogador quanto do inimigo. 
                if Forca > Inimigo_Forca:
                    dano_inimigo = Forca - Inimigo_Forca
                    Energia_Jogador_Inimigo -= dano_inimigo
                    pygame.time.wait(200)
                    Jogador_Inimigo = False
                                                  
                    
                if  Forca < Inimigo_Forca and y1 == possition:  
                    carta_1 = randint(1, 25)
                    sprite_carta_1 = 'Deck/PyRamses_Carta' + str(carta_1) + '.png'
                    carta1 = pygame.image.load(sprite_carta_1)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y1 = possition_original
                                
                    
                if  Forca < Inimigo_Forca and y2 == possition:
                    carta_2 = randint(1, 25)
                    sprite_carta_2 = 'Deck/PyRamses_Carta' + str(carta_2) + '.png'
                    carta2 = pygame.image.load(sprite_carta_2)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y2 = possition_original
                
                
                
                if  Forca < Inimigo_Forca and y3 == possition:
                    carta_3 = randint(1, 25)
                    sprite_carta_3 = 'Deck/PyRamses_Carta' + str(carta_3) + '.png'
                    carta3 = pygame.image.load(sprite_carta_3)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y3 = possition_original
                
                
                
                if  Forca < Inimigo_Forca and y4 == possition:
                    carta_4 = randint(1, 25)
                    sprite_carta_4 = 'Deck/PyRamses_Carta' + str(carta_4) + '.png'
                    carta4 = pygame.image.load(sprite_carta_4)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y4 = possition_original
                
                
                
                if  Forca < Inimigo_Forca and y5 == possition:
                    carta_5 = randint(1, 25)
                    sprite_carta_5 = 'Deck/PyRamses_Carta' + str(carta_5) + '.png'
                    carta5 = pygame.image.load(sprite_carta_5)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y5 = possition_original                
                                    
                
                if Forca < Inimigo_Forca:
                    dano_jogador = Inimigo_Forca - Forca
                    Energia_Jogador -= dano_jogador
                    
                              
                               
                if  Forca == Inimigo_Forca and y1 == possition:
                    carta_1 = randint(1, 25)
                    sprite_carta_1 = 'Deck/PyRamses_Carta' + str(carta_1) + '.png'
                    carta1 = pygame.image.load(sprite_carta_1)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y1 = possition_original
                                        
                    Jogador_Inimigo = False
                    
                if  Forca == Inimigo_Forca and y2 == possition:
                    carta_2 = randint(1, 25)
                    sprite_carta_2 = 'Deck/PyRamses_Carta' + str(carta_2) + '.png'
                    carta2 = pygame.image.load(sprite_carta_2)
                    
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y2 = possition_original
                    
                    Jogador_Inimigo = False
                
                if  Forca == Inimigo_Forca and y3 == possition:
                    carta_3 = randint(1, 25)
                    sprite_carta_3 = 'Deck/PyRamses_Carta' + str(carta_3) + '.png'
                    carta3 = pygame.image.load(sprite_carta_3)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y3 = possition_original
                                         
                    Jogador_Inimigo = False
                    
                if  Forca == Inimigo_Forca and y4 == possition:
                    carta_4 = randint(1, 25)
                    sprite_carta_4 = 'Deck/PyRamses_Carta' + str(carta_4) + '.png'
                    carta4 = pygame.image.load(sprite_carta_4)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y4 = possition_original
                                       
                    Jogador_Inimigo = False
                    
                if  Forca  == Inimigo_Forca and y5 == possition:
                    carta_5 = randint(1, 25)
                    sprite_carta_5 = 'Deck/PyRamses_Carta' + str(carta_5) + '.png'
                    carta5 = pygame.image.load(sprite_carta_5)
                    if Carta_Selecionada == True:
                        Carta_Selecionada = False
                        y5 = possition_original
                                        
                    Jogador_Inimigo = False
                                  
                    #Se jogador levar dano ou se a carta do jogador possuir força igual a do inimigo, então as cartas voltam para suas posições originais em FALSE.
                    if Carta_Selecionada == False:
                        y1 = possition_original 
                        y2 = possition_original 
                        y3 = possition_original 
                        y4 = possition_original 
                        y5 = possition_original 
                  
            #Verifica quanto de dano ocorreu durante um ataque e se energia do jogador ou oponente chegar a 0, o jogo acaba informando se o jogador venceu ou perdeu.
                if Forca == Inimigo_Forca:
                        dano_jogador = 0
                   
                    
            contador = 1                
            if Energia_Jogador <= 0 and Energia_Jogador_Inimigo > 0:
                screen.blit(Jogador_Perdedor, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                
                while contador < 26:
                    imagem = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
                    compressed = zlib.compress(imagem,9)
                    imagemsave = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
                    imagemsave.write(compressed)
                    imagemsave.close()
                    contador = contador + 1
                exit()
            
            if Energia_Jogador_Inimigo <= 0 and Energia_Jogador > 0:
                screen.blit(Jogador_Vencedor, (0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                
                while contador < 26:
                    imagem = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
                    compressed = zlib.compress(imagem,9)
                    imagemsave = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
                    imagemsave.write(compressed)
                    imagemsave.close()
                    contador = contador + 1
                exit()     
                
            vida1 = font.render(str(Energia_Jogador), 1, (0, 0, 0))
            vida2 = font.render(str(Energia_Jogador_Inimigo), 1, (0, 0, 0))

            screen.blit(PyRamses_Background_Selecionado, (0, 0))
            screen.blit(carta1, (x1, y1))
            screen.blit(carta2, (x2, y2))
            screen.blit(carta3, (x3, y3))
            screen.blit(carta4, (x4, y4))
            screen.blit(carta5, (x5, y5))
            screen.blit(Carta_Inimigo, (320, 40))
            screen.blit(vida2, (110, 270))
            screen.blit(vida1, (110, 820))
            screen.blit(avatar_jogador, (10, 590))
            screen.blit(avatar_inimigo, (10, 40))
            pygame.display.update()
            
    #Nesse If mostra as regras do jogos
    
     #Imagem com as regras do jogo
    if menu_selecao == 12:
    
        #pygame.init()
        pygame.display.set_caption ('PyRamses Card Game')

                
        
        screen = pygame.display.set_mode((1920, 1080))
        

        instrucoes = 'instrucoes.png'
        instrucoes_selecionado = pygame.image.load(instrucoes)

        screen.blit(instrucoes_selecionado,(0,0))
        pygame.display.update()
        #time_passed = clock.tick(10)


#If contendo imagem com os créditos
    if menu_selecao == 13:
    
        #pygame.init()
        pygame.display.set_caption ('PyRamses Card Game')
                
        
        screen = pygame.display.set_mode((1920, 1080))
        

        creditos = 'creditos.png'
        creditos_selecionado = pygame.image.load(creditos)

        screen.blit(creditos_selecionado,(0,0))
        pygame.display.update()
        #time_passed = clock.tick(10)

    contador = 1
    if menu_selecao == 14:
        while contador < 26:
                imagem = open('Deck/PyRamses_Carta'+str(contador)+'.png','r').read()
                compressed = zlib.compress(imagem,9)
                imagemsave = open('Deck/PyRamses_Carta'+str(contador)+'.png','w')
                imagemsave.write(compressed)
                imagemsave.close()
                contador = contador + 1

                    #exit()
                
        exit()

menu_selecao = 1


while (True): #movimenta selecao

    selecao()

    fixo()
    tela.blit(fundo_selecionado,(0,0))
      
    
    for e in pygame.event.get():
        if (e.type == QUIT):
            exit()
        if (e.type == KEYDOWN):
            if (e.key == K_DOWN):
                menu_selecao = menu_selecao+1
                #pygame.display.update()
            if (e.key == K_UP):
                menu_selecao = menu_selecao-1
                #pygame.display.update()
            if (e.key == K_RETURN):
                menu_selecao = menu_selecao+10
                #pygame.display.update()
            if (e.key == K_ESCAPE):
                menu_selecao = menu_selecao-10
                #pygame.display.update()
#pygame.display.update()
   
