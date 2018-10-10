import pygame.font

from pygame.sprite import Group
from svemirski_brod import SvemirskiBrod

class Rezultati:
    """Klasa koja sluzi za prikazivanje rezultata"""

    def __init__(self,ai_podesavanja,ekran,stats):
        self.ekran=ekran
        self.ekran_rect=self.ekran.get_rect()
        self.ai_podesavanja=ai_podesavanja
        self.stats=stats

        #Podesavanje fonta
        self.boja_teksta=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        #Pripremi sliku rezultata
        self.pripremi_rezultate()
        self.pripremi_najbolji_rez()
        self.pripremi_nivo()
        self.pripremi_brod()

    def pripremi_rezultate(self):
        """Pretvaranje rezultata u sliku"""
        zaokruzen_rezultat=int(round(self.stats.rezultat,-1))
        rezultat_str="{:,}".format(zaokruzen_rezultat)
        self.rezultat_slika=self.font.render(rezultat_str,True,self.boja_teksta,self.ai_podesavanja.boja_pozadine)

        #Prikazi rezultat na desnom vrhu ekrana
        self.rezultat_rect=self.rezultat_slika.get_rect()
        self.rezultat_rect.right=self.ekran_rect.right-20
        self.rezultat_rect.top=20

    def pripremi_najbolji_rez(self):
        """Pretvori najbolji rezultat u sliku"""
        najbolji_rezultat=int(round(self.stats.najbolji_rezultat,-1))
        najbolji_rezultat_str="{:,}".format(najbolji_rezultat)
        self.najbolji_rezultat_slika=self.font.render(najbolji_rezultat_str,True,self.boja_teksta,self.ai_podesavanja.boja_pozadine)

        #Centriraj najbolji rezultat na vrhu ekrana
        self.najbolji_rezultat_rect=self.najbolji_rezultat_slika.get_rect()
        self.najbolji_rezultat_rect.centerx=self.ekran_rect.centerx
        self.najbolji_rezultat_rect.top=20

    def pripremi_nivo(self):
        """Pretvori broj nivoa u sliku"""
        nivo=self.stats.nivo
        self.nivo_slika=self.font.render(str(nivo),True,self.boja_teksta,self.ai_podesavanja.boja_pozadine)

        #Postavi nivo ispod rezultata
        self.nivo_rect=self.nivo_slika.get_rect()
        self.nivo_rect.right=self.ekran_rect.right-20
        self.nivo_rect.top=self.rezultat_rect.bottom+20

    def pripremi_brod(self):
        """Prikazuje koliko je brodova ostalo"""
        self.brodovi=Group()
        for broj_brodova in range(self.stats.preostali_brodovi):
            brod=SvemirskiBrod(self.ai_podesavanja,self.ekran)
            brod.rect.x=10+broj_brodova*brod.rect.width
            brod.rect.y=10
            self.brodovi.add(brod)

    def prikazi_rezultate(self):
        self.ekran.blit(self.rezultat_slika,self.rezultat_rect)
        self.ekran.blit(self.najbolji_rezultat_slika,self.najbolji_rezultat_rect)
        self.ekran.blit(self.nivo_slika,self.nivo_rect)
        self.brodovi.draw(self.ekran)

        