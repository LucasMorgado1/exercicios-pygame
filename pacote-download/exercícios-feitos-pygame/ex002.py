import pygame

altura1 = int(input("Digite um numero acima de 100 e menos de 2000 para o tamanho da janela: "))
altura2 = int(input("Digite outro numero acima de 100 e menos de 2000 para o tamanho da janela: "))

bloco1 = int(input("Digite um numero inteiro para posicionar o retangulo: "))
bloco2 = int(input("Digite um outro numero inteiro para posicionar o retangulo: "))

pygame.init()
screen = pygame.display.set_mode((altura1, altura2))
pygame.display.set_caption("O ULTIMO YASUO")

JogoAtivo = True

while JogoAtivo:
    #Sistema que da o bloco
    Laranja  = (122, 255, 194)
    bloco = pygame.Rect((altura1 - bloco1)/2, (altura2 - bloco2)/2, bloco1, bloco2)
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
