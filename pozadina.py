import pygame

class Pozadina:
    """Klasa za svemirski brod"""
    def __init__(self,ekran):
        self.ekran=ekran

        #ubacivanje slike pozadine
        self.pozadina=pygame.image.load('slike/pozadina.jpg')
        

    def blitpozadina(self):
        """Postavi pozadinu na gornji levi ugao ekrana"""
        self.ekran.blit(self.pozadina,(0,0))
