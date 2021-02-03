import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("O ULTIMO YASUO")

JogoAtivo = True

while JogoAtivo:
    #Sistema que da o bloco
    Laranja  = (255, 123, 0)
    bloco = pygame.Rect(1, 1, 100, 100)
    pygame.draw.rect(screen, Laranja, bloco)
    pygame.display.flip()

    # trata os eventos da fila de eventos
    for evento in pygame.event.get():
       #print(evento)
        # verifica se o evento que veio eh
        # para fechar a janela
        if evento.type == pygame.QUIT:
            JogoAtivo = False
        if evento.type == pygame.KEYDOWN:
            print('uma tecla foi pressionada')
            if evento.key == pygame.K_ESCAPE:
                JogoAtivo = False
        if evento.type == pygame.KEYUP:
            print('uma tecla foi liberada')

pygame.quit()
