from model.utente import Utente
import pickle
import os






class Paziente(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.esercizi_assegnati = []
        self.prenotazioni = []
        self.cartella_clinica = None
    
  
    def set_cartella_clinica(self,cartella):
        self.cartella_clinica = cartella
        
    def get_cartella_clinica(self):
        return self.cartella_clinica.descrizione
    
    def set_credenziali(self, nome, email, password):
        self.nome = nome
        self.password = password
        self.email = email
        
    def get_esercizi(self):
        return self.esercizi_assegnati
    
    def add_esercizio(self, esercizio, file_path='data/utenti.pkl'):
        self.esercizi_assegnati.append(esercizio)
        self._salva_modifiche_pickle(file_path)
    
    def remove_esercizio(self, esercizio, file_path='data/utenti.pkl'):
        self.esercizi_assegnati.remove(esercizio)
        self._salva_modifiche_pickle(file_path)

        
    def prenota (self, prenotazione, file_path='data/utenti.pkl'):
        prenotazione.stato = "prenotato"
        self.prenotazioni.append(prenotazione)
        self._salva_modifiche_pickle(file_path)

    
    def elimina_prenotazione (self, prenotazione, file_path='data/utenti.pkl'):
        if prenotazione in self.prenotazioni:
            prenotazione.stato = "disponibile"
            self.prenotazioni.remove(prenotazione)
            self._salva_modifiche_pickle(file_path)
    
    def get_prenotazioni(self):
        return self.prenotazioni
    
    
    
    def __del__(self):
        print(f"Paziente {self.nome} eliminato")
        
    def _salva_modifiche_pickle(self, file_path='data/utenti.pkl'):
        try:
            # Carica tutti gli utenti dal file pickle
            lista_utenti = []
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    lista_utenti = pickle.load(file)

            # Cerca l'utente corrente nella lista e aggiorna i suoi dati
            for idx, utente in enumerate(lista_utenti):
                if isinstance(utente, Paziente) and utente.email == self.email:
                    lista_utenti[idx] = self  # Aggiorna i dati di questo utente

            # Salva la lista aggiornata nel file pickle
            with open(file_path, 'wb') as file:
                pickle.dump(lista_utenti, file)
                print("Modifiche salvate correttamente nel file pickle.")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
        
    