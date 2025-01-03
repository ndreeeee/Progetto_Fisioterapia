import sqlite3
from database import Database


class GestoreDati:
    def __init__ (self):
        self.db = Database()

    
    
    def inserisci_esercizio(self, titolo, descrizione, video):
        self.db.cursor.execute('''
                INSERT INTO esercizi (titolo, descrizione, video_url)
                VALUES (?, ?, ?)
            ''', (titolo, descrizione, video))
        self.db.conn.commit()
        
    def get_esercizi(self):
        from model.esercizio import Esercizio
        
        self.db.cursor.execute("SELECT * FROM esercizi")
        rows = self.db.cursor.fetchall()
        
        esercizi = []
        
        for row in rows:
            esercizio = Esercizio (row[1], row[2], row[3])
            esercizi.append(esercizio)
    
        return esercizi
    

        
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
        from model.cartella_clinica import CartellaClinica

        query = '''
            SELECT 
                utenti.id,
                utenti.nome,
                utenti.email,
                utenti.password,
                utenti.tipo,
                cartella_clinica.descrizione AS descrizione_cartella
            FROM utenti
            LEFT JOIN cartella_clinica ON utenti.id = cartella_clinica.id_paziente;
        '''
        
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        utenti = []

        for row in rows:
            # Determina il tipo di utente
            if row[4] == 'fisioterapista':
                utente = Fisioterapista(row[1], row[2], row[3])
            elif row[4] == 'paziente':
                utente = Paziente(row[1], row[2], row[3])
                
                # Associa la cartella clinica se presente
                descrizione_cartella = row[5]
                if descrizione_cartella:
                    cartella = CartellaClinica(descrizione_cartella)
                    cartella.set_id(row[0])  # Usa lo stesso ID del paziente
                    utente.set_cartella_clinica(cartella)

            utente.set_id(row[0])
            utenti.append(utente)

        return utenti

    
    def carica_pazienti(self):
        from model.paziente import Paziente
        from model.cartella_clinica import CartellaClinica

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
                cartella.set_id(row[0])  
                paziente.set_cartella_clinica(cartella)
                print(f"{paziente.get_nome()} cartella -- {paziente.get_cartella_clinica().get_descrizione()}")

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
        print("Inserimento completato con successo")

        
    def modifica_cartella(self, id, descrizione):
        self.db.cursor.execute('''
            UPDATE cartella_clinica
            SET  descrizione = ?
            WHERE id_paziente = ?
        ''', (descrizione, id))
        self.db.conn.commit()

    
    def carica_prenotazioni(self):
        from model.prenotazione import Prenotazione
        
        self.db.cursor.execute('SELECT id, data_ora, id_paziente, stato FROM prenotazioni')
        prenotazioni = []
        for row in self.db.cursor.fetchall():
            id_prenotazione = row[0]
            data_ora = row[1]
            id_paziente = row[2]
            stato = row[3]
            
            # Cerca il paziente solo se esiste un id_paziente (non NULL)
            paziente = None
            if id_paziente:
                paziente = self.get_paziente_by_id(id_paziente)

            prenotazione = Prenotazione(data_ora, paziente)
            prenotazione.set_id(id_prenotazione)
            prenotazione.set_stato(stato)
            prenotazioni.append(prenotazione)

        return prenotazioni
    
    def get_prenotazioni_effettuate(self):
        from model.prenotazione import Prenotazione
        
        self.db.cursor.execute('SELECT id, data_ora, id_paziente, stato FROM prenotazioni WHERE stato = "prenotato"')
        prenotazioni = []
        for row in self.db.cursor.fetchall():
            id_prenotazione = row[0]
            data_ora = row[1]
            id_paziente = row[2]
            stato = row[3]
            
            # Cerca il paziente solo se esiste un id_paziente (non NULL)
            paziente = None
            if id_paziente:
                paziente = self.get_paziente_by_id(id_paziente)

            prenotazione = Prenotazione(data_ora, paziente)
            prenotazione.set_id(id_prenotazione)
            prenotazione.set_stato(stato)
            prenotazioni.append(prenotazione)

        return prenotazioni
    
    
    def salva_prenotazioni(self, prenotazioni):
        for prenotazione in prenotazioni:
            try:
                # Verifica se la prenotazione esiste già nel DB
                self.db.cursor.execute(
                    "SELECT COUNT(*) FROM prenotazioni WHERE data_ora = ?", (prenotazione.get_data_e_ora(),)
                )
                esiste = self.db.cursor.fetchone()[0]

                if esiste == 0:
                    # Inserisce la nuova prenotazione
                    self.db.cursor.execute(
                        "INSERT INTO prenotazioni (data_ora, stato) VALUES (?, ?)",
                        (prenotazione.get_data_e_ora(), prenotazione.get_stato())
                    )
            except Exception as e:
                print(f"Errore durante il salvataggio della prenotazione: {e}")

        self.db.conn.commit()  # Conferma le modifiche al database
        
    def prenota(self, prenotazione):
        paziente = prenotazione.get_paziente()
        id_paziente = paziente.get_id()
        self.db.cursor.execute('''
            UPDATE prenotazioni
            SET  stato = ?, id_paziente = ?
            WHERE id = ?
        ''', (prenotazione.get_stato(), id_paziente, prenotazione.get_id()))
        self.db.conn.commit()
        
    def elimina_prenotazione(self, prenotazione):
        paziente = prenotazione.get_paziente()
        id_paziente = paziente.get_id()
        self.db.cursor.execute('''
            UPDATE prenotazioni
            SET  stato = ?, id_paziente = NULL
            WHERE id = ?
        ''', (prenotazione.get_stato(), prenotazione.get_id()))
        self.db.conn.commit()
   
    
    def get_prenotazioni_per_paziente(self, id_paziente):
        from model.prenotazione import Prenotazione
        self.db.cursor.execute('SELECT id, data_ora, stato FROM prenotazioni WHERE id_paziente = ?', (id_paziente,))
        prenotazioni = []
        for row in self.db.cursor.fetchall():
            id_prenotazione = row[0]
            data_ora = row[1]
            stato = row[2]
            
            # Crea un oggetto Prenotazione con i dati
            paziente = self.get_paziente_by_id(id_paziente)
            prenotazione = Prenotazione(data_ora, paziente)
            prenotazione.set_id(id_prenotazione)
            prenotazione.set_stato(stato) 
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
        
    def get_cartella_clinica_utente(self, id):
        from model.cartella_clinica import CartellaClinica
        self.db.cursor.execute('''
            SELECT * FROM cartella_clinica
            WHERE id_paziente = ?
        ''', (id,))
        cartella = self.db.cursor.fetchone()
        print("dati", cartella)

        if cartella:
            cartella_clinica = CartellaClinica(cartella[2])
            cartella_clinica.set_id(cartella[0])
            print("dati", cartella_clinica)
            # Restituisce la descrizione della cartella clinica
            return cartella_clinica
        
    def aggiorna_stato(self, paziente, esercizio, stato):
        
        self.db.cursor.execute('''
            UPDATE esercizio_assegnato
            SET  stato = ?
            WHERE id_esercizio = ? AND id_paziente = ?
        ''', (stato,  esercizio.get_id(), paziente.get_id()))
        self.db.conn.commit()
        
    def get_fisioterapista(self):
        from model.fisioterapista import Fisioterapista
        self.db.cursor.execute('SELECT * FROM utenti WHERE tipo = "fisioterapista"')
        row = self.db.cursor.fetchone()
        
        fisioterapista = Fisioterapista(row[1], row[2], row[3])
        fisioterapista.set_id(row[0])
        return fisioterapista

    
 

    def carica_messaggi(self):
        from model.messaggio import Messaggio
        

        try:
            # Recupera tutti i messaggi dal database
            self.db.cursor.execute("SELECT * FROM messaggi")
            rows = self.db.cursor.fetchall()

            messaggi = []

            for row in rows:
                messaggio_id = row[0]
                mittente_id = row[1]
                destinatario_id = row[2]
                descrizione = row[3]
                timestamp = row[4]

                # Recupera i dettagli del mittente
                self.db.cursor.execute("SELECT * FROM utenti WHERE id = ?", (mittente_id,))
                mittente_data = self.db.cursor.fetchone()

                if mittente_data is None:
                    print(f"Errore: Nessun utente trovato con ID {mittente_id}.")
                    continue

                mittente = self.crea_utente(mittente_data)

                # Recupera i dettagli del destinatario
                self.db.cursor.execute("SELECT * FROM utenti WHERE id = ?", (destinatario_id,))
                destinatario_data = self.db.cursor.fetchone()

                if destinatario_data is None:
                    print(f"Errore: Nessun utente trovato con ID {destinatario_id}.")
                    continue

                destinatario = self.crea_utente(destinatario_data)

                # Crea l'oggetto Messaggio
                messaggio = Messaggio(descrizione, destinatario, mittente, timestamp)
                messaggio.set_id(messaggio_id)
                messaggi.append(messaggio)

            print(f"Messaggi caricati: {len(messaggi)}")
            return messaggi

        except sqlite3.Error as e:
            print(f"Errore durante il caricamento dei messaggi: {e}")
            return []

    def crea_utente(self, utente_data):
        from model.fisioterapista import Fisioterapista
        from model.paziente import Paziente
        user_id, nome, email, password, tipo = utente_data

        if tipo == "fisioterapista":
            utente = Fisioterapista(nome,email,password)
            utente.set_id(user_id)
            return utente
        elif tipo == "paziente":
            utente= Paziente(nome, email, password)
            utente.set_id(user_id)
            return utente
        else:
            raise ValueError(f"Tipo di utente sconosciuto: {tipo}")
        
    def salva_messaggio(self, messaggio, mittente_id, destinatario_id):
        self.db.cursor.execute('''
            INSERT INTO messaggi (mittente_id, destinatario_id, messaggio)
            VALUES (?, ?, ?)
        ''', (mittente_id, destinatario_id, messaggio.get_descrizione()))
        self.db.conn.commit()