import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class PrenotazioniFisio():
    def __init__(self, root, fisioterapista, gestore):
        self.root = root
        self.fisioterapista = fisioterapista
        self.gestore = gestore
        
        prenotazioni_window = tk.Toplevel(self.root)
        prenotazioni_window.title("Gestisci Prenotazioni")
        prenotazioni_window.geometry("900x700")  
        prenotazioni_window.config(bg="#f5f5f5")  

        title_label = tk.Label(prenotazioni_window, text="Elenco Prenotazioni", font=("Arial", 16, "bold"), bg="#f5f5f5")
        title_label.pack(pady=10)

        frame = tk.Frame(prenotazioni_window)
        frame.pack(pady=10)

        self.results_listbox = tk.Listbox(frame, width=70, height=20, font=("Arial", 14), bg="#ffffff", selectbackground="#cceeff")
        self.results_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_listbox.yview)

        prenotazioni = self.gestore.get_prenotazioni()

        self.results_listbox.delete(0, tk.END)

        if not prenotazioni:
            messagebox.showinfo("Nessuna Prenotazione", "Non ci sono prenotazioni.")
        else:
            for prenotazione in prenotazioni:
                self.results_listbox.insert(
                    tk.END, 
                    f"ID-prenotazione: {prenotazione.get_id()}, Paziente: {prenotazione.get_paziente().get_nome()}, Data: {prenotazione.get_data_e_ora()}"
                )
                
        back_button = ttk.Button(prenotazioni_window, text="Torna Indietro", command=prenotazioni_window.destroy, style="TButton")
        back_button.pack(pady=20, ipadx=10, ipady=5)
        
        
        
        
        
        #remove_button = ttk.Button(prenotazioni_window, text="Rimuovi Prenotazione", command=self.rimuovi_prenotazione)
        #remove_button.pack(pady=10)
        
        

        #remove_button.config(width=20)
    """   
    def rimuovi_prenotazione(self):
        selezione = self.results_listbox.curselection()
        if selezione:
            indice = selezione[0]
            prenotazione_selezionata = self.results_listbox.get(indice)
            id_prenotazione = int(prenotazione_selezionata.split(",")[0].split(":")[1].strip())

            self.prenotazione_controller.rimuovi_prenotazione(id_prenotazione)

            self.results_listbox.delete(indice)

            messagebox.showinfo("Successo", "Prenotazione rimossa con successo.")
        else:
            messagebox.showerror("Errore", "Seleziona una prenotazione da rimuovere.")"""