import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

class MostraDettagliEsercizioPazienteView():
    def __init__(self, root, titolo, paziente, gestore):
        self.root = root
        self.titolo = titolo
        self.esercizio = gestore.get_esercizio(titolo)
        self.paziente = paziente
        self.gestore = gestore
        
        dettagli_window = tk.Toplevel(root)
        dettagli_window.title(f"Dettagli Esercizio: {self.esercizio.get_titolo()}")
        dettagli_window.geometry("900x800")  

        titolo_font = font.Font(family="Arial", size=14, weight="bold")
        testo_font = font.Font(family="Arial", size=14)

        dettagli_frame = tk.Frame(dettagli_window, bg="#f0f0f0")
        dettagli_frame.pack(fill="both", expand=True, padx=20, pady=20)

        titolo_label = tk.Label(dettagli_frame, text=f"Titolo: {self.esercizio.get_titolo()}", font=titolo_font, bg="#f0f0f0")
        titolo_label.pack(pady=15)

        descrizione_label = tk.Label(dettagli_frame, text="Descrizione:", font=titolo_font, bg="#f0f0f0")
        descrizione_label.pack(pady=10)

        descrizione_text = tk.Text(dettagli_frame, height=15, width=80, font=testo_font, bg="#ffffff", fg="#333333")
        descrizione_text.pack(pady=10)
        descrizione_text.insert(tk.END, self.esercizio.get_descrizione())
        descrizione_text.config(state=tk.DISABLED)
        
        video_url = tk.Label(dettagli_frame, text=f"Video URL: {self.esercizio.get_video()}", fg="blue", cursor="hand2")
        video_url.pack(pady=10)
        video_url.bind("<Button-1>", lambda e: self.apri_url(self.esercizio.get_video()))


        self.stato_var = 0
        
        stato_corrente = self.esercizio.get_stato()
        
        self.stato_var = tk.IntVar(value=1 if stato_corrente == 'completato' else 0)

            
    
        completato_checkbox = tk.Checkbutton(dettagli_frame, text="Esercizio Completato", variable=self.stato_var, font=testo_font, bg="#f0f0f0")
        completato_checkbox.pack(pady=20)
        
        aggiorna_stato_button = tk.Button(dettagli_frame, text="Aggiorna Stato", command=lambda: self.gestore.aggiorna_stato_esercizio(self.paziente, self.esercizio, self.stato_var),
                                        bg="#4CAF50", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        aggiorna_stato_button.pack(pady=15)

        back_button = tk.Button(dettagli_frame, text="Torna Indietro", command=dettagli_window.destroy,
                                bg="#f44336", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        back_button.pack(pady=20)
        
    def apri_url(self, url):
        import webbrowser
        webbrowser.open(url)