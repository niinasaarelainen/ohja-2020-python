import pygame, random


pygame.init()
naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Robotin paikka")

robo = pygame.image.load("robo.png")
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()



def aseta():
    robon_random_x = random.randint(0, 640 - robon_leveys)
    robon_random_y = random.randint(0, 480 - robon_korkeus)
    naytto.blit(robo, (robon_random_x, robon_random_y))
    pygame.display.flip()
    while True:
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                hiiri_x = tapahtuma.pos[0]
                hiiri_y = tapahtuma.pos[1]
                if hiiri_x >= robon_random_x and hiiri_x <= robon_random_x + robon_leveys and hiiri_y >= robon_random_y and hiiri_y <= robon_random_y + robon_korkeus:
                   robon_random_x = random.randint(0, 640 - robon_leveys)
                   robon_random_y = random.randint(0, 480 - robon_korkeus)
                   naytto.fill((0, 0, 0))
                   naytto.blit(robo, (robon_random_x, robon_random_y))
                   pygame.display.flip()
               
            

aseta()
