import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class GestisciEsercizi:
    def __init__(self, root, paziente, gestoreEsercizi):
        self.root = root
        self.paziente = paziente
        self.gestoreEsercizi = gestoreEsercizi
        
        profilo_paziente_window = tk.Toplevel(self.root)
        profilo_paziente_window.title("Gestisci Esercizi del Paziente")
        
        esercizi_window = ttk.Frame(profilo_paziente_window, width=900, height=700)
        esercizi_window.pack_propagate(False)
        esercizi_window.pack(pady=20, padx=20)

        esercizi = self.gestoreEsercizi.get_esercizi_assegnati_per_paziente(self.paziente)
        

        self.esercizi_listbox = tk.Listbox(esercizi_window, font=("Arial", 14), width=60, height=15)
        self.esercizi_listbox.pack(pady=10)
        
        if not esercizi:
            ttk.Label(esercizi_window, text="Nessun esercizio assegnato a questo paziente.", font=("Arial", 14)).pack(pady=10)
        else:
            for esercizio in esercizi:
                
                self.esercizi_listbox.insert(tk.END, f"{esercizio.get_titolo()} - {esercizio.get_descrizione()}") 
                print(f"Titolo: {esercizio.get_titolo()}, Descrizione: {esercizio.get_descrizione()}")
 
        
        stato_esercizio = ttk.Label(esercizi_window, text="", font=("Arial", 14), cursor="hand2")
        stato_esercizio.pack(pady=10)

        ttk.Button(esercizi_window, text="Aggiungi Esercizio",
                command=lambda: self.aggiungi_esercizio_al_paziente(self.paziente),
                style="TButton").pack(pady=10, ipadx=10, ipady=5)

        rimuovi_button = ttk.Button(esercizi_window, text="Rimuovi Esercizio",
                                    command=lambda: self.rimuovi_esercizio_al_paziente(),
                                    style="TButton")
        rimuovi_button.pack(pady=10, ipadx=10, ipady=5)

                
        """
        if self.controller.db.ottieni_stato_esercizio(id_paziente, id_esercizio) == 'completato':
            stato_esercizio.config(text="Il paziente ha completato l'esercizio", cursor="hand2", foreground="green")
        else:
            stato_esercizio.config(text="Il paziente NON ha ancora completato l'esercizio", cursor="hand2", foreground="red")
            """

    def rimuovi_esercizio_al_paziente(self):
        selezione = self.esercizi_listbox.curselection()

        if selezione:
            esercizio_selezionato = self.esercizi_listbox.get(selezione[0])
            titolo_esercizio = esercizio_selezionato.split("-")[0].strip()  

            conferma = messagebox.askyesno("Conferma", f"Sei sicuro di voler rimuovere l'esercizio '{titolo_esercizio}'?")

            if conferma:
                print("view", esercizio_selezionato)
                self.gestoreEsercizi.rimuovi_esercizio_assegnato(titolo_esercizio)

                self.esercizi_listbox.delete(selezione[0])

                messagebox.showinfo("Successo", "L'esercizio è stato rimosso con successo.")
        else:
            messagebox.showerror("Errore", "Seleziona un esercizio da rimuovere.")
            
                
    

            
            
            
    def aggiungi_esercizio_al_paziente(self, paziente):
        aggiungi_window = tk.Toplevel(self.root)
        aggiungi_window.title("Aggiungi Esercizio al Paziente")
        
        aggiungi_frame = ttk.Frame(aggiungi_window, width=900, height=700)
        aggiungi_frame.pack_propagate(False)
        aggiungi_frame.pack(pady=20, padx=20)
        
        label = tk.Label(aggiungi_frame, text = "Clicca l'esercizio da assegnare al paziente:", font = ("Arial",16, "bold"))
        label.pack(pady=10)

        esercizi_assegnati = self.gestoreEsercizi.get_esercizi_assegnati_per_paziente(self.paziente)
        
        
        esercizi_predefiniti = self.gestoreEsercizi.get_esercizi()
        
        titoli_assegnati = {esercizio.titolo for esercizio in esercizi_assegnati}
        esercizi_disponibili = [esercizio for esercizio in esercizi_predefiniti if esercizio.titolo not in titoli_assegnati]
            
        listbox_esercizi = tk.Listbox(aggiungi_frame, font=("Arial", 14), width=70, height=15)
        listbox_esercizi.pack(pady=10)

        for esercizio in esercizi_disponibili:
            listbox_esercizi.insert(tk.END, f"{esercizio.titolo}: {esercizio.descrizione}")  

        def on_double_click(event):
            selezione = listbox_esercizi.curselection()
            if selezione:
                index = selezione[0]
                esercizio_selezionato = esercizi_disponibili[index]
                
                
                
                self.gestoreEsercizi.aggiungi_esercizio_assegnato(self.paziente, esercizio_selezionato)
                self.esercizi_listbox.insert(tk.END, f"{esercizio_selezionato.titolo}: {esercizio_selezionato.descrizione}")
                
                messagebox.showinfo("Successo", f"Esercizio '{esercizio_selezionato.titolo}' assegnato con successo.")
                aggiungi_window.destroy()

        listbox_esercizi.bind("<Double-1>", on_double_click)