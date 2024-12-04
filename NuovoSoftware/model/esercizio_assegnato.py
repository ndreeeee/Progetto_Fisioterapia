from model.esercizio import Esercizio

class EsercizioAssegnato(Esercizio):
    def __init__(self, titolo, descrizione, video):
        super().__init__(titolo, descrizione, video)
        self.paziente = None
        self.esercizio = Esercizio
        self.stato = "incompleto"
        
    def set_stato(self, stato):
        self.stato = stato
        
    def get_stato(self):
        return self.stato
    
    def set_paziente(self, paziente):
        self.paziente = paziente
        
    def get_paziente(self):
        return self.paziente
    
    def get_esercizio(self):
        return self.esercizio
    