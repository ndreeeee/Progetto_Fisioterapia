from controller.gestore_dati import GestoreDati

class GestorePaziente():
    def __init__(self):
        self.lista_esercizi_assegnati = []
        self.cartella_clinica = None
        
    def get_esercizi_assegnati(self, paziente):
        self.lista_esercizi_assegnati
        
        # Filtra gli esercizi assegnati per l'ID del paziente
        esercizi_filtrati = [
            esercizio for esercizio in self.lista_esercizi_assegnati
            if esercizio.get_paziente().get_id() == paziente.get_id()  # Confronta gli ID
        ]
        return esercizi_filtrati
        
    def aggiungi_nuovo_esercizio(self, esercizio):
        pass
    
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
            
            
    def aggiorna_stato_esercizio(self, esercizio, stato):
        for esercizio_assegnato in self.lista_esercizi_assegnati:
            if esercizio == esercizio_assegnato:
                if stato == 1:
                    esercizio_assegnato.set_stato("completato")
                    GestoreDati().aggiorna_stato("completato")
                elif stato == 0:
                    esercizio_assegnato.set_stato("incompleto")
                    GestoreDati().aggiorna_stato("incompleto")
        