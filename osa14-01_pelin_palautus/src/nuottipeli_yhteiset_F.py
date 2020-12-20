import pygame

WIDTH = 790
HEIGHT = 410
VIIVASTON_ALKU_X = 50
VIIVOJEN_VALI = 50
YLIN_VIIVA_Y = 100      
ALIN_NUOTTI_Y = 325     
KUVAN_KOKO = 50
JESS_NO_AIKARAJA = 60   # 60 x mainin kesto    

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

tumma = (25, 25, 25)
turkoosi = (0, 205, 205)
punainen = (255, 0, 0)
keltainen = (255, 255, 0)

F_avain = pygame.transform.scale(pygame.image.load("bass_clef.png").convert_alpha(), (180, 230))  

K_f = pygame.K_f
K_g = pygame.K_g
K_a = pygame.K_a
K_h = pygame.K_h
K_c = pygame.K_c
nappaimet = [K_f, K_g, K_a, K_h, K_c]
      

