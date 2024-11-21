import tkinter as tk
from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog


# width=700, height=600
class CercaPazienteView(tk.Frame):
    def __init__(self, flag, root, fisioterapista):
        self.fisioterapista = fisioterapista
        search_window = tk.Toplevel(root)
        search_window.title("Cerca Paziente")

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"))

        search_frame = ttk.Frame(search_window, width=900, height=700)
        search_frame.pack_propagate(False) 
        search_frame.pack(pady=20, padx=20)  

        
        ttk.Label(search_frame, text="Inserisci il nome o cognome del paziente", style="TLabel").pack(pady=10)

        
        self.search_entry = ttk.Entry(search_frame, font=("Arial", 14), width=40)
        self.search_entry.pack(pady=10)

        
        self.search_entry.bind("<KeyRelease>", self.aggiorna_ricerca)
        
        self.results_listbox = tk.Listbox(search_frame, width=80, height=20, font=("Arial", 14))  
        self.results_listbox.pack(pady=10)

        back_button = ttk.Button(search_frame, text="Torna Indietro", command=search_window.destroy, style="TButton")
        back_button.pack(pady=20, ipadx=10, ipady=5)  

        self.visualizza_tutti_pazienti(fisioterapista)  
        
        if flag == 1:
            self.results_listbox.bind("<Double-1>", self.apri_chat_paziente)
            
            
        
    def visualizza_tutti_pazienti(self, fisioterapista):
        self.results_listbox.delete(0, tk.END)
        for paziente in self.fisioterapista.lista_pazienti:
            self.results_listbox.insert(tk.END, f"Nome: {paziente.nome}, Email: {paziente.email}")

        self.results_listbox.bind("<Double-1>", self.apri_profilo_paziente)
        
        
   
    
    def aggiorna_ricerca(self, event):
        query = self.search_entry.get().strip()  
        if query:
            
            risultati = self.fisioterapista.cerca_pazienti(query)
            self.results_listbox.delete(0, tk.END)

            if risultati:
                for paziente in risultati:
                    try:
                        
                        self.results_listbox.insert(tk.END, f"Nome: {paziente.nome}, Email: {paziente.email}")
                    except KeyError:
                        self.results_listbox.insert(tk.END, "Dati paziente non validi.")
            else:
                self.results_listbox.insert(tk.END, "Nessun paziente trovato.")
        else:
            self.visualizza_tutti_pazienti(self.fisioterapista)  