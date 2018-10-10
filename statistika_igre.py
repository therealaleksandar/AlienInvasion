class StatistikaIgre:
    """Prati statistiku za igru"""

    def __init__(self,ai_podesavanja):
        self.ai_podesavanja=ai_podesavanja
        self.resetuj_statistiku()
        
        self.aktivna_igra=False

        #najbolji rezultat ne bi trebalo da se resetuje
        self.najbolji_rezultat=0

    def resetuj_statistiku(self):
        """Podesava statistiku koja moze da se menja tokom igre"""
        self.preostali_brodovi=self.ai_podesavanja.limit_brodova
        self.rezultat=0
        self.nivo=1