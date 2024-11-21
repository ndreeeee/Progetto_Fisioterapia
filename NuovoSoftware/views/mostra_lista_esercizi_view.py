import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog

from views.mostra_form_aggiungi_esercizio_view import MostraFormAggiungiEsercizio
from views.mostra_dettagli_esercizio_view import VisualizzaDettagliEsercizio

class MostraListaEsercizi:
    def __init__(self, root, fisioterapista):
        self.root = root
        self.fisioterapista = fisioterapista
        
        
        form_window = tk.Toplevel(self.root)
        form_window.title("Lista degli esercizi")

        self.main_frame = tk.Frame(form_window, width=900, height=800)
        self.main_frame.pack_propagate(False)  
        self.main_frame.pack()

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"))

        self.spazio = ttk.Label(self.main_frame)
        self.spazio.pack(expand=True)

        
        esercizi = self.fisioterapista.lista_esercizi

      
        self.search_frame = ttk.Frame(self.main_frame)
        self.search_frame.pack(pady=10)

        self.search_entry = ttk.Entry(self.search_frame,font=("Arial", 14), width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=10)
 
        self.search_entry.bind("<KeyRelease>", self.cerca_esercizi)

        self.listbox = tk.Listbox(self.main_frame, width=80, height=15, font=("Arial", 14))
        self.listbox.pack(padx=10, pady=10)

       
        if not esercizi:
            ttk.Label(self.main_frame, text="Nessun esercizio trovato.").pack()
        else:
            self.esercizi_data = {}  
            
            for esercizio in esercizi:
                
                """
                id_esercizio = esercizio[0]  
                titolo = esercizio[1]
                descrizione = esercizio[2]
                    """
          
                self.listbox.insert(tk.END, f"{esercizio.titolo}")
                
                """                # Memorizza le informazioni degli esercizi nel dizionario
                self.esercizi_data[id_esercizio] = {
                    "titolo": titolo,
                    "descrizione": descrizione,
                    "video_url": esercizio[3]  
                }"""


        self.listbox.bind("<Double-1>", lambda event: self.mostra_dettagli_esercizio(self.listbox, self.esercizi_data, event))

        back_button = ttk.Button(self.main_frame, text="Torna Indietro", command=form_window.destroy)
        back_button.pack(pady=20, ipadx=10, ipady=5)

        aggiungi_button = ttk.Button(self.main_frame, text="Aggiungi Esercizio", command=lambda: MostraFormAggiungiEsercizio(self.root, fisioterapista))
        aggiungi_button.pack(pady=20, ipadx=10, ipady=5)

        remove_button = ttk.Button(self.main_frame, text="Rimuovi Esercizio", command=lambda:self.rimuovi_esercizio_lista(self.listbox))
        remove_button.pack(pady=20, ipadx=10, ipady=5)

        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        
    def cerca_esercizi(self, event=None):
        
        search_text = self.search_entry.get().lower()
        
        self.listbox.delete(0, tk.END)
        
        for id_esercizio, info in self.esercizi_data.items():
            if search_text in info['titolo'].lower():  
                self.listbox.insert(tk.END, f"{id_esercizio}: {info['titolo']}")
                
    def mostra_dettagli_esercizio(self, listbox, esercizi_data, event):
            
            try:
                selezione = listbox.curselection()  
                if selezione:
                    indice = selezione[0]  
                    esercizio_selezionato = listbox.get(indice) 
                    
                    id_esercizio = int(esercizio_selezionato.split(":")[0])

                    dettagli_esercizio = esercizi_data[id_esercizio]

                    VisualizzaDettagliEsercizio(dettagli_esercizio, id_esercizio)
            except Exception as e:
                print(f"Errore durante la visualizzazione dei dettagli dell'esercizio: {e}")