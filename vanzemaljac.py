import pygame

from pygame.sprite import Sprite

class Vanzemaljac(Sprite):
    """Klasa koja predstavlja vanzemaljca"""
    def __init__(self,ai_podesavanje,ekran):
        super().__init__()
        self.ekran=ekran
        self.ai_podesavanje=ai_podesavanje

        #dodaj sliku vanzemaljca
        self.image=pygame.image.load('slike/ufo.png')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.width
        
        self.x=float(self.rect.x)

    def blitvanzemaljca(self):
        """Nacrtaj vanzemaljca na njegovoj lokaciji"""
        self.ekran.blit(self.image,self.rect)

    def proveri_ivice(self):
        """Vrati True ako je vanzemaljac na ivici ekrana"""
        ekran_rect=self.ekran.get_rect()
        if self.rect.right>=ekran_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        """Pomeri vanzemaljca desno"""
        self.x+=(self.ai_podesavanje.brzina_kretanja_vanzemaljaca*
                self.ai_podesavanje.pravac_flote)
        self.rect.x=self.x