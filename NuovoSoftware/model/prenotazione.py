class Prenotazione:
    
    _id_counter = 1 
    def __init__(self, data_e_ora, paziente = None):
        
        self.codice = Prenotazione._id_counter
        Prenotazione._id_counter += 1
        self.paziente = paziente
        self.data_e_ora = data_e_ora
        self.stato = "disponibile"
        
        
    def aggiungi_prenotazione (self,paziente):
        self.paziente = paziente
        self.stato = "prenotato"
        
    
        
        
