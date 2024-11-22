import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog

class VisualizzaDettagliEsercizio:
    def __init__ (self, esercizio, root, fisioterapista):
        self.esercizio = esercizio
        self.file_video_path = ""
        self.root = root
        self.fisioterapista = fisioterapista
        
        dettagli_window = tk.Toplevel(self.root)
        dettagli_window.title(f"Dettagli Esercizio: {esercizio.titolo}")
        dettagli_window.geometry("1000x800")  

        titolo_font = font.Font(family="Arial", size=14, weight="bold")
        testo_font = font.Font(family="Arial", size=14)

        titolo_label = tk.Label(dettagli_window, text="Titolo:", font=titolo_font, bg="#f0f0f0")
        titolo_label.pack(pady=10)
        titolo_entry = tk.Entry(dettagli_window, font=testo_font, width=60)
        titolo_entry.insert(0, esercizio.titolo)
        titolo_entry.pack(pady=10)

        descrizione_label = tk.Label(dettagli_window, text="Descrizione:", font=titolo_font, bg="#f0f0f0")
        descrizione_label.pack(pady=10)

        descrizione_text = tk.Text(dettagli_window,height=15, width=80, font=testo_font, bg="#ffffff", fg="#333333")
        descrizione_text.pack(pady=10)
        descrizione_text.insert(tk.END, esercizio.descrizione)
        
        video_url_label = tk.Label(dettagli_window, fg="blue", cursor="hand2")
        video_url_label.pack(pady=10)
    
        # Mostra l'URL del video se disponibile
        if esercizio.video:
            video_url_label.config(text=f"Video URL: {esercizio.video}")
            video_url_label.bind("<Button-1>", lambda e: self.apri_url(esercizio.video))
        
        def carica_video():
            video_dialog = tk.Toplevel(dettagli_window)
            video_dialog.title("Inserisci URL Video")
            video_dialog.geometry("500x300")

            dialog_label = tk.Label(video_dialog, text="Inserisci l'URL del video:", font=testo_font)
            dialog_label.pack(pady=10)

            video_url_entry = tk.Entry(video_dialog, font=testo_font, width=60)
            video_url_entry.pack(pady=10)

            def conferma_url():
                nuovo_video_url = video_url_entry.get()
                self.file_video_path = nuovo_video_url
                if nuovo_video_url:
                    video_url_label.config(text=f"Video URL: {nuovo_video_url}")
                    video_url_label.bind("<Button-1>", lambda e: self.apri_url(nuovo_video_url))
                    carica_video_button.pack_forget()  
                    video_dialog.destroy()
        
            conferma_button = tk.Button(video_dialog, text="Conferma", command=conferma_url, bg="#2196F3", fg="white", font=testo_font)
            conferma_button.pack(pady=10)

        carica_video_button = tk.Button(dettagli_window, text="Carica Video", command=carica_video, bg="#2196F3", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        carica_video_button.pack(pady=10)
        
        def salva_modifiche():
            nuovo_titolo = titolo_entry.get()
            nuova_descrizione = descrizione_text.get("1.0", tk.END).strip()  

            if nuovo_titolo != esercizio.titolo or nuova_descrizione != esercizio.descrizione or self.file_video_path != esercizio.video:
                self.fisioterapista.modifica_esercizio(nuovo_titolo, nuova_descrizione, self.file_video_path, esercizio)
                dettagli_window.destroy() 
            else:
                messagebox.showerror("Nessuna modifica da salvare.")

        salva_button = tk.Button(dettagli_window, text="Salva Modifiche", command=salva_modifiche,
                                bg="#4CAF50", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        salva_button.pack(pady=20)

        back_button = tk.Button(dettagli_window, text="Torna Indietro", command=dettagli_window.destroy,
                                bg="#f44336", fg="white", font=testo_font, bd=0, relief="flat", padx=20, pady=10)
        back_button.pack(pady=10)
        
    def apri_url(self, url):
        import webbrowser
        webbrowser.open(url)