from datetime import datetime, timedelta


class Prenotazione:
    
    _id_counter = 1 
    def __init__(self, data_e_ora):
        
        self.codice = Prenotazione._id_counter
        Prenotazione._id_counter += 1
        self.paziente = None
        self.data_e_ora = data_e_ora
        self.stato = "disponibile"
        
        
    def aggiungi_prenotazione (self,paziente):
        self.paziente = paziente
        self.stato = "prenotato"
        
    
        
        
class GestorePrenotazioni:
    def __init__(self):
        self.prenotazioni = []
        self.settimana_corrente = None 
        self.aggiorna_prenotazioni_future(giorni_in_avanti=7)
       


    def aggiorna_prenotazioni_future(self, giorni_in_avanti=7):
        
        if self.prenotazioni:
            ultima_data = max(p.data_e_ora for p in self.prenotazioni)
        else:
            ultima_data = None
            
        if ultima_data is None:
            ultima_data = datetime.now()
        else:
            ultima_data = datetime.strptime(ultima_data, '%Y-%m-%d %H:%M')

        # Determina la data limite per le nuove prenotazioni
        data_limite = datetime.now() + timedelta(days=giorni_in_avanti)

        while ultima_data < data_limite:
            ultima_data += timedelta(days=1)
            # per togliere sabato e domenica
            if ultima_data.weekday() in [5, 6]:
                continue
            self.riempi_prenotazioni_iniziali(ultima_data.date(), '09:00', '18:00')
            
            
    def riempi_prenotazioni_iniziali(self, data, orario_inizio, orario_fine):
        
        ora_inizio = datetime.strptime(orario_inizio, "%H:%M").time()
        ora_fine = datetime.strptime(orario_fine, "%H:%M").time()
        orario_corrente = datetime.combine(data, ora_inizio)

        while orario_corrente.time() <= ora_fine:
            data_ora = orario_corrente.strftime('%Y-%m-%d %H:%M')
            nuova_prenotazione = Prenotazione (data_ora)
            self.prenotazioni.append(nuova_prenotazione)
            orario_corrente += timedelta(hours=1)


    def cancella_prenotazioni(self):
        self.prenotazioni.clear()
        
    def get_prenotazioni_disponibili(self):
        prenotazioni_disponibili = []
        for prenotazione in self.prenotazioni:
            if prenotazione.stato == "disponibile":
                prenotazioni_disponibili.append(prenotazione)
        
        return prenotazioni_disponibili
    
    def get_posti_prenotati(self):
        posti_prenotati = []
        for prenotazione in self.prenotazioni:
            if prenotazione.stato == "prenotato":
                posti_prenotati.append(prenotazione)
        
        return posti_prenotati
    
    def elimina_prenotazioni_scadute(self):
     
        ora_attuale = datetime.now()
        prenotazioni_da_rimuovere = [p for p in self.prenotazioni if p.data_e_ora < ora_attuale]

        # Rimuove le prenotazioni scadute dalla lista
        for p in prenotazioni_da_rimuovere:
            self.prenotazioni.remove(p)