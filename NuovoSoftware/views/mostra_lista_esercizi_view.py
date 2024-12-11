import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog

from views.mostra_form_aggiungi_esercizio_view import MostraFormAggiungiEsercizio
from views.mostra_dettagli_esercizio_view import VisualizzaDettagliEsercizio

class MostraListaEsercizi:
    def __init__(self, root, fisioterapista, gestoreEsercizi):
        self.root = root
        self.fisioterapista = fisioterapista
        self.gestoreEsercizi = gestoreEsercizi
        
        
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

        
        esercizi = self.gestoreEsercizi.get_esercizi()

      
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
          
                self.listbox.insert(tk.END, f"{esercizio.titolo}")
                
            


        self.listbox.bind("<Double-1>", lambda event: self.mostra_dettagli_esercizio(self.listbox, event))

        back_button = ttk.Button(self.main_frame, text="Torna Indietro", command=form_window.destroy)
        back_button.pack(pady=20, ipadx=10, ipady=5)

        aggiungi_button = ttk.Button(self.main_frame, text="Aggiungi Esercizio", command=lambda: MostraFormAggiungiEsercizio(self.root, fisioterapista, self.gestoreEsercizi))
        aggiungi_button.pack(pady=20, ipadx=10, ipady=5)

        remove_button = ttk.Button(self.main_frame, text="Rimuovi Esercizio", command=lambda:self.rimuovi_esercizio_lista(self.listbox))
        remove_button.pack(pady=20, ipadx=10, ipady=5)

        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        self.visualizza_esercizi()
        
        
        
    def visualizza_esercizi(self):
        self.listbox.delete(0, tk.END)
        lista_esercizi = self.gestoreEsercizi.get_esercizi()
        for esercizio in lista_esercizi:
            self.listbox.insert(tk.END, f"{esercizio.titolo}")
        
        
    def cerca_esercizi(self, event=None):
        
        search_text = self.search_entry.get().lower()
        if search_text:
            
            risultati = self.gestoreEsercizi.cerca_esercizio(search_text)
            self.listbox.delete(0, tk.END)
        
            if risultati:
                for esercizio in risultati:
                    try:
                        self.listbox.insert(tk.END, f"{esercizio.titolo}")
                    except KeyError:
                        self.listbox.insert(tk.END, f"Ricerca non valida")
            else:
                self.listbox.insert(tk.END, f"Nessun Esercizio trovato")
        else:
            self.listbox.delete(0,tk.END)

            for esercizio in self.gestoreEsercizi.lista_esercizi:
                self.listbox.insert(tk.END, f"{esercizio.titolo}")

    def rimuovi_esercizio_lista(self, listbox):
            selezione = self.listbox.curselection()
            if selezione:
                indice = selezione[0]
                esercizio = listbox.get(indice)
            

                
                conferma = messagebox.askyesno("Conferma", f"Sei sicuro di voler eliminare l'esercizio '{esercizio}'?")
                if conferma:
                    self.gestoreEsercizi.elimina_esercizio(esercizio)

                    self.listbox.delete(indice)
            else:
                messagebox.showerror("Errore", "Seleziona un esercizio da eliminare.")
            
                
    def mostra_dettagli_esercizio(self, listbox, event):
            
            try:
                selezione = listbox.curselection()  
                if selezione:
                    indice = selezione[0]  
                    esercizio = listbox.get(indice) 
                    ex_dettagli = self.gestoreEsercizi.ottieni_esercizio(esercizio)
                    
                    VisualizzaDettagliEsercizio(ex_dettagli, self.root, self.gestoreEsercizi)
            except Exception as e:
                print(f"Errore durante la visualizzazione dei dettagli dell'esercizio: {e}")