import pygame

from pygame.sprite import Sprite

class SvemirskiBrod(Sprite):
    """Klasa za svemirski brod"""
    def __init__(self,ai_podesavanje,ekran):
        super().__init__()
        self.ekran=ekran
        self.ai_podesavanje=ai_podesavanje

        #Ubacivanje slike broda
        self.image=pygame.image.load('slike/sv_brod.png')
        self.rect=self.image.get_rect()
        self.ekran_rect=ekran.get_rect()

        #Svaki novi brod postavi na sredinu donjeg dela ekrana
        self.rect.centerx=self.ekran_rect.centerx
        self.rect.bottom=self.ekran_rect.bottom

        self.center=float(self.rect.centerx)

        #Zastavize za pomeranje
        self.pomeranje_desno=False
        self.pomeranje_levo=False
        self.pomeranje_gore=False
        self.pomeranje_dole=False

    def blitbrod(self):
        """Nacrtaj brod na njegovoj trenutnoj lokaciji"""
        self.ekran.blit(self.image,self.rect)

    def azuriraj(self):
        """Azurira pomeranje sv. broda"""
        if self.pomeranje_desno and self.rect.right<self.ekran_rect.right:
            self.center+=self.ai_podesavanje.sv_brod_brzina
        if self.pomeranje_levo and self.rect.left>self.ekran_rect.left:
            self.center-=self.ai_podesavanje.sv_brod_brzina
        if self.pomeranje_gore and self.rect.top>self.ekran_rect.top:
            self.rect.top-=self.ai_podesavanje.sv_brod_brzina
        if self.pomeranje_dole and self.rect.bottom<self.ekran_rect.bottom:
            self.rect.top+=self.ai_podesavanje.sv_brod_brzina

        self.rect.centerx=self.center

    def centriraj_brod(self) :
        """Centrira brod na sredinu ekrana"""
        self.center=self.ekran_rect.centerx

        