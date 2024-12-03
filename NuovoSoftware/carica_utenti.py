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

if __name__ == "__main__":
    print_utenti()

