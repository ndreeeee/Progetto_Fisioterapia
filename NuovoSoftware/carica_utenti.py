import sqlite3

def print_utenti(db_name="gestione_fisioterapia.db"):
    try:
        # Connessione al database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Recupera tutti gli utenti dalla tabella "utenti"
        cursor.execute("SELECT id, nome, email, tipo FROM utenti")
        utenti = cursor.fetchall()

        # Controlla se ci sono utenti
        if not utenti:
            print("Non ci sono utenti nel database.")
            return

        # Stampa gli utenti
        print("Lista utenti:")
        for utente in utenti:
            print(f"ID: {utente[0]}, Nome: {utente[1]}, Email: {utente[2]}, Tipo: {utente[3]}")

        # Chiude la connessione
        conn.close()

    except sqlite3.Error as e:
        print(f"Errore durante il recupero degli utenti: {e}")
        
def print_esercizi_assegnati(db_name="gestione_fisioterapia.db"):
    try:
        # Connessione al database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Recupera tutti gli utenti dalla tabella "utenti"
        cursor.execute("SELECT id_paziente, id_esercizio, stato FROM esercizio_assegnato")
        utenti = cursor.fetchall()

        # Controlla se ci sono utenti
        if not utenti:
            print("Non ci sono utenti nel database.")
            return

        # Stampa gli utenti
        print("Lista utenti:")
        for utente in utenti:
            print(f"id_paziente: {utente[0]}, id_esercizio: {utente[1]}, stato: {utente[2]}")

        # Chiude la connessione
        conn.close()

    except sqlite3.Error as e:
        print(f"Errore durante il recupero degli utenti: {e}")
        

def print_prenotazioni(db_name="gestione_fisioterapia.db"):
    try:
        # Connessione al database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Recupera tutti gli utenti dalla tabella "utenti"
        cursor.execute("SELECT id, id_paziente, stato FROM prenotazioni")
        utenti = cursor.fetchall()

        # Controlla se ci sono utenti
        if not utenti:
            print("Non ci sono utenti nel database.")
            return

        # Stampa gli utenti
        print("Lista utenti:")
        for utente in utenti:
            print(f"id: {utente[0]}, id_paziente: {utente[1]}, stato: {utente[2]}")

        # Chiude la connessione
        conn.close()

    except sqlite3.Error as e:
        print(f"Errore durante il recupero degli utenti: {e}")
        
        
def correggi_prenotazioni_incoerenti(db_name="gestione_fisioterapia.db"):
    
   
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id
        FROM prenotazioni
        WHERE stato = 'prenotato' AND id_paziente IS NULL
    ''')
    prenotazioni_incoerenti = cursor.fetchall()

    # Se ci sono prenotazioni incoerenti, aggiornale
    if prenotazioni_incoerenti:
        for prenotazione in prenotazioni_incoerenti:
            cursor.execute('''
                UPDATE prenotazioni
                SET stato = 'disponibile'
                WHERE id = ?
            ''', (prenotazione[0],))  # prenotazione[0] è l'ID della prenotazione

        conn.commit()
        print(f"Corrette {len(prenotazioni_incoerenti)} prenotazioni incoerenti.")
    else:
        print("Nessuna prenotazione incoerente trovata.")

        
if __name__ == "__main__":
    print_utenti()
    print_esercizi_assegnati()
    correggi_prenotazioni_incoerenti()

    print_prenotazioni()

