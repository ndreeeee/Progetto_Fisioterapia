import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

class MostraDettagliEsercizioPazienteView():
    def __init__(self, root, esercizio, paziente):
        self.root = root
        self.esercizio = esercizio
        self.paziente = paziente
        
        dettagli_window = tk.Toplevel(root)
        dettagli_window.title(f"Dettagli Esercizio: {self.esercizio.titolo}")
        dettagli_window.geometry("900x800")  

        titolo_font = font.Font(family="Arial", size=14, weight="bold")
        testo_font = font.Font(family="Arial", size=14)

        dettagli_frame = tk.Frame(dettagli_window, bg="#f0f0f0")
        dettagli_frame.pack(fill="both", expand=True, padx=20, pady=20)

        titolo_label = tk.Label(dettagli_frame, text=f"Titolo: {self.esercizio.titolo}", font=titolo_font, bg="#f0f0f0")
        titolo_label.pack(pady=15)

        descrizione_label = tk.Label(dettagli_frame, text="Descrizione:", font=titolo_font, bg="#f0f0f0")
        descrizione_label.pack(pady=10)

        descrizione_text = tk.Text(dettagli_frame, height=15, width=80, font=testo_font, bg="#ffffff", fg="#333333")
        descrizione_text.pack(pady=10)
        descrizione_text.insert(tk.END, self.esercizio.descrizione)
        descrizione_text.config(state=tk.DISABLED)
        
        video_url = tk.Label(dettagli_frame, text=f"Video URL: {self.esercizio.video}", fg="blue", cursor="hand2")
        video_url.pack(pady=10)
        video_url.bind("<Button-1>", lambda e: self.apri_url(self.esercizio.video))


        stato_var = tk.IntVar()
        
        stato_corrente = self.esercizio.get_stato()
        print("stato ottenuto")
        
        if stato_corrente == 'completato':
            stato_var.set(1)
        else:
            stato_var.set(0)
            
    
        completato_checkbox = tk.Checkbutton(dettagli_frame, text="Esercizio Completato", variable=stato_var, font=testo_font, bg="#f0f0f0")
        completato_checkbox.pack(pady=20)
        
        aggiorna_stato_button = tk.Button(dettagli_frame, text="Aggiorna Stato", command=lambda: self.paziente.aggiorna_stato_esercizio(self.esercizio, stato_var),
                                        bg="#4CAF50", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        aggiorna_stato_button.pack(pady=15)
        print("chekbox passata")

        back_button = tk.Button(dettagli_frame, text="Torna Indietro", command=dettagli_window.destroy,
                                bg="#f44336", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        back_button.pack(pady=20)
        
    def apri_url(self, url):
        import webbrowser
        webbrowser.open(url)