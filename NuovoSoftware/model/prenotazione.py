class Prenotazione:
    def __init__(self, codice, paziente, data_e_ora):
        
        self.codice = codice
        self.paziente = paziente
        self.data_e_ora = data_e_ora
        self.stato = "disponibile"