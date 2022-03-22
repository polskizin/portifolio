import pygame
import random
import time
from pygame.locals import *

def escolher_cor_aleatoria():
    pisca_vermelho = {'cor':cor_vermelha,'pos':(251,282),'raio':130}
    pisca_verde = {'cor': cor_verde, 'pos': (251, 282), 'raio': 130}
    pisca_laranja = {'cor': cor_laranja, 'pos': (251, 282), 'raio': 130}
    pisca_azul = {'cor': cor_azul, 'pos': (251, 282), 'raio': 130}
    cores=[pisca_azul,pisca_verde,pisca_vermelho,pisca_laranja]
    return random.choice(cores)

def piscar_cores(lista_cores):
    for cor in lista_cores:
        if cor['cor']== cor_verde:
            pygame.draw.circle(interface,cor['cor'],cor['pos'],cor['raio'],draw_top_right=True)
        elif cor['cor']== cor_laranja:
            pygame.draw.circle(interface,cor['cor'],cor['pos'],cor['raio'],draw_bottom_left=True)
        elif cor['cor']== cor_azul:
            pygame.draw.circle(interface,cor['cor'],cor['pos'],cor['raio'],draw_top_left=True)
        elif cor['cor']== cor_vermelha:
            pygame.draw.circle(interface,cor['cor'],cor['pos'],cor['raio'],draw_bottom_right=True)

        pygame.display.update()
        time.sleep(0.3)
        interface.blit(fundo,(0,30))
        pygame.display.update()
        time.sleep(0.3)

def obter_resposta(quantidade_cores):
    resposta_usuario = []
    while quantidade_cores > 0:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_verde.collidepoint(mouse):
                    resposta_usuario.append(cor_verde)
                    quantidade_cores -= 1
                elif botao_laranja.collidepoint(mouse):
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    resposta_usuario.append(cor_vermelha)
                    quantidade_cores -= 1
                elif botao_azul.collidepoint(mouse):
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
    return resposta_usuario

def restart():
    texto_restart = fonte_botoes.render('RESTART',True,cor_preto)
    interface.blit(fundo,(0,30))
    botao_restart = pygame.draw.rect(interface,cor_branca,(175,70,155,60))
    interface.blit(texto_restart,(176,73))
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_restart.collidepoint(mouse):
                    interface.blit(fundo,(0,30))
                    pygame.display.update()
                    return True


pygame.init()
interface = pygame.display.set_mode((500,530))
fonte_botoes = pygame.font.SysFont('Arial',40)
fonte_contagem = pygame.font.SysFont('Arial',30)
status_bar = pygame.Surface((interface.get_width(),30))

fundo = pygame.image.load(('Imagem.png'))

#definindo cores

cor_preto = (0,0,0)
cor_branca = (255,255,255)
cor_vermelha = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)

#Poligonos da escolha do mouse
botao_azul = pygame.draw.circle(interface,cor_azul,center=(251,282),radius=130,draw_top_left=True)
botao_verde = pygame.draw.circle(interface,cor_verde,center=(251,282),radius=130,draw_top_right=True)
botao_vermelho = pygame.draw.circle(interface,cor_vermelha,center=(251,282),radius=130,draw_bottom_right=True)
botao_laranja = pygame.draw.circle(interface,cor_laranja,center=(251,282),radius=130,draw_bottom_left=True)

#textos
texto_comeco = fonte_botoes.render('START',True,cor_preto)
pontos = 0
cores_sequencia = []
jogando = False

while not jogando:
    interface.blit(fundo,(0,30))
    botao_comecar = pygame.draw.rect(interface,cor_branca,(180,70,150,60))
    interface.blit(texto_comeco,(200,74))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if botao_comecar.collidepoint(mouse):
                jogando = True

interface.blit(fundo,(0,30))
pygame.display.update()

while jogando:
    status_bar.fill(cor_preto)
    pontuacao = fonte_contagem.render("Pontos:" +str(pontos),True,(cor_branca))
    status_bar.blit(pontuacao,(0,0))
    interface.blit(status_bar,(0,0))
    pygame.display.update()
    time.sleep(.5)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()
    cores_sequencia.append(escolher_cor_aleatoria())
    piscar_cores(cores_sequencia)
    resposta_jogador = obter_resposta(len(cores_sequencia))
    sequencia_cores = []
    for cor in cores_sequencia:
        sequencia_cores.append(cor['cor'])
    if sequencia_cores == resposta_jogador:
        pontos += 1
    else:
        jogando == restart()
        if jogando:
            pontos = 0
            cores_sequencia = []








