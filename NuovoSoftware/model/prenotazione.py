class Prenotazione:
    
    def __init__(self, data_e_ora, paziente = None):
        
        self.id = 0
        self.paziente = paziente
        self.data_e_ora = data_e_ora
        self.stato = "disponibile"
        
    
    def get_data_e_ora(self):
        return self.data_e_ora
    
    def set_data_e_ora(self, data):
        self.data_e_ora = data
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def get_stato(self):
        return self.stato
    
    def set_stato(self, stato):
        self.stato = stato
        
    def get_paziente(self):
        return self.paziente
    
    def set_paziente(self, paziente):
        self.paziente = paziente
    
    def aggiungi_prenotazione (self,paziente):
        self.paziente = paziente
        self.stato = "prenotato"
        
        
    
        
        
