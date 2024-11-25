import tkinter as tkk
import pickle
import os
from views.login_view import LoginView
from gestore_dati import GestoreDati


def carica_utenti():
    try:
        with open('data/utenti.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def salva_utenti(lista_utenti):
    os.makedirs('data', exist_ok=True)
    with open('data/utenti.pkl', 'wb') as file:
        pickle.dump(lista_utenti, file, pickle.HIGHEST_PROTOCOL)
        
def on_close(root, lista_utenti):
    
    print("Salvataggio dei dati in corso...")
    salva_utenti(lista_utenti)  # Salva gli utenti nel file pickle
    root.destroy()  # Chiude la finestra

        


def main():
    lista_utenti = carica_utenti()    
    root = tkk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, lista_utenti))

    root.geometry("900x700")
    LoginView(root, lista_utenti)
    root.mainloop()

if __name__ == "__main__":
    main()