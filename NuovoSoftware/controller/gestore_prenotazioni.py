from datetime import datetime, timedelta
from model.prenotazione import Prenotazione
from controller.gestore_dati import GestoreDati


class GestorePrenotazioni:
    def __init__(self):
        self.prenotazioni = GestoreDati().carica_prenotazioni()
        self.aggiorna_prenotazioni_future(giorni_in_avanti=7)
        self.elimina_prenotazioni_scadute()
       

    
    
    def prenota(self, prenotazione1):
        for prenotazione in self.prenotazioni:
            if prenotazione == prenotazione1:
                prenotazione.set_stato("prenotato")
                GestoreDati().prenota(prenotazione)
    
    
    def get_prenotazioni(self):
        return self.prenotazioni 

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

            nuove_prenotazioni = []  # Lista per salvare le nuove prenotazioni

            while ultima_data < data_limite:
                ultima_data += timedelta(days=1)
                # Esclude sabato e domenica
                if ultima_data.weekday() in [5, 6]:
                    continue
                nuove_prenotazioni.extend(self.riempi_prenotazioni_iniziali(ultima_data.date(), '09:00', '18:00'))

            # Salva le nuove prenotazioni nel database
            if nuove_prenotazioni:
                GestoreDati().salva_prenotazioni(nuove_prenotazioni)

    def riempi_prenotazioni_iniziali(self, data, orario_inizio, orario_fine):
        ora_inizio = datetime.strptime(orario_inizio, "%H:%M").time()
        ora_fine = datetime.strptime(orario_fine, "%H:%M").time()
        orario_corrente = datetime.combine(data, ora_inizio)

        nuove_prenotazioni = []  # Lista di nuove prenotazioni

        while orario_corrente.time() <= ora_fine:
            data_ora = orario_corrente.strftime('%Y-%m-%d %H:%M')
            nuova_prenotazione = Prenotazione(data_ora)
            self.prenotazioni.append(nuova_prenotazione)
            nuove_prenotazioni.append(nuova_prenotazione)
            orario_corrente += timedelta(hours=1)

        return nuove_prenotazioni


    def cancella_prenotazioni(self):
        self.prenotazioni.clear()
        
    def get_prenotazioni_disponibili(self):
        prenotazioni_disponibili = []
        for prenotazione in self.prenotazioni:
            if prenotazione.get_stato() == "disponibile":
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
        prenotazioni_da_rimuovere = [
                p for p in self.prenotazioni
                if datetime.strptime(p.data_e_ora, '%Y-%m-%d %H:%M') < ora_attuale
            ]
        
        for p in prenotazioni_da_rimuovere:
            self.prenotazioni.remove(p)