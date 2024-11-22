import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog

class CartellaClinicaFisio:
    def __init__(self, root, paziente, fisioterapista):
        self.root = root
        self.paziente = paziente
        self.fisioterapista = fisioterapista

        cartella_window = tk.Toplevel(self.root)
        cartella_window.title("Cartella Clinica")
        cartella_window.geometry("900x700")
        cartella_clinica = self.paziente.get_cartella_clinica()

        if cartella_clinica:
            cartella_info = f"{cartella_clinica.descrizione}"
            informazioni_label = ttk.Label(cartella_window, text="Cartella Clinica del Paziente" + f"{paziente.nome}", font=("Arial", 14))
            informazioni_label.pack(pady=10)
        else:
            cartella_info = "Il paziente non ha ancora una cartella clinica."
            informazioni_label = ttk.Label(cartella_window, text="Cartella Clinica del Paziente" + f"{paziente.nome}", font=("Arial", 14))
            informazioni_label.pack(pady=10)

        descrizione_label = ttk.Label(cartella_window, text="Descrizione", font=("Arial", 14))
        descrizione_label.pack(pady=2)

        info_text = tk.Text(cartella_window, wrap='word', height=20, width=70, font=("Arial", 12))
        info_text.pack(pady=10)

        info_text.insert(tk.END, cartella_info)
        

        def salva_modifiche(flag):
            testo_modificato = info_text.get("1.0", tk.END).strip()  
            
            if flag == 1:
                try:
                    self.fisioterapista.aggiungi_cartella_clinica(paziente, testo_modificato)
                    cartella_window.destroy

                except Exception as e:
                    messagebox.showerror("Errore", f"Si è verificato un errore durante l'esecuzione: {e}")
            else:
                if not testo_modificato:
                    messagebox.showwarning("Attenzione", "Nessun testo da salvare.")
                    return
                try:
                    self.fisioterapista.modifica_cartella_clinica(cartella_clinica, testo_modificato)  
                    messagebox.showinfo("Successo", "Modifiche salvate con successo!")
                    cartella_window.destroy
                except Exception as e:
                    messagebox.showerror("Errore", f"Si è verificato un errore durante il salvataggio: {e}")

        if cartella_clinica:
            salva_button = ttk.Button(cartella_window, text="Salva Modifiche", command=lambda: salva_modifiche(0), style='TButton')
            salva_button.pack(pady=20, ipadx=20, ipady=10)
        else:
            aggiungi_button = ttk.Button(cartella_window, text="Aggiungi cartella clinica", command=lambda: salva_modifiche(1), style='TButton')
            aggiungi_button.pack(pady=20, ipadx=20, ipady=10)
            
        indietro_button = ttk.Button(cartella_window, text="Torna indietro", command=cartella_window.destroy, style='TButton')
        indietro_button.pack(pady=20, ipadx=20, ipady=10)