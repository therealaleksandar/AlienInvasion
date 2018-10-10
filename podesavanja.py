class Podesavanje:
    """Klasa podesavanje za postavljanje boje i velicine ekrana"""
    def __init__(self):
        #Podesavanje ekrana
        self.ekran_sirina=1200
        self.ekran_duzina=800
        self.boja_pozadine=(255,255,255)

        #podesavanje sv_broda
        self.limit_brodova=3

        #podesavanje metka
        self.sirina_metka=4
        self.duzina_metka=10
        self.boja_metka=0,0,0
        self.dozvoljeni_broj_metaka=6

        #podesavanje vanzemaljca
        self.brzina_spustanja_vanzemaljaca=15

        #koliko ubrzava igra
        self.razmera_ubrzanja=1.1
        #Koliko se ubrzava vrednost ubijenog vanzemaljca
        self.razmera_rezultata=1.5

        self.inicijalizovati_dinamicka_podesavanja()

    def inicijalizovati_dinamicka_podesavanja(self):
        """Inicijalizacija podesavanja koja se menjaju tokom igre"""
        self.sv_brod_brzina=1.5
        self.brzina_metka=3
        self.brzina_kretanja_vanzemaljaca=1

        #prava_flote 1 predstavlja desno, -1 predstavlja levo
        self.pravac_flote=1

        self.vanzemaljci_poeni=50

    def povecaj_brzinu(self):
        """Povecava brzinu igre i vrednosti poena"""
        self.sv_brod_brzina*=self.razmera_ubrzanja
        self.brzina_metka*=self.razmera_ubrzanja
        self.brzina_kretanja_vanzemaljaca*=self.razmera_ubrzanja

        self.vanzemaljci_poeni=int(self.vanzemaljci_poeni*self.razmera_rezultata)
