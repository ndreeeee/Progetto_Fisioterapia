import sqlite3
from database import Database


class GestoreDati:
    def __init__ (self):
        self.db = Database()

    
    def get_esercizi(self):
        from model.esercizio import Esercizio
        
        self.db.cursor.execute("SELECT * FROM esercizi")
        rows = self.db.cursor.fetchall()
        
        esercizi = []
        
        for row in rows:
            esercizio = Esercizio (row[1], row[2], row[3])
            esercizi.append(esercizio)
    
        return esercizi
    
    
    def inserisci_esercizio(self, titolo, descrizione, video):
        self.db.cursor.execute('''
                INSERT INTO esercizi (titolo, descrizione, video_url)
                VALUES (?, ?, ?)
            ''', (titolo, descrizione, video))
        self.db.conn.commit()
    
    def ottieni_messaggi(self, fisioterapista, paziente):
        from model.messaggio import Messaggio
        
        
        self.db.cursor.execute("SELECT * FROM messaggi")
        rows = self.db.cursor.fetchall()

        
        messaggi = []
        
        for row in rows:
            
            self.db.cursor.execute('SELECT * FROM utenti WHERE id=?', (row[2],))  # destinatario_id
            destinatario = self.db.cursor.fetchone()
             
            if destinatario[4] == 'fisioterapista':
                messaggio = Messaggio(row[3], fisioterapista, paziente, row[4])  
                messaggi.append(messaggio)            
            else:
                messaggio = Messaggio(row[3], paziente, fisioterapista, row[4])  
                messaggi.append(messaggio)     
                
             
          
            

        
            # Filtra i messaggi rilevanti tra fisioterapista e paziente
        messaggi_filtrati = [
            m for m in messaggi
            if (m.mittente == fisioterapista and m.destinatario == paziente) or
            (m.mittente == paziente and m.destinatario == fisioterapista)
        ]

        return messaggi_filtrati

        
    def salva_messaggio(self, mittente, destinatario, testo):
        self.db.cursor.execute('''
                INSERT INTO messaggi (mittente_id, destinatario_id, messaggio)
                VALUES (?, ?, ?)
            ''', (mittente, destinatario, testo))
        self.db.conn.commit()

        
    def aggiungi_utente(self, nome, email, password, tipo):
       
        try:
            # Controllo validità del tipo
            if tipo not in ('fisioterapista', 'paziente'):
                raise ValueError("Tipo utente non valido. Deve essere 'fisioterapista' o 'paziente'.")
            
            # Inserimento nel database
            self.db.cursor.execute('''
                INSERT INTO utenti (nome, email, password, tipo)
                VALUES (?, ?, ?, ?)
            ''', (nome, email, password, tipo))
            self.db.conn.commit()
            print(f"Utente {nome} aggiunto con successo come {tipo}.")
        except sqlite3.IntegrityError as e:
            print(f"Errore: L'email '{email}' è già utilizzata.")
        except ValueError as ve:
            print(f"Errore: {ve}")
        except sqlite3.Error as e:
            print(f"Errore durante l'aggiunta dell'utente: {e}")
            
    def carica_utenti(self):
        from model.fisioterapista import Fisioterapista
        from model.paziente import Paziente
        self.db.cursor.execute("SELECT * FROM utenti")
        rows = self.db.cursor.fetchall()
        utenti = []

        for row in rows:
            # Crea l'oggetto utente in base al tipo
            if row[4] == 'fisioterapista':
                utente = Fisioterapista(row[1], row[2], row[3])
            elif row[4] == 'paziente':
                utente = Paziente(row[1], row[2], row[3])
                
            utente.set_id(row[0])
            utenti.append(utente)
        
        
        return utenti
    
    def carica_pazienti(self):
        from model.paziente import Paziente
        from model.cartella_clinica import CartellaClinica

        # Query per ottenere i pazienti e le loro cartelle cliniche
        query = '''
            SELECT 
                utenti.id AS paziente_id,
                utenti.nome,
                utenti.email,
                utenti.password,
                cartella_clinica.descrizione AS descrizione_cartella
            FROM utenti
            LEFT JOIN cartella_clinica ON utenti.id = cartella_clinica.id_paziente
            WHERE utenti.tipo = 'paziente';
        '''
        
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        pazienti = []

        for row in rows:
            # Crea l'oggetto Paziente
            paziente = Paziente(row[1], row[2], row[3])
            paziente.set_id(row[0])

            # Se la cartella clinica è presente, associare
            descrizione_cartella = row[4]
            if descrizione_cartella:
                cartella = CartellaClinica(descrizione_cartella)
                cartella.set_id(row[0])  # Usa lo stesso ID del paziente
                paziente.set_cartella_clinica(cartella)

            # Aggiungi il paziente alla lista
            pazienti.append(paziente)

        return pazienti

        
    
    def modifica_paziente(self, id, nome, email, password):
        self.db.cursor.execute('''
            UPDATE utenti
            SET nome = ?, email = ?, password = ?
            WHERE id = ?
        ''', (nome, email, password, id))
        self.db.conn.commit()
        
    def elimina_paziente(self, paziente_id):
        try:
            # Elimina il paziente dal database
            self.db.cursor.execute('''
                DELETE FROM utenti
                WHERE id = ? 
            ''', (paziente_id,))
            
            # Conferma l'operazione
            self.db.conn.commit()

        except Exception as e:
            print(f"Errore durante l'eliminazione del paziente: {e}")
            
    def aggiungi_cartella(self, descrizione, id_paziente):
        self.db.cursor.execute('''
                INSERT INTO cartella_clinica (id_paziente, descrizione)
                VALUES (?, ?)
            ''', (id_paziente, descrizione))
        self.db.conn.commit()
        
    def modifica_cartella(self, id, descrizione):
        self.db.cursor.execute('''
            UPDATE cartella_clinica
            SET  descrizione = ?
            WHERE id = ?
        ''', (descrizione, id))
        self.db.conn.commit()

    
    def carica_prenotazioni (self):
        from model.prenotazione import Prenotazione
        from model.paziente import Paziente
        
        self.db.cursor.execute ("SELECT * FROM prenotazioni")
        rows = self.db.cursor.fetchall()
        
        prenotazioni = []
        
        for row in rows:
            
            self.db.cursor.execute('SELECT * FROM utenti WHERE id = ?', (row[0],))
            dati = self.db.cursor.fetchone()
            
            paziente = Paziente(dati[1], dati [2], dati[3])
            
            prenotazione = Prenotazione(row[3], paziente)
            
            prenotazioni.append(prenotazione)
        
        return prenotazioni
    
    
    def carica_esercizi(self):
        from model.esercizio import Esercizio
        
        self.db.cursor.execute ("SELECT * FROM esercizi")
        rows = self.db.cursor.fetchall()
        
        esercizi = []
        
        for row in rows:
            
            esercizio = Esercizio(row[1], row[2], row[3])
            esercizio.set_id(row[0])
            
            esercizi.append(esercizio)
        
        return esercizi
    
    def elimina_esercizio(self, id):
        self.db.cursor.execute('''
                DELETE FROM esercizi
                WHERE id = ? 
            ''', (id,))
            
        self.db.conn.commit()
        
    def modifica_esercizio(self, esercizio):
        
        self.db.cursor.execute('''
            UPDATE esercizi
            SET  titolo = ?, descrizione = ?, video_url = ?
            WHERE id = ?
        ''', (esercizio.get_titolo(),esercizio.get_descrizione(), esercizio.get_video(), esercizio.get_id()))
        self.db.conn.commit()
        
    def get_esercizi_assegnati(self):
        from model.esercizio_assegnato import EsercizioAssegnato

        # Query per unire esercizio_assegnato con esercizi e recuperare i dati necessari
        self.db.cursor.execute('''
            SELECT 
                ea.id_paziente,
                ea.stato,
                e.id AS esercizio_id,
                e.titolo,
                e.descrizione,
                e.video_url
            FROM esercizio_assegnato ea
            INNER JOIN esercizi e ON ea.id_esercizio = e.id
        ''')
        rows = self.db.cursor.fetchall()

        esercizi_assegnati = []

        for row in rows:
            id_paziente, stato, esercizio_id, titolo, descrizione, video_url = row

            # Recupera l'oggetto Paziente
            paziente = self.get_paziente_by_id(id_paziente)

            # Creare l'oggetto EsercizioAssegnato
            esercizio_assegnato = EsercizioAssegnato(titolo, descrizione, video_url)
            esercizio_assegnato.set_id(esercizio_id)
            esercizio_assegnato.set_stato(stato)
            esercizio_assegnato.set_paziente(paziente)  # Assegna l'oggetto Paziente

            esercizi_assegnati.append(esercizio_assegnato)

        print(esercizi_assegnati)
        return esercizi_assegnati

    
        
    def get_paziente_by_id(self, id_paziente):
        from model.paziente import Paziente

        # Query per recuperare i dettagli del paziente
        self.db.cursor.execute('''
            SELECT id, nome, email, password, tipo 
            FROM utenti
            WHERE id = ?
        ''', (id_paziente,))
        row = self.db.cursor.fetchone()

        if row:
            id, nome, email, password, tipo = row  # Adatta al numero di colonne
            if tipo != 'paziente':  # Assicurati che sia un paziente
                return None
            paziente = Paziente(nome, email, password)
            paziente.set_id(id)
            return paziente
        return None

    
    def get_esercizi_assegnati_paziente(self, id_paziente):
        from model.esercizio_assegnato import EsercizioAssegnato

        # Query filtrata per un paziente specifico
        self.db.cursor.execute('''
            SELECT 
                ea.id_paziente,
                ea.stato,
                e.id AS esercizio_id,
                e.titolo,
                e.descrizione,
                e.video_url
            FROM esercizio_assegnato ea
            INNER JOIN esercizi e ON ea.id_esercizio = e.id
            WHERE ea.id_paziente = ?
        ''', (id_paziente,))
        rows = self.db.cursor.fetchall()

        esercizi_assegnati = []

        # Recupera l'oggetto Paziente
        paziente = self.get_paziente_by_id(id_paziente)

        for row in rows:
            _, stato, esercizio_id, titolo, descrizione, video_url = row

            # Creare l'oggetto EsercizioAssegnato
            esercizio_assegnato = EsercizioAssegnato(titolo, descrizione, video_url)
            esercizio_assegnato.set_id(esercizio_id)
            esercizio_assegnato.set_stato(stato)
            esercizio_assegnato.set_paziente(paziente)  # Assegna l'oggetto Paziente

            esercizi_assegnati.append(esercizio_assegnato)

        return esercizi_assegnati


    
    
    def aggiungi_esercizio_assegnato(self, id_paziente, id_esercizio, stato="incompleto"):
        self.db.cursor.execute('''
            INSERT INTO esercizio_assegnato (id_paziente, id_esercizio, stato)
            VALUES (?, ?, ?)
        ''', (id_paziente, id_esercizio, stato))
        self.db.conn.commit()
        
    def rimuovi_esercizio_assegnato(self, id):
        self.db.cursor.execute('''
                DELETE FROM esercizio_assegnato
                WHERE id_esercizio = ? 
            ''', (id,))
            
        self.db.conn.commit()



            
            
            