import pygame
pygame.init()
pygame.display.set_caption("Oblivion")
screen=pygame.display.set_mode((500,500))

background = pygame.image.load('PygameAssets-main/Arthur_jdr.png')

running = True

while running:
    screen.blit(background,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermer")
prout