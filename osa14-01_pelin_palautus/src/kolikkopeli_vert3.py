import pygame
from random import randint
class Kolikko:
	def __init__(self, kuva, x: int, y: int):
		self.kuva = kuva
		self.x = x
		self.y = y
 
class Hirvio:
	def __init__(self, kuva, x: int, y: int, nopeus: int):
		self.kuva = kuva
		self.x = x
		self.y = y
		self.nopeus = nopeus
 
class Kolikkopeli:
	def __init__(self):
		pygame.init()
		self.pisteet = 0
		self.elamat = 3
		self.nopeus = 3
 
		self.naytto = pygame.display.set_mode((640, 480))
		self.fontti = pygame.font.SysFont("Arial", 24)
 
		pygame.display.set_caption("Kolikkopeli")
 
		#Robo
		self.robo = pygame.image.load("robo.png")
		self.robo_x = 320
		self.robo_y =480-self.robo.get_height()
		self.vasemmalle = False
		self.oikealle = False
		self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
 
		#Kolikko
		self.kolikot = []
		for i in range(11):
			self.kolikko = Kolikko(pygame.image.load("kolikko.png"), 0, 0)
			self.kolikko.x = randint(0, 640-self.kolikko.kuva.get_width())
			self.kolikko.y = -randint(100, 5000)
			self.naytto.blit(self.kolikko.kuva, (self.kolikko.x, self.kolikko.y))
			self.kolikot.append(self.kolikko)
 
		#Hirvio
		self.hirviot = []
		for i in range(7):
			self.hirvio = Hirvio(pygame.image.load("hirvio.png"), 0, 0, self.nopeus)
			self.hirvio.x = randint(0, 640-self.hirvio.kuva.get_width())
			self.hirvio.y = -randint(100, 1000)
			self.naytto.blit(self.hirvio.kuva, (self.hirvio.x, self.hirvio.y))
			self.hirviot.append(self.hirvio)
 
		self.kello = pygame.time.Clock()
		self.silmukka()
 
	def silmukka(self):
		while True:
			self.tutki_tapahtumat()
			self.piirra_naytto()
	
	def uusi_peli(self):
		Kolikkopeli()
 
	def tutki_tapahtumat(self):
		for tapahtuma in pygame.event.get():
			if tapahtuma.type == pygame.KEYDOWN:
				if tapahtuma.key == pygame.K_LEFT:
					self.vasemmalle = True
				if tapahtuma.key == pygame.K_RIGHT:
					self.oikealle = True
				if tapahtuma.key == pygame.K_F2:
					self.uusi_peli()
				if tapahtuma.key == pygame.K_ESCAPE:
					exit()
 
			if tapahtuma.type == pygame.KEYUP:
				if tapahtuma.key == pygame.K_LEFT:
					self.vasemmalle = False
				if tapahtuma.key == pygame.K_RIGHT:
					self.oikealle = False
 
			if tapahtuma.type == pygame.QUIT:
				exit()
		
		if self.peli_lapi() != True and self.peli_ohi() != True:
	
			#Robo
			if self.oikealle and self.robo_x <= 640-self.robo.get_width():
				self.robo_x += 6
			if self.vasemmalle and self.robo_x >= 0:
				self.robo_x -= 6
 
			#Kolikko
			for kolikko in self.kolikot:
				self.naytto.blit(kolikko.kuva, (kolikko.x, kolikko.y))
				kolikko.y += 3
				if kolikko.y+kolikko.kuva.get_height() > 480:
					kolikko.x = randint(0, 640-kolikko.kuva.get_width())
					kolikko.y = -kolikko.kuva.get_height()
 
				if kolikko.y+kolikko.kuva.get_height() >= self.robo_y:
					robo_keski = self.robo_x+self.robo.get_width()/2
					kolikko_keski = kolikko.x+kolikko.kuva.get_width()/2
					if abs(robo_keski-kolikko_keski) <= (self.robo.get_width()+kolikko.kuva.get_width())/2:
						# robotti sai kolikon kiinni
						kolikko.x = 1000
						kolikko.y = 0
						self.pisteet += 1
 
			#Hirviö
			for hirvio in self.hirviot:
				self.naytto.blit(hirvio.kuva, (hirvio.x, hirvio.y))
				hirvio.y += hirvio.nopeus
				if hirvio.y+hirvio.kuva.get_height() > 480:
					hirvio.x = randint(0, 640-hirvio.kuva.get_width())
					hirvio.y = -hirvio.kuva.get_height()
 
				if hirvio.y+hirvio.kuva.get_height() >= self.robo_y:
					robo_keski = self.robo_x+self.robo.get_width()/2
					kolikko_keski = hirvio.x+hirvio.kuva.get_width()/2
					if abs(robo_keski-kolikko_keski) <= (self.robo.get_width()+hirvio.kuva.get_width())/2:
						# robotti osuu hirviöön
						hirvio.x = randint(0, 640-hirvio.kuva.get_width())
						hirvio.y = -hirvio.kuva.get_height()
						self.elamat -= 1	
			
		else:
			return
 
	def piirra_naytto(self):
		self.naytto.fill((105, 105, 105))
		teksti = self.fontti.render(f"Pisteet: {self.pisteet}", True, (255, 0, 0))
		self.naytto.blit(teksti, (400, 0))
		teksti = self.fontti.render(f"Elämät: {self.elamat}", True, (255, 0, 0))
		self.naytto.blit(teksti, (150, 0))
 
		self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
		for kolikko in self.kolikot:
			self.naytto.blit(kolikko.kuva, (kolikko.x, kolikko.y))
		for hirvio in self.hirviot:
			self.naytto.blit(hirvio.kuva, (hirvio.x, hirvio.y))
 
		if self.peli_lapi():
			teksti = self.fontti.render("Onnittelut, läpäisit pelin!", True, (255, 0, 0))
			teksti_x = 320 - teksti.get_width() / 2
			teksti_y = 240 - teksti.get_height() / 2
			pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
			self.naytto.blit(teksti, (teksti_x, teksti_y))
 
			uusi_teksti = self.fontti.render("F2 = uusi peli", True, (255, 0, 0))
			uusi_teksti_x = 320 - uusi_teksti.get_width() / 2
			uusi_teksti_y = 240 - uusi_teksti.get_height() / 2 + teksti.get_height()
			pygame.draw.rect(self.naytto, (0, 0, 0), (uusi_teksti_x, uusi_teksti_y, uusi_teksti.get_width(), uusi_teksti.get_height()))
			self.naytto.blit(uusi_teksti, (uusi_teksti_x, uusi_teksti_y))
 
			esc_teksti = self.fontti.render("Esc = sulje peli", True, (255, 0, 0))
			esc_teksti_x = 320 - esc_teksti.get_width() / 2
			esc_teksti_y = 240 + esc_teksti.get_height() / 2 + teksti.get_height()
			pygame.draw.rect(self.naytto, (0, 0, 0), (esc_teksti_x, esc_teksti_y, esc_teksti.get_width(), esc_teksti.get_height()))
			self.naytto.blit(esc_teksti, (esc_teksti_x, esc_teksti_y))
 
		if self.peli_ohi():
			teksti = self.fontti.render("Peli päättyi", True, (255, 0, 0))
			teksti_x = 320 - teksti.get_width() / 2
			teksti_y = 240 - teksti.get_height() / 2
			pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
			self.naytto.blit(teksti, (teksti_x, teksti_y))
 
			uusi_teksti = self.fontti.render("F2 = uusi peli", True, (255, 0, 0))
			uusi_teksti_x = 320 - uusi_teksti.get_width() / 2
			uusi_teksti_y = 240 - uusi_teksti.get_height() / 2 + teksti.get_height()
			pygame.draw.rect(self.naytto, (0, 0, 0), (uusi_teksti_x, uusi_teksti_y, uusi_teksti.get_width(), uusi_teksti.get_height()))
			self.naytto.blit(uusi_teksti, (uusi_teksti_x, uusi_teksti_y))
 
			esc_teksti = self.fontti.render("Esc = sulje peli", True, (255, 0, 0))
			esc_teksti_x = 320 - esc_teksti.get_width() / 2
			esc_teksti_y = 240 + esc_teksti.get_height() / 2 + teksti.get_height()
			pygame.draw.rect(self.naytto, (0, 0, 0), (esc_teksti_x, esc_teksti_y, esc_teksti.get_width(), esc_teksti.get_height()))
			self.naytto.blit(esc_teksti, (esc_teksti_x, esc_teksti_y))
		
 
		pygame.display.flip()
		self.kello.tick(60)
 
	def peli_lapi(self):
		if self.pisteet == 10: 
			return True
	
	def peli_ohi(self):
		if self.elamat == 0:
			return True
 
if __name__ == "__main__":
	Kolikkopeli()