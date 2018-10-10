import pygame
from pygame.sprite import Sprite

class Metak(Sprite):
    """Klasa koja predstavlja metak koji ispaljujemo iz broda"""
    def __init__(self,ai_podesavanja,ekran,sv_brod):
        super(Metak,self).__init__()
        self.ekran=ekran

        #Kreiranje metka na poziciji (0,0) i onda postavljanja na pravu poziciju
        self.rect=pygame.Rect(0,0,ai_podesavanja.sirina_metka,ai_podesavanja.duzina_metka)
        self.rect.centerx=sv_brod.rect.centerx
        self.rect.top=sv_brod.rect.top

        #postavi poziciju metka kao decimalnu vrednost
        self.y=float(self.rect.y)

        self.boja=ai_podesavanja.boja_metka
        self.brzina=ai_podesavanja.brzina_metka
    
    def update(self):
        """Pomeranje metka po ekranu"""
        #azuriranje decimalne pozicije metka
        self.y-=self.brzina
        
        #azuriranje rect pozicije
        self.rect.y=self.y

    def nacrtaj_metak(self):
        """Crtanje metka na ekranu"""
        pygame.draw.rect(self.ekran,self.boja,self.rect)

