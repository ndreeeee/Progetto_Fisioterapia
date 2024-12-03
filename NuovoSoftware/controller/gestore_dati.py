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
        self.db.cursor.execute("SELECT * FROM utenti")
        rows = self.db.cursor.fetchall()
        pazienti = []

        for row in rows:
            if row[4] == 'paziente':
                utente = Paziente(row[1], row[2], row[3])
                utente.set_id(row[0])
                pazienti.append(utente)
        
        
        return pazienti
        
    
    def modifica_paziente(self, paziente, nome, email, password):
        print(f"UPDATE utenti SET nome = '{nome}', email = '{email}', password = '{password}' WHERE id = {paziente.id}")
        self.db.cursor.execute('''
            UPDATE utenti
            SET nome = ?, email = ?, password = ?
            WHERE id = ?
        ''', (nome, email, password, paziente.get_id()))
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

            # Verifica quante righe sono state eliminate
            if self.db.cursor.rowcount == 0:
                print(f"Nessun paziente trovato con ID {paziente_id}.")
            else:
                print(f"Paziente con ID {paziente_id} eliminato con successo.")

        except Exception as e:
            print(f"Errore durante l'eliminazione del paziente: {e}")

    
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
        
        
        