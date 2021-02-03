import pygame

altura1 = int(input("Digite um numero acima de 100 e menos de 2000 para o tamanho da janela: "))
altura2 = int(input("Digite outro numero acima de 100 e menos de 2000 para o tamanho da janela: "))

bloco1 = int(input("Digite um numero inteiro para posicionar o retangulo: "))
bloco2 = int(input("Digite um outro numero inteiro para posicionar o retangulo: "))

pygame.init()
screen = pygame.display.set_mode((altura1, altura2))
pygame.display.set_caption("O ULTIMO YASUO")

JogoAtivo = True
um = 1

Laranja = (122, 255, 194)
bloco = pygame.Rect(um, um, bloco1, bloco2) #Setar fora para nao comer muita memoria

while JogoAtivo:
    #Sistema que da o bloco
    screen.fill((0, 0, 0)) #Sempre deixa a cor preta quando resetar
    pygame.draw.rect(screen, Laranja, bloco)

    # trata os eventos da fila de eventos
    for evento in pygame.event.get():
       #print(evento)
        # verifica se o evento que veio eh
        # para fechar a janela
        if evento.type == pygame.QUIT:
            JogoAtivo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                JogoAtivo = False
            if evento.key == pygame.K_s:
                bloco = pygame.Rect(um, um, bloco1, bloco2)
                um += 10
    pygame.display.flip() #Sempre imprime o bloco
pygame.quit()
