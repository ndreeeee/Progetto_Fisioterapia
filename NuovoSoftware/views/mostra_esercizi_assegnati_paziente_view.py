import tkinter as tk
from tkinter import font
from views.mostra_dettagli_esercizio_paziente_view import MostraDettagliEsercizioPazienteView


class MostraEserciziAssegnatiView():
    def __init__(self, root, paziente, gestore):
        self.root = root
        self.paziente = paziente
        self.gestore = gestore
        
        search_window = tk.Toplevel(self.root)
        search_window.title("Esercizi assegnati")
        search_window.geometry("900x700")  
        
        search_frame = tk.Frame(search_window, width=900, height=700, bg="#f0f0f0")
        search_frame.pack_propagate(False)
        search_frame.pack(pady=20, padx=20)
        
        titolo_font = font.Font(family="Arial", size=16, weight="bold")
        testo_font = font.Font(family="Arial", size=14)
        
        label = tk.Label(search_frame, text="Clicca su un esercizio per vederne i dettagli!", font=titolo_font, bg="#f0f0f0")
        label.pack(pady=10)


        esercizi = self.gestore.get_esercizi_assegnati(self.paziente)
        print("view", esercizi)

        self.esercizi_listbox = tk.Listbox(search_frame, font=testo_font, bg="#ffffff", fg="#333333", height=15, width = 80, bd=2)
        self.esercizi_listbox.pack(pady=20)

        if not esercizi:
            tk.Label(search_frame, text="Nessun esercizio assegnato.", font=titolo_font, bg="#f0f0f0").pack(pady=10)
        else:
            for esercizio in esercizi:
                self.esercizi_listbox.insert(tk.END, f"{esercizio.titolo}")
                
            self.esercizi_listbox.bind("<<ListboxSelect>>", self.mostra_dettagli_esercizio)
        
        
        back_button = tk.Button(search_window, text="Torna Indietro", command=search_window.destroy,
                                bg="#4CAF50", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        back_button.pack()

    def mostra_dettagli_esercizio(self, event):
        try:
            selezione = self.esercizi_listbox.curselection()  
            if selezione:
                indice = selezione[0]
                esercizio_selezionato = self.esercizi_listbox.get(indice) 
                


                MostraDettagliEsercizioPazienteView(self.root, esercizio_selezionato, self.paziente)
        except Exception as e:
            print(f"Errore durante la visualizzazione dei dettagli dell'esercizio: {e}")
