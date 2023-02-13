import sys, pygame, pygame.mixer
from pygame.locals import *
import time
import _thread
import sys
import random

#  -------------------- instâncias de globais :------------------------------------------------------
#SCREEN
bgHD = pygame.image.load('./img/bgHD.png')
screen_widthHD = 500
screen_heightHD = 720
pontuacao = 0
gameOver = False

screen_width = screen_widthHD 
screen_height = screen_heightHD
bg = bgHD

#PLAYER
player_height = player_width = 95
velP = 7
velE = 3

player_x = 0
player_y = screen_height - player_height

#ENEMY
enemyImgHD = pygame.image.load('./img/enemyHD.png')
enemiesL1 = []
enemiesL2 = []
enemiesL3 = []

enemiesL1.append([20,20])
enemiesL1.append([160,20])
enemiesL1.append([270,20])
enemiesL1.append([390,20])
enemiesL2.append([20,110])
enemiesL2.append([160,110])
enemiesL2.append([270,110])
enemiesL2.append([390,110])
enemiesL3.append([20,200])
enemiesL3.append([160,200])
enemiesL3.append([270,200])
enemiesL3.append([390,200])
enemy_height = 88
enemy_width = 110
enemyImg = enemyImgHD

#PLAYER BULLETS
pewImgAhri = pygame.image.load('./img/pewAhri.png')
pewImgAkali = pygame.image.load('./img/pewAkali.png')
pewImgEvelyn = pygame.image.load('./img/pewEvelyn.png')
pewImgKaisa = pygame.image.load('./img/pewKaisa.png')
pewImgEnemy = pygame.image.load('./img/pewImgEnemy.png')
pew_x = 0
pew_y = 0

pews = []
enemyPews = []

#gameOver
imgGame_Over = pygame.image.load('./img/menu/gameOver.png')

def pewDoMau(tamanho, height):
    global enemyPews

    while True:       
        enemyPews.append([random.choice([230,560, 600, 120, 300]),0])
        time.sleep(0.5)

pygame.init()
pygame.display.set_caption('K/DA INVADER')
pewSound = pygame.mixer.Sound('./song/pewSound.mp3')
bgSong = pygame.mixer.Sound('./song/bgSong.mp3')
hitPlayer = pygame.mixer.Sound('./song/hit_on_player.mp3')
pygame.display.set_icon(pewImgEvelyn)

bgSong.play()
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
done = False
_thread.start_new_thread(pewDoMau, (20,screen_height))

# Definindo proporções da tela
pygame.init()
height = 500
width = 720
screen.fill((0,0,0))

# Definindo as Fontes e textos universais

tituloFont = pygame.font.SysFont('Times New Roman', 30)
bonecasFont = pygame.font.SysFont('Arial', 25)
txtVoltar = tituloFont.render('Voltar', False, (255, 255, 255))
tituloPoints = pygame.font.SysFont('Times New Roman', 15)
txtPoints = tituloPoints.render('PONTOS:', False, (255,255,255))
# Definindo valores para telas

clock = pygame.time.Clock()
done = False
resumeGame = False
startGame = False
resumeAbout = False
resumeHelp = False
howToPlay = False
aboutGame = False

#  -------------------- Tela de menu:------------------------------------------------------

# Definindo e verificando imagens 
imgFundo = pygame.image.load('./img/menu/fundo.png')
if (imgFundo == None):
    print('imagem do fundo não encontrada')
    quit()

imgKaisa_PB = pygame.image.load('./img/menu/kaisa_pb.jpg')
if (imgKaisa_PB == None):
    print('imagem da Kaisa_pb não encontrada')
    quit()

imgAhri_PB = pygame.image.load('./img/menu/ahri_pb.jpg')
if (imgAhri_PB == None):
    print('imagem da Ahri_pb não encontrada')
    quit()
    
imgAkali_PB = pygame.image.load('./img/menu/akali_pb.jpg')
if (imgAkali_PB == None):
    print('imagem da Akali_pb não encontrada')
    quit()
    
imgEvelynn_PB = pygame.image.load('./img/menu/eve_pb.jpg')
if (imgEvelynn_PB == None):
    print('imagem da Evelynn não encontrada')
    quit()

imgKaisa_Selected = pygame.image.load('./img/menu/kaisa.jpg')
if (imgKaisa_Selected == None):
    print('imagem da Kaisa não encontrada')
    quit()

imgAhri_Selected = pygame.image.load('./img/menu/ahri.jpg')
if (imgAhri_Selected == None):
    print('imagem da Ahri não encontrada')
    quit()
    
imgAkali_Selcted = pygame.image.load('./img/menu/akali.jpg')
if (imgAkali_Selcted == None):
    print('imagem da Akali não encontrada')
    quit()

imgEvelynn_Selcted = pygame.image.load('./img/menu/eve.jpg')
if (imgEvelynn_Selcted == None):
    print('imagem da Evelynn não encontrada')
    quit()

imgLogoGame = pygame.image.load('./img/menu/logo.jpg')
if (imgLogoGame == None):
    print('imagem da Logo não encontrada')
    quit()


x_kaisa = 30
x_ahri =  x_kaisa + 84 + 30
x_eve = x_ahri + 84 + 30
x_akali = x_eve + 84 + 30
y_selection = 200

button_color_Start = (207, 122, 154)
button_selected = (90, 56, 102)
button_not_selected = (140, 87, 158)
button_color_kaisa=  button_not_selected
button_color_ahri=  button_not_selected
button_color_akali=  button_not_selected
button_color_eve=  button_not_selected


imgKaisa = imgKaisa_PB
imgAhri =  imgAhri_PB
imgAkali = imgAkali_PB
imgEvelynn = imgEvelynn_PB


tituloMenu = tituloFont.render('Escolha sua personagem:', False, (255, 255, 255))
txtKaisa = bonecasFont.render('Kaisa', False, (255, 255, 255))
txtAhri = bonecasFont.render('Ahri', False, (255, 255, 255))
txtAkali = bonecasFont.render('Akali', False, (255, 255, 255))
txtEve = bonecasFont.render('Evelynn', False, (255, 255, 255))
txtSelected = tituloFont.render('Personagem selecionado: ' , False, (255, 255, 255))
txtStart = tituloFont.render('Start ', False, (255, 255, 255))
txtHelp = tituloFont.render('Help ', False, (255, 255, 255))
txtSobre = tituloFont.render('Sobre ', False, (255, 255, 255))

#  -------------------- Tela de Sobre:------------------------------------------------------
imgSobre = pygame.image.load('./img/menu/sobre.jpg')
if (imgSobre == None):
    print('imagem do Sobre não encontrada')
    quit()

button_color_Sobre = (222, 11, 95)

#  -------------------- Tela de Help:------------------------------------------------------
imgHelp = pygame.image.load('./img/menu/help.jpg')
if (imgHelp == None):
    print('imagem do Help não encontrada')
    quit()
button_color_help = (222, 11, 95)

while not done:
    resumeGame = False
    resumeAbout = False
    resumeHelp = False
    howToPlay = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    screen.fill((0, 0, 0))
    screen.blit(imgFundo,(-5, 150))
    screen.blit(imgLogoGame,(125, 5))
    
    screen.blit(imgKaisa, (x_kaisa,y_selection))
    screen.blit(imgAhri, (x_ahri,y_selection))
    screen.blit(imgAkali, (x_akali,y_selection))
    screen.blit(imgEvelynn, (x_eve,y_selection))


    button_kaisa = pygame.Rect(x_kaisa, 364, 86, 30)
    pygame.draw.rect(screen, button_color_kaisa, button_kaisa)

    button_ahri = pygame.Rect(x_ahri, 364, 86, 30)
    pygame.draw.rect(screen, button_color_ahri, button_ahri)

    button_akali = pygame.Rect(x_akali, 364, 86, 30)
    pygame.draw.rect(screen, button_color_akali, button_akali)

    button_eve = pygame.Rect(x_eve, 364, 86, 30)
    pygame.draw.rect(screen, button_color_eve, button_eve)

    button_start = pygame.Rect(200, 500, 100, 30)
    pygame.draw.rect(screen, button_color_Start, button_start)

    button_help = pygame.Rect(200, 550, 100, 30)
    pygame.draw.rect(screen, button_color_Start, button_help)

    button_sobre = pygame.Rect(200, 600, 100, 30)
    pygame.draw.rect(screen, button_color_Start, button_sobre)


    screen.blit(tituloMenu,(100, 150))
    screen.blit(txtKaisa,((x_kaisa + 18), 364))
    screen.blit(txtAhri,((x_ahri + 25), 364))
    screen.blit(txtAkali,((x_akali + 22), 364))
    screen.blit(txtEve,((x_eve + 8), 364))
    screen.blit(txtSelected,(30 , 400))
    screen.blit(txtStart,(220 , 497))
    screen.blit(txtHelp,(220 , 547))
    screen.blit(txtSobre,(215 , 597))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos  


        if button_kaisa.collidepoint(mouse_pos):
                button_color_kaisa=  button_selected
                button_color_ahri=  button_not_selected
                button_color_akali=  button_not_selected
                button_color_eve=  button_not_selected

                imgKaisa = imgKaisa_Selected
                imgAhri =  imgAhri_PB
                imgAkali = imgAkali_PB
                imgEvelynn = imgEvelynn_PB
                player = pygame.image.load('./img/kaisaHD.png')
                pewImg = pewImgKaisa
                txtSelected = tituloFont.render('Personagem selecionado: KAISA ', False, (255, 255, 255))


        if button_ahri.collidepoint(mouse_pos):
                button_color_kaisa=  button_not_selected
                button_color_ahri=  button_selected
                button_color_akali=  button_not_selected
                button_color_eve=  button_not_selected

                imgKaisa = imgKaisa_PB
                imgAhri =  imgAhri_Selected
                imgAkali = imgAkali_PB
                imgEvelynn = imgEvelynn_PB
                player = pygame.image.load('./img/ahriHD.png')
                pewImg = pewImgAhri
                txtSelected = tituloFont.render('Personagem selecionado: AHRI ' , False, (255, 255, 255))


        if button_akali.collidepoint(mouse_pos):
                button_color_kaisa=  button_not_selected
                button_color_ahri=  button_not_selected
                button_color_akali=  button_selected
                button_color_eve=  button_not_selected

                imgKaisa = imgKaisa_PB
                imgAhri =  imgAhri_PB
                imgAkali = imgAkali_Selcted
                imgEvelynn = imgEvelynn_PB
                player = pygame.image.load('./img/akaliHD.png')
                pewImg = pewImgAkali
                txtSelected = tituloFont.render('Personagem selecionado: AKALI', False, (255, 255, 255))

            
        if button_eve.collidepoint(mouse_pos):
                button_color_kaisa=  button_not_selected
                button_color_ahri=  button_not_selected
                button_color_akali=  button_not_selected
                button_color_eve=  button_selected

                imgKaisa = imgKaisa_PB
                imgAhri =  imgAhri_PB
                imgAkali = imgAkali_PB
                imgEvelynn = imgEvelynn_Selcted
                player = pygame.image.load('./img/evelynHD.png')
                pewImg = pewImgEvelyn
                txtSelected = tituloFont.render('Personagem selecionado: EVELLYN'  , False, (255, 255, 255))

        if button_start.collidepoint(mouse_pos):
            startGame = True

        if button_help.collidepoint(mouse_pos):
            howToPlay = True

        if button_sobre.collidepoint(mouse_pos):
            aboutGame = True

    if startGame:
        screen.fill((0, 0, 0))
        gameOver = False
        while not resumeGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resumeGame = True
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        pews.append([player_x+(player_height/2),screen_height-player_height])
                        pewSound.play()

            clock.tick(60)
            pressed = pygame.key.get_pressed()   
            if pressed[pygame.K_LEFT] and player_x >= 0: 
                player_x -= velE
            if pressed[pygame.K_RIGHT] and player_x <= screen_width-player_width: 
                player_x += velE

            for b in range(len(pews)): 
                pews[b][1] -= velP 
            for b in range(len(enemyPews)): 
                enemyPews[b][1] += velE
            
            for pew in pews[:]:  
                for enemy in enemiesL3[:]:
                    if pew[0] >= enemy[0] and pew[0] <= (enemy[0]+enemy_width) and pew[1] <= enemy[1]+enemy_height:
                        pontuacao+=1
                        hitPlayer.play()
                        pews.remove(pew)
                        enemiesL3.remove(enemy)
                        break
                for enemy in enemiesL2[:]:
                    if pew[0] >= enemy[0] and pew[0] <= (enemy[0]+enemy_width) and pew[1] <= enemy[1]+enemy_height:
                        pontuacao+=1
                        hitPlayer.play()
                        pews.remove(pew)
                        enemiesL2.remove(enemy)
                        break
                for enemy in enemiesL1[:]:
                    if pew[0] >= enemy[0] and pew[0] <= (enemy[0]+enemy_width) and pew[1] <= enemy[1]+enemy_height:
                        pontuacao+=1
                        hitPlayer.play()
                        pews.remove(pew)
                        enemiesL1.remove(enemy)
                        break
            if len(enemiesL1) == 0 and len(enemiesL2) == 0 and len(enemiesL3) == 0:
                enemiesL1.append([20,20])
                enemiesL1.append([160,20])
                enemiesL1.append([270,20])
                enemiesL1.append([390,20])
                enemiesL2.append([20,110])
                enemiesL2.append([160,110])
                enemiesL2.append([270,110])
                enemiesL2.append([390,110])
                enemiesL3.append([20,200])
                enemiesL3.append([160,200])
                enemiesL3.append([270,200])
                enemiesL3.append([390,200])
            for enemyPew in enemyPews[:]:  
                    if enemyPew[0] >= player_x and enemyPew[0] <= (player_x+player_width) and enemyPew[1] >= player_y:
                        #enemyPews.remove(enemyPew)
                        gameOver = True
                        resumeGameOver = False
                        resumeGame = True
                        startGame = False
                        pontuacao = 0
                        pews = []
                        enemyPews = []
                        enemiesL1 = []
                        enemiesL2 = []
                        enemiesL3 = []
                        
            # Iterate over a slice copy if you want to mutate a list.
            for pew in pews[:]:
                if pew[1] < 0:
                    pews.remove(pew)

            for enemyPew in enemyPews[:]:
                if enemyPew[1] > screen_height:
                    enemyPews.remove(enemyPew)
            
            screen.blit(bg, (0, 0))
            for pew in pews:
                screen.blit(pewImg, pygame.Rect(pew[0], pew[1], 0, 0)) 

            for enemyPew in enemyPews:
                screen.blit(pewImgEnemy, pygame.Rect(enemyPew[0], enemyPew[1], 0, 0)) 
            for enemy in enemiesL3:
                screen.blit(enemyImg, pygame.Rect(enemy[0], enemy[1], 0, 0))
            for enemy in enemiesL2:
                screen.blit(enemyImg, pygame.Rect(enemy[0], enemy[1], 0, 0))
            for enemy in enemiesL1:
                screen.blit(enemyImg, pygame.Rect(enemy[0], enemy[1], 0, 0))

            pygame.draw.rect(screen, (0,0,0),(0, 0, screen_widthHD, 17))
            screen.blit(txtPoints, (0,0))
            txtPointsValue = tituloPoints.render(str(pontuacao),False, (255,255,255))
            screen.blit(txtPointsValue, (70,0))
            screen.blit(player,(player_x,player_y))
            pygame.display.flip()

    elif howToPlay:
        screen.fill((0, 0, 0))
        while not resumeHelp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resumeHelp = True
                    done = True
                screen.fill((0, 0, 0))
                screen.blit(imgHelp, (0,0))
                button_back = pygame.Rect(0, 0, 100, 30)
                pygame.draw.rect(screen, button_color_help, button_back)
                screen.blit(txtVoltar, (5,0))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  

                    if button_back.collidepoint(mouse_pos):
                        resumeHelp = True
                        howToPlay = False

                pygame.display.flip() 
                clock.tick(100) 
    elif aboutGame:
        screen.fill((0, 0, 0))
        while not resumeAbout:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resumeAbout = True
                    done = True
                screen.fill((0, 0, 0))
                screen.blit(imgSobre, (0,0))
                button_back = pygame.Rect(0, 0, 100, 30)
                pygame.draw.rect(screen, button_color_Sobre, button_back)
                screen.blit(txtVoltar, (5,0))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  

                    if button_back.collidepoint(mouse_pos):
                        resumeAbout = True
                        aboutGame = False

                pygame.display.flip() 
                clock.tick(100)
    elif gameOver:
        screen.fill((0, 0, 0))
        while not resumeGameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resumeGameOver = True
                    done = True
                txtBackMenu = tituloFont.render('Voltar ao menu', False,(225, 255, 255))
                button_back = pygame.Rect(150, 355, 200, 30)
                screen.blit(imgGame_Over, (150,200))
                pygame.draw.rect(screen, button_color_help, button_back)
                screen.blit(txtBackMenu, (158,355))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  
                    if button_back.collidepoint(mouse_pos):                           
                        resumeGameOver = True
                        gameOver = False

                pygame.display.flip() 
                clock.tick(100)  
    else:                 
        pygame.display.flip()
        clock.tick(100)