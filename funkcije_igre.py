import sys

import pygame

from metak import Metak
from vanzemaljac import Vanzemaljac
from time import sleep

def prati_dogadjaje(sv_brod,ai_podesavanja,ekran,metci,stats,igraj_dugme,vanzemaljci,rez):
    #Posmatraj aktivnosti misa i tastature
    for dogadjaj in pygame.event.get():
        if dogadjaj.type==pygame.QUIT:
            sys.exit(0)
        elif dogadjaj.type==pygame.KEYDOWN:
            pritisnuto_dugme(sv_brod,dogadjaj,ai_podesavanja,ekran,metci,stats,vanzemaljci,rez)
        elif dogadjaj.type==pygame.KEYUP:
            podignuto_dugme(sv_brod,dogadjaj)
        elif dogadjaj.type==pygame.MOUSEBUTTONDOWN:
            mis_x,mix_y=pygame.mouse.get_pos()
            proveri_igraj_dugme(ai_podesavanja,ekran,sv_brod,vanzemaljci,metci,stats,igraj_dugme,mis_x,mix_y,rez)

def proveri_igraj_dugme(ai_podesavanja,ekran,sv_brod,vanzemaljci,metci,stats,igraj_dugme,mis_x,mis_y,rez):
    """Pocni novu igru kada igrac stisne 'Pocni igru'"""
    dugme_igraj_pritisnuto=igraj_dugme.rect.collidepoint(mis_x,mis_y)
    if dugme_igraj_pritisnuto and not stats.aktivna_igra:
        pocni_igru(ai_podesavanja,ekran,stats,vanzemaljci,metci,sv_brod,rez)

        #Resetuj podesavanja igre
        ai_podesavanja.inicijalizovati_dinamicka_podesavanja()

def pocni_igru(ai_podesavanja,ekran,stats,vanzemaljci,metci,sv_brod,rez):
    #Sakrij kursor misa
    pygame.mouse.set_visible(False)

    #Resetuj statistiku igre
    stats.resetuj_statistiku()
    stats.aktivna_igra=True

    #Resetuj rezultate
    rez.pripremi_rezultate()
    rez.pripremi_najbolji_rez()
    rez.pripremi_nivo()
    rez.pripremi_brod()

    #Isprazni listu vanzemaljaca i metkova
    vanzemaljci.empty()
    metci.empty()

    #Napravi novu flotu i centriraj brod
    napravi_flotu(ai_podesavanja,ekran,vanzemaljci,sv_brod)
    sv_brod.centriraj_brod()

def pritisnuto_dugme(sv_brod,dogadjaj,ai_podesavanja,ekran,metci,stats,vanzemaljci,rez):
    #funkcija za pritisnuto dugme na tastaturi
    if dogadjaj.key==pygame.K_RIGHT:
        sv_brod.pomeranje_desno=True
    elif dogadjaj.key==pygame.K_LEFT:
        sv_brod.pomeranje_levo=True
    elif dogadjaj.key==pygame.K_SPACE:
        ispaljivanje_metaka(metci,ai_podesavanja,ekran,sv_brod)
    elif dogadjaj.key==pygame.K_q:
        sys.exit(0)
    elif dogadjaj.key==pygame.K_p:
        if not stats.aktivna_igra:
            pocni_igru(ai_podesavanja,ekran,stats,vanzemaljci,metci,sv_brod,rez)

def podignuto_dugme(sv_brod,dogadjaj):
    #funkcija za podigunto dugme na tastaturi
    if dogadjaj.key==pygame.K_RIGHT:
        sv_brod.pomeranje_desno=False
    elif dogadjaj.key==pygame.K_LEFT:
        sv_brod.pomeranje_levo=False

def ispaljivanje_metaka(metci,ai_podesavanja,ekran,sv_brod):
    if len(metci)<ai_podesavanja.dozvoljeni_broj_metaka:
        novi_metak=Metak(ai_podesavanja,ekran,sv_brod)
        metci.add(novi_metak)

def azuriraj_metke(metci,vanzemaljci,ai_podesavanja,ekran,sv_brod,stats,rez):
    """Azuriranje pozicije metaka i brisanje starih"""
    metci.update()
    for metak in metci.copy():
        if metak.rect.bottom<=0:
            metci.remove(metak)
    
    proveri_sudar_metka_vanzemaljca(metci,vanzemaljci,ai_podesavanja,ekran,sv_brod,stats,rez)

def proveri_sudar_metka_vanzemaljca(metci,vanzemaljci,ai_podesavanja,ekran,sv_brod,stats,rez):
    #Proveri da li je metak udario vanzemaljca
    #ako jeste, ukloni metak i vanzemaljca
    sudari=pygame.sprite.groupcollide(metci,vanzemaljci,True,True)
    if sudari:
        for vanzemaljci in sudari.values():
            stats.rezultat+=ai_podesavanja.vanzemaljci_poeni*len(vanzemaljci)
            rez.pripremi_rezultate()
        proveri_najbolji_rez(stats,rez)

    if len(vanzemaljci)==0:
        #unisti postojece metke, ubrzaj igru i kreiraj novu flotu
        metci.empty()
        ai_podesavanja.povecaj_brzinu()
        napravi_flotu(ai_podesavanja,ekran,vanzemaljci,sv_brod)

        #Povecaj nivo
        stats.nivo+=1
        rez.pripremi_nivo()

def dobij_broj_redova(ai_podesavanja,visina_broda,visina_vanzemaljca):
    """Dobijanje broja redova vanzemaljaca koji mogu stati na ekran"""
    dostupna_mesta_y=(ai_podesavanja.ekran_duzina-(6*visina_vanzemaljca)-visina_broda)
    broj_redova=int(dostupna_mesta_y/(5*visina_vanzemaljca))
    return broj_redova

def napravi_vanzemaljca(ai_podesavanja,ekran,broj_vanzemaljaca,broj_reda,vanzemaljci):
    #kreiraj vanzemaljca i stavi ga u red
    vanzemaljac=Vanzemaljac(ai_podesavanja,ekran)
    sirina_vanzemaljca=vanzemaljac.rect.width
    visina_vanzemaljca=vanzemaljac.rect.height
    vanzemaljac.x=sirina_vanzemaljca+2*sirina_vanzemaljca*broj_vanzemaljaca
    vanzemaljac.rect.x=vanzemaljac.x
    vanzemaljac.rect.y=5*visina_vanzemaljca+3*visina_vanzemaljca*broj_reda
    vanzemaljci.add(vanzemaljac)

def dobij_broj_vanzemaljaca_x(ai_podesavanja,sirina_vanzemaljca):
    dostupna_mesta_x=ai_podesavanja.ekran_sirina-2*sirina_vanzemaljca
    broj_vanzemaljaca_x=int(dostupna_mesta_x/(2*sirina_vanzemaljca))
    return broj_vanzemaljaca_x

def napravi_flotu(ai_podesavanja,ekran,vanzemaljci,sv_brod):
    """Napravi flotu vanzemaljaca"""
    #napravi vanzemaljca i pronadji broj vanzemaljaca u redu
    #razmak izmedju svakog vanzemaljca je jednak sirini jednog vanzemaljca
    vanzemaljac=Vanzemaljac(ai_podesavanja,ekran)
    broj_vanzemaljaca_x=dobij_broj_vanzemaljaca_x(ai_podesavanja,vanzemaljac.rect.width)
    broj_redova=dobij_broj_redova(ai_podesavanja,sv_brod.rect.height,vanzemaljac.rect.height)

    #kreiraj flotu vanzemaljaca
    for broj_reda in range(broj_redova):
        for broj_vanzemaljaca in range(broj_vanzemaljaca_x):
            #kreiraj vanzemaljca i stavi ga u red
            napravi_vanzemaljca(ai_podesavanja,ekran,broj_vanzemaljaca,broj_reda,vanzemaljci)

def proveri_ivicu_flote(ai_podesavanja,vanzemaljci):
    """Proveri da li je flota na ivici ekrana i reaguj"""
    for vanzemaljac in vanzemaljci.sprites():
        if vanzemaljac.proveri_ivice():
            promeni_pravac_flote(ai_podesavanja,vanzemaljci)
            break

def promeni_pravac_flote(ai_podesavanja,vanzemaljci):
    """Spusti flotu i promeni pravac kretanja"""
    for vanzemaljac in vanzemaljci.sprites():
        vanzemaljac.rect.y+=ai_podesavanja.brzina_spustanja_vanzemaljaca
    ai_podesavanja.pravac_flote*=-1

def sudar_broda(ai_podesavanja,stats,ekran,sv_brod,vanzemaljci,metci,rez):
    """Odgovara na sudar broda sa vanzemaljcem"""
    if stats.preostali_brodovi>0:
        #Smanjuje preostale brodove
        stats.preostali_brodovi-=1

        #Azuriraj rezultate
        rez.pripremi_brod()

        #Prazni listu brodova i metaka
        vanzemaljci.empty()
        metci.empty()

        #Pravi novu flotu i centrira sv. brod
        napravi_flotu(ai_podesavanja,ekran,vanzemaljci,sv_brod)
        sv_brod.centriraj_brod()

        #pauza
        sleep(0.6)
    else:
        stats.aktivna_igra=False
        pygame.mouse.set_visible(True)

def proveri_vanzemaljce_dno(ai_podesavanja,stats,ekran,sv_brod,vanzemaljci,metci,rez):
    """Proverava da li su vanzemaljci dosli do dna ekrana"""
    ekran_rect=ekran.get_rect()
    for vanzemaljac in vanzemaljci.sprites():
        if vanzemaljac.rect.bottom>=ekran_rect.bottom:
            #Tretiraj ovo isto kao i da je vanzemaljac udario sv brod
            sudar_broda(ai_podesavanja,stats,ekran,sv_brod,vanzemaljci,metci,rez)
            break

def azuriraj_vanzemaljce(ai_podesavanja,vanzemaljci,sv_brod,stats,ekran,metci,rez):
    """Proveri da li je flota na ivici i azuriraj poziciju vanzemaljaca u floti"""
    proveri_ivicu_flote(ai_podesavanja,vanzemaljci)
    vanzemaljci.update()

    #Prati sudar vanzemaljca i broda
    if pygame.sprite.spritecollideany(sv_brod,vanzemaljci):
        sudar_broda(ai_podesavanja,stats,ekran,sv_brod,vanzemaljci,metci,rez)

    #Prati da li su vanzemaljci dosli do dna ekrana
    proveri_vanzemaljce_dno(ai_podesavanja,stats,ekran,sv_brod,vanzemaljci,metci,rez)

def proveri_najbolji_rez(stats,rez):
    """Proveri da li postoji novi najbolji rezultat"""
    if stats.rezultat>stats.najbolji_rezultat:
        stats.najbolji_rezultat=stats.rezultat
        rez.pripremi_najbolji_rez()

def azuriraj_ekran(pozadina,ekran,sv_brod,metci,vanzemaljci,stats,igraj_dugme,rez):
    #postavljanje slike pozadine ekrana
    pozadina.blitpozadina()

    #Precrtaj sve metke iza broda i vanzemaljaca
    for metak in metci.sprites():
        metak.nacrtaj_metak()

    #postavljanje broda u prvobitnu poziciju
    sv_brod.blitbrod()

    #postavljanje vanzemaljca u prvobitnu poziciju
    vanzemaljci.draw(ekran)

    rez.prikazi_rezultate()

    #Nacrtaj dugme ako je igra neaktivna
    if not stats.aktivna_igra:
        igraj_dugme.nacrtaj_dugme()

    #refresh ekrana
    pygame.display.flip()


        
