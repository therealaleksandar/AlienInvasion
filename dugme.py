import pygame.font

class Dugme:

    def __init__(self,ai_podesavanja,ekran,poruka):
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()

        #Postavi dimenzije i funkcije dugmeta
        self.sirina,self.visina=200,50
        self.boja_dugmeta=(0,250,0)
        self.boja_teksta=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #Napravi dugme rect i centriraj ga
        self.rect=pygame.Rect(0,0,self.sirina,self.visina)
        self.rect.center=self.ekran_rect.center

        #slika invazija vanzemaljaca
        self.iv_slika=pygame.image.load('slike/iv.png')
        self.iv_rect=self.iv_slika.get_rect()
        self.iv_rect.centerx=self.ekran_rect.centerx
        self.iv_rect.top=100

        #Priprema poruke na dugmetu
        self.prip_poruka(poruka)

    def prip_poruka(self,poruka):
        """Pretvara poruku u renderovanu sliku i centrira tekst na dugmetu"""
        self.poruka_slika=self.font.render(poruka,True,self.boja_teksta,self.boja_dugmeta)
        self.poruka_slika_rect=self.poruka_slika.get_rect()
        self.poruka_slika_rect.center=self.rect.center

    def nacrtaj_dugme(self):
        #Nacrtaj prazno dugme i dodaj poruku
        self.ekran.fill(self.boja_dugmeta,self.rect)
        self.ekran.blit(self.poruka_slika,self.poruka_slika_rect)
        self.ekran.blit(self.iv_slika,self.iv_rect)