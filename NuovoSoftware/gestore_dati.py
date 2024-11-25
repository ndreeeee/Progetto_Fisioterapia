import sqlite3
from tkinter import messagebox


class GestoreDati:
    def __init__ (self, db):
        self.db = db
        
        
    def ottieni_messaggi(self, fisioterapista, paziente):
        from model.messaggio import Messaggio
        
        
        # Recupera tutti i messaggi dal DB
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

            utenti.append(utente)
        
        
        return utenti
    
    def modifica_paziente(self, paziente, nome, email, password):
        # Recupera l'email corrente
        self.db.cursor.execute('SELECT email FROM utenti WHERE id = ?', (paziente.codice,))
        email_corrente = self.db.cursor.fetchone()

        if email_corrente and email_corrente[0] != email:
            # Se l'email è cambiata, controlla se è già in uso
            self.db.cursor.execute('SELECT * FROM utenti WHERE email = ?', (email,))
            if self.db.cursor.fetchone() is not None:
                messagebox.showerror("Errore", "Esiste già un paziente con questa email.")
                return

        # Procedi con l'aggiornamento
        self.db.cursor.execute('''
            UPDATE utenti
            SET nome = ?, email = ?, password = ?
            WHERE id = ?
        ''', (nome, email, password, paziente.codice))
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
        
        
        