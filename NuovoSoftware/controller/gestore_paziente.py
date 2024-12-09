from controller.gestore_dati import GestoreDati

class GestorePaziente():
    def __init__(self):
        self.lista_esercizi_assegnati = []
        self.cartella_clinica = None
        self.prenotazioni = []
        
    
    
                
    def elimina_prenotazione (self, prenotazione1):
        for prenotazione in self.prenotazioni:
            if prenotazione == prenotazione1:
                prenotazione.set_stato("disponibile")
                GestoreDati().elimina_prenotazione(prenotazione)

        
    
    def get_prenotazioni(self, id):
        self.prenotazioni = GestoreDati().get_prenotazioni_per_paziente(id)
        return self.prenotazioni
    
        
    def get_esercizi_assegnati(self, paziente):
        self.lista_esercizi_assegnati
        
        esercizi_filtrati = [
            esercizio for esercizio in self.lista_esercizi_assegnati
            if esercizio.get_paziente().get_id() == paziente.get_id()  
        ]
        return esercizi_filtrati
    
    def set_esercizi_assegnati(self, lista_esercizi):
        self.lista_esercizi_assegnati = lista_esercizi
    
    def set_cartella(self, cartella):
        self.cartella_clinica = cartella
        
    def get_cartella(self):
        return self.cartella_clinica
    
    def get_esercizio(self, titolo):
        for esercizio in self.lista_esercizi_assegnati:
            if esercizio.get_titolo() == titolo:
                return esercizio
            
    def aggiorna_stato_esercizio(self, paziente, esercizio, stato_var):
        stato = "completato" if stato_var.get() == 1 else "incompleto"
        
        for esercizio_assegnato in self.lista_esercizi_assegnati:
            if esercizio == esercizio_assegnato:
                esercizio_assegnato.set_stato(stato)
                GestoreDati().aggiorna_stato(paziente, esercizio, stato)
                
    def get_fisioterapista(self):
        return GestoreDati().get_fisioterapista()
                
 
        