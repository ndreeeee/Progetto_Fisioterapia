import tkinter as tk
import tkinter.ttk as ttk
from views.profilo_paziente_view import ProfiloPaziente
from views.messaggi_view import MessaggiView


# width=700, height=600
class CercaPazienteView:
    def __init__(self, flag, root, fisioterapista, gestore, gestoreEsercizi):
        self.root = root
        self.fisioterapista = fisioterapista
        self.gestoreEsercizi = gestoreEsercizi
        search_window = tk.Toplevel(self.root)
        self.gestore = gestore
        self.flag = flag
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

        self.visualizza_tutti_pazienti()  
        
        if self.flag == 1:
            self.results_listbox.bind("<Double-1>", self.apri_chat_paziente)
        else:
            self.results_listbox.bind("<Double-1>", self.apri_profilo_paziente)

            
            
        
    def visualizza_tutti_pazienti(self):
        self.results_listbox.delete(0, tk.END)
        lista_pazienti = self.gestore.get_pazienti()
        for paziente in lista_pazienti:
            self.results_listbox.insert(tk.END, f"Nome: {paziente.nome}, Email: {paziente.email}")

        
        
   
    
    def aggiorna_ricerca(self, event):
        query = self.search_entry.get().strip()  
        if query:
            
            risultati = self.gestore.cerca_pazienti(query)
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
            self.visualizza_tutti_pazienti()  
    
    
    def apri_profilo_paziente(self, event):
        indice_selezionato = self.results_listbox.curselection()
        if indice_selezionato:
            
            testo_selezionato = self.results_listbox.get(indice_selezionato[0])

            dati = testo_selezionato.split(", ")
            nome = dati[0].split(": ")[1]  
            email = dati[1].split(": ")[1]  
            paziente = self.gestore.ottieni_paziente(nome, email)
            ProfiloPaziente(self.root, paziente, self.gestore, self.gestoreEsercizi)
            
    def apri_chat_paziente(self, event):

        indice_selezionato = self.results_listbox.curselection()
        if indice_selezionato:
            
            testo_selezionato = self.results_listbox.get(indice_selezionato[0])

            dati = testo_selezionato.split(", ")
            nome = dati[0].split(": ")[1]  
            email = dati[1].split(": ")[1]  
            paziente = self.gestore.ottieni_paziente(nome, email)
            root = tk.Tk() 
            MessaggiView(root, paziente, self.fisioterapista, 1)
            