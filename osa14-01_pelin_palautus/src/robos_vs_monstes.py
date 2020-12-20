import pygame
import random
 
pygame.init()
naytto = pygame.display.set_mode((1920, 1080))
h1=pygame.font.SysFont("Corbel", 100)
h2=pygame.font.SysFont("Corbel", 24)
kello = pygame.time.Clock()
pygame.display.set_caption("Robos VS. Monsters")
robo = pygame.image.load("robo.png")
gameOver=False
inMainMenu=True
tasoKorkeus=1080-1080/6 #Tästä voi hallita, kuinka korkealla tai matalalla kenttä on.
enemy = pygame.image.load("hirvio.png")
enemyScaleY=enemy.get_height()
enemyScaleX=enemy.get_width()
enemy_hp2=pygame.transform.scale(enemy, (int(enemyScaleX*1.2), int(enemyScaleY*1.2))) #Isompien vihollisten skaalaukset
enemy_hp3=pygame.transform.scale(enemy, (int(enemyScaleX*1.4), int(enemyScaleY*1.4)))
coin = pygame.image.load("kolikko.png")
enemySpawnFrame=random.randint(10, 100) #Milloin tulee ensimmäinen vihollinen?
framesAfterEnemy=0 #Kuinka monta kuvaa edellisen vihollisen jälkeen
viholliset=[]
ammukset=[]
kolikot=[]
ammusSuunnat=[0,1,-1,2,-2] #Mihin suuntaan ammukset lentävät, jos niitä on useampi.
ammusTaso=1 #Kuinka monta ammusta ammutaan. 2 = 3 ammusta ja 3 = 5 ammusta.
ammusKoko=10 #Kuinka suuria ammukset ovat
taso=1
tasoBonukset=["koko","maara","koko","maara","koko"] #Mitä päivityksiä pelaaja saa, jos hän kerää kolikon.
robX=120
robY=(tasoKorkeus)-robo.get_height()
oikealle=False
vasemmalle=False
framesAfterBullet=1000
pisteet=0
ennatys=0
vaikeusTaso=1 #Mitä korkeampi vaikeustaso on, sitä enemmän vihollisia on.
 
def drawMainMenu():
    naytto.fill((255, 255, 255))
    drawCity()
    pygame.draw.rect(naytto, (0, 0, 0), (0, tasoKorkeus, 1920, 1080))
    naytto.blit(robo, (robX, robY))
    teksti = h1.render("Robos VS. Monsters", True, (0, 0, 0))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080/6))
    teksti = h2.render("Paina F2 aloittaaksesi, paina F3 katsoaksesi ohjeita tai paina ESC poistuaksesi pelistä", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080-1080/12))
    pygame.display.flip()
 
def drawHowToPlay():
    naytto.fill((0, 0, 0))
    teksti = h1.render("Ohjeet", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 60))
    teksti = h2.render("Hirviöt ovat hyökänneet Maapallolle, ja robo on värvätty apuun.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 220))
    teksti = h2.render("Puolusta kaupunkia niin kauan kuin mahdollista ampumalla hirviöitä. Jotkut hirviöt voivat pudottaa kolikoita, joilla robo pystyy päivittämään itseään.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 260))
    teksti = h2.render("Kuitenkin jos hirviö pääsee laskeutumaan maahan, niin robo menettää päivityksen. Jos hirviö laskeutuu, kun robo on tasolla 1, peli on menetetty.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 300))
    teksti = h2.render("Välillä roboa vastaan voi tulla tavallista isompi hirviö, joka tarvitsee kolme osumaa ennen kuin se tuhoutuu.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 340))
    teksti = h2.render("Mitä enemmän hirviöitä robo tuhoaa, sitä enemmän niitä hyökkää.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 380))
    teksti = h2.render("Robolla voi olla korkeintaan viisi päivitystä.", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 420))
    teksti = h1.render("Kontrollit", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 600))
    teksti = h2.render("Liikkuminen - A ja D tai nuolinäppäimet", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 750))
    teksti = h2.render("Ampuminen - LMB tai RMB", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 790))
    teksti = h2.render("Pelistä poistuminen - ESC", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 830))
    teksti = h2.render("Paina ESC palataksesi päävalikkoon", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1000))
    pygame.display.flip()
    inHowToPlay=True
    while inHowToPlay==True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    drawMainMenu()
                    inHowToPlay=False
                    break
 
 
 
def drawBG_rob(): #Näytön täyttö ja robon piirtäminen
    naytto.fill((255, 255, 255))
    drawCity()
    pygame.draw.rect(naytto, (0, 0, 0), (0, tasoKorkeus, 1920, 1080))
    naytto.blit(robo, (robX, robY))
 
def newGame():
    global viholliset
    viholliset=[]
    global framesAfterEnemy
    framesAfterEnemy=0
    global taso
    taso=1
    global ammusTaso
    ammusTaso=1
    global ammusKoko
    ammusKoko=10
    global pisteet
    pisteet=0
    global ammukset
    ammukset=[]
    global kolikot
    kolikot=[]
    global vaikeusTaso
    vaikeusTaso=1
    global oikealle
    oikealle=False
    global vasemmalle
    vasemmalle=False
 
def ammu():
    for suunta in ammusSuunnat[:2*(ammusTaso)-1]:
        ammukset.append((robX+robo.get_width()/2,robY,suunta)) #(x,y,suunta)
 
def drawCity():
    pygame.draw.rect(naytto, (130, 130, 130), (0, tasoKorkeus-200, 70, tasoKorkeus))#Taustalla olevan "kaupungin" piirtäminen
    pygame.draw.rect(naytto, (170, 170, 170), (70, tasoKorkeus-150, 120, tasoKorkeus))
    pygame.draw.rect(naytto, (100, 100, 100), (190, tasoKorkeus-400, 100, tasoKorkeus))
    pygame.draw.rect(naytto, (200, 200, 200), (290, tasoKorkeus-100, 200, tasoKorkeus))
    pygame.draw.rect(naytto, (160, 160, 160), (490, tasoKorkeus-250, 80, tasoKorkeus))
    pygame.draw.rect(naytto, (140, 140, 140), (550, tasoKorkeus-130, 250, tasoKorkeus))
    pygame.draw.rect(naytto, (80, 80, 80), (800, tasoKorkeus-500, 150, tasoKorkeus))
    pygame.draw.rect(naytto, (150, 150, 150), (950, tasoKorkeus-300, 300, tasoKorkeus))
    pygame.draw.rect(naytto, (170, 170, 170), (1250, tasoKorkeus-250, 190, tasoKorkeus))
    pygame.draw.rect(naytto, (210, 210, 210), (1440, tasoKorkeus-130, 150, tasoKorkeus))
    pygame.draw.rect(naytto, (70, 70, 70), (1590, tasoKorkeus-400, 200, tasoKorkeus))
    pygame.draw.rect(naytto, (180, 180, 180), (1790, tasoKorkeus-230, 250, tasoKorkeus))
 
    for i in range(6): #Valopylväät
        pygame.draw.rect(naytto, (50, 50, 50), (45+i*350, tasoKorkeus-225, 20, tasoKorkeus))
        pygame.draw.rect(naytto, (50, 50, 50), (65+i*350, tasoKorkeus-225, 60, 20))
 
 
def drawBullets():
    for ammus in ammukset: #Poistetaan näytön ulkopuolella olevat ammukset
        if ammus[1]<=-40:
            ammukset.remove(ammus)
    
    for ammus in range(len(ammukset)):
        uusiAmmus=ammukset[ammus]
        pygame.draw.circle(naytto, (0, 0, 0), (uusiAmmus[0]+uusiAmmus[2], uusiAmmus[1]-1), ammusKoko)
        ammukset[ammus]=(uusiAmmus[0]+uusiAmmus[2],uusiAmmus[1]-5,uusiAmmus[2]) #uusiAmmus[0]=X, uusiAmmus[1]=Y, uusiAmmus[2]=Ammuksen suunta
 
def spawnEnemy():
    if random.randint(0,10)==10: #Spawnaa suuremman hirviön
        viholliset.append((random.randint(100,1800),-100,3)) #(X,Y,HP)
    else:
        viholliset.append((random.randint(100,1800),-100, 1))
 
def drawEnemy():
    global enemy
    for vihollinen in range(len(viholliset)):
        uusiVihollinen=viholliset[vihollinen]
        if uusiVihollinen[2]==3:
            naytto.blit(enemy_hp3,(uusiVihollinen[0],uusiVihollinen[1]+2))
        elif uusiVihollinen[2]==2:
            naytto.blit(enemy_hp2,(uusiVihollinen[0],uusiVihollinen[1]+2))
        else:
            naytto.blit(enemy,(uusiVihollinen[0],uusiVihollinen[1]+2))
        viholliset[vihollinen]=(uusiVihollinen[0],uusiVihollinen[1]+2,uusiVihollinen[2])
 
    for vihollinen in viholliset: #Pääsikö jokin vihollinen maahan asti?
        if vihollinen[1]+(1+(vihollinen[2]-1)*0.2)*enemy.get_height()>=tasoKorkeus:
            viholliset.remove(vihollinen)
            levelDown()
 
def drawCoins():
    for kolikko in range(len(kolikot)):
        uusiKolikko=kolikot[kolikko]
        if uusiKolikko[1]+coin.get_height()>=tasoKorkeus: #Kolikon on maassa
            naytto.blit(coin,(uusiKolikko[0],tasoKorkeus-coin.get_height()))
        else:
            naytto.blit(coin,(uusiKolikko[0],uusiKolikko[1]+4))
            kolikot[kolikko]=(uusiKolikko[0],uusiKolikko[1]+4)
 
def areHits(): #Onko osuttu hirviöön
    vihollinenIndex=0 #Tätä käytetään, koska en saanut peliä toimimaan tavallisella list.index() funktiolla.
    for vihollinen in viholliset:
        for ammus in ammukset:
            if vihollinen[0]<=ammus[0]+ammusKoko/2<=vihollinen[0]+(1+(vihollinen[2]-1)*0.2)*enemy.get_width() and vihollinen[1]<=ammus[1]+ammusKoko/2<=vihollinen[1]+(1+(vihollinen[2]-1)*0.2)*enemy.get_height():
                if vihollinen[2]==1: #Jos 1 HP, niin tapetaan
                    if random.randint(0,7)==5: #Hallitsee kolikon pudottamisen todennäköisyyttä
                        kolikot.append((vihollinen[0]+enemy.get_width()/2-coin.get_width()/2,vihollinen[1]+enemy.get_height()/2-coin.get_height()/2)) #Jos käy tuuri, vihollisen kohdalle spawnataan kolikko.
                    viholliset.remove(vihollinen)
                    ammukset.remove(ammus)
                    return True
                else: 
                    viholliset[vihollinenIndex]=(vihollinen[0],vihollinen[1],vihollinen[2]-1) #Vähennä 1 HP
                    ammukset.remove(ammus)
        vihollinenIndex+=1
 
def catchCoin():
    for kolikko in kolikot:
        if robX<=kolikko[0]+coin.get_width()/2<=robX+robo.get_width() and robY<=kolikko[1]+coin.get_height():
            kolikot.remove(kolikko)
            levelUp()
 
def levelUp():
    global taso
    global ammusKoko
    global ammusTaso
    if taso==len(tasoBonukset):
        pass
    else:
        if tasoBonukset[taso-1]=="maara": #Päivitetäänkö määrää vai kokoa?
            ammusTaso+=1
            taso+=1
        elif tasoBonukset[taso-1]=="koko":
            ammusKoko+=5
            taso+=1
 
def levelDown():
    global taso
    global ammusKoko
    global ammusTaso
    if taso==1:
        gameOver()
    else:
        if tasoBonukset[taso-2]=="maara":
            ammusTaso-=1
            taso-=1
        elif tasoBonukset[taso-2]=="koko":
            ammusKoko-=5
            taso-=1
 
 
def drawPoints(): #Tulostetaan pistemäärä
    teksti = h1.render(f"Pisteet:{pisteet}", True, (255, 255, 255))
    naytto.blit(teksti, (1920-teksti.get_width()-20, 1080-teksti.get_height()-20))
 
def drawLevel(): #Tulostetaan robon taso
    teksti = h1.render(f"Taso:{taso}", True, (255, 255, 255))
    naytto.blit(teksti, (20, 1080-teksti.get_height()-20))
 
def gameOver():
    global ennatys
    gameOver=True
    teksti = h1.render("GAME OVER", True, (0, 0, 0))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080/6))
    teksti = h2.render("Paina F2 yrittääksesi uudelleen tai paina ESC poistuaksesi pelistä", True, (255, 255, 255))
    naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080-1080/12))
    if pisteet>ennatys: #Onko uusi ennätys?
        ennatys=pisteet
        teksti = h2.render(f"Uusi ennätys: {pisteet} pistettä", True, (0, 0, 0))
        naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080/6+120))
    else:
        teksti = h2.render(f"Pisteet: {pisteet}", True, (0, 0, 0))
        naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080/6+120))
        teksti = h2.render(f"Ennätys: {ennatys}", True, (0, 0, 0))
        naytto.blit(teksti, ((1920/2)-(teksti.get_width()/2), 1080/6+160))
    pygame.display.flip()
    while gameOver==True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
                if tapahtuma.key == pygame.K_F2:
                    newGame()
                    gameOver=False
                    break
    
 
#Tästä alkaa varsinainen koodin suoritus
 
 
drawMainMenu() #Alustus
 
while inMainMenu==True: #Päävalikon looppi
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()
            if tapahtuma.key == pygame.K_F3:
                drawHowToPlay()
            if tapahtuma.key == pygame.K_F2:
                newGame()
                inMainMenu=False
                break
            
            
    
while True: #Pelilooppi
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d:
                oikealle = True
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()
 
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d:
                oikealle = False
 
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN and framesAfterBullet>=30: #Tästä voi hallinnoida, kuinka usein pelaaja voi ampua.
            framesAfterBullet=0
            ammu()
 
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    if oikealle and robX<1920-robo.get_width():
        robX += 5
    if vasemmalle and robX>0:
        robX -= 5
 
    if framesAfterEnemy>=enemySpawnFrame:
        enemySpawnFrame=random.randint(int(400/vaikeusTaso), int(500/vaikeusTaso)) #Tästä voi hallinnoida, kuinka usein vihollisia spawnaa
        framesAfterEnemy=0
        spawnEnemy()
 
    if areHits(): #Onko osuma
        pisteet+=1
        if pisteet//10==pisteet/10: #Jos pistemäärä on luvun 10 moninkerta, vaikeustasoa nostetaan.
            vaikeusTaso+=0.5
    
    drawBG_rob()
    drawBullets()
    drawEnemy()
    drawPoints()
    drawCoins()
    drawLevel()
    catchCoin()
 
    framesAfterBullet+=1
    framesAfterEnemy+=1
    kello.tick(144)
    pygame.display.flip()