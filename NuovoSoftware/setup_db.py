from database import Database

if __name__ == "__main__":
    db = Database()
    db.aggiungi_utente("Dott. Rossi", "dottor.rossi@email.com", "password123", "fisioterapista")
    db.aggiungi_utente("Marco Rossi", "marco@email.com", "password123", "paziente")
    print("Database inizializzato e popolato con utenti di esempio.")
    db.conn.close()