import pygame
import funkcije_igre as fi

from podesavanja import Podesavanje
from svemirski_brod import SvemirskiBrod
from pozadina import Pozadina
from pygame.sprite import Group
from vanzemaljac import Vanzemaljac
from statistika_igre import StatistikaIgre
from dugme import Dugme
from rezultati import Rezultati

def pokreni_igru():
    #Napravi objekat na ekranu
    pygame.init()

    #Napravi podesavanje objekat
    ai_podesavanje=Podesavanje()

    #napravi ekran i postavi rezoluciju
    ekran=pygame.display.set_mode((ai_podesavanje.ekran_sirina,ai_podesavanje.ekran_duzina))
    pygame.display.set_caption('Invazija Vanzemaljaca')

    #Napravi Igraj dugme
    igraj_dugme=Dugme(ai_podesavanje,ekran,"Igraj")

    #Napravi objekat statistike igre
    stats=StatistikaIgre(ai_podesavanje)
    rez=Rezultati(ai_podesavanje,ekran,stats)

    #Napravi pozadinu objekat
    pozadina=Pozadina(ekran)
    
    #Napravi sv. brod objekat
    sv_brod=SvemirskiBrod(ai_podesavanje,ekran)

    #Napravi grupu metaka i grupu vanzemaljaca
    metci=Group()
    vanzemaljci=Group()

    #Napravi flotu vanzemaljaca
    fi.napravi_flotu(ai_podesavanje,ekran,vanzemaljci,sv_brod)

    #Postavljanje glavnog loop-a za igru
    while True:

        #Posmatraj aktivnosti misa i tastature
        fi.prati_dogadjaje(sv_brod,ai_podesavanje,ekran,metci,stats,igraj_dugme,vanzemaljci,rez)

        if stats.aktivna_igra:
            sv_brod.azuriraj()

            fi.azuriraj_metke(metci,vanzemaljci,ai_podesavanje,ekran,sv_brod,stats,rez)

            fi.azuriraj_vanzemaljce(ai_podesavanje,vanzemaljci,sv_brod,stats,ekran,metci,rez)

        #azuriraj ekran
        fi.azuriraj_ekran(pozadina,ekran,sv_brod,metci,vanzemaljci,stats,igraj_dugme,rez)    


pokreni_igru()
