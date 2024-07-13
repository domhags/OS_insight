import tkinter as tk
from tkinter import ttk, messagebox
from data_collector import DataCollector


class SystemInfoGUI:
    def __init__(self, root):
        # Initialisiert die Benutzeroberfläche
        self.root = root
        self.root.title("System Information")
        self.root.geometry("450x450")

        self.collector = DataCollector()

        # Labels und Checkbuttons für Auswahl der Daten
        ttk.Label(root, text="Wählen Sie die anzuzeigenden Daten aus:").pack()

        self.checkbox_vars = []
        self.data_to_show = ["Timestamp", "Platform", "Python Version", "Machine"]
        for item in self.data_to_show:
            var = tk.IntVar(value=1)
            checkbox = ttk.Checkbutton(root, text=item, variable=var)
            checkbox.pack(anchor="w")
            self.checkbox_vars.append((item, var))

        # Textfeld zur Anzeige der CSV-Daten
        self.text_area = tk.Text(root, wrap="word", height=10, width=60)
        self.text_area.pack()

        # Frame für die Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        # Buttons für verschiedene Aktionen
        ttk.Button(button_frame, text="Daten exportieren (CSV)", command=self.save_button_clicked).pack()
        ttk.Button(button_frame, text="Daten importieren (CSV)", command=self.load_csv_data).pack()
        ttk.Button(button_frame, text="Ausgewählte Werte anzeigen", command=self.show_selected_values).pack()
        ttk.Button(button_frame, text="Textfeld leeren", command=self.clear_text_area).pack()
        ttk.Button(button_frame, text="Beenden", command=self.root.destroy).pack()

    def save_button_clicked(self):
        # Handler für den Klick auf den "Daten exportieren" Button.
        selected_items = [item for item, var in self.checkbox_vars if var.get() == 1]
        if not selected_items:
            messagebox.showwarning("Keine Auswahl", "Bitte wählen Sie mindestens ein Element aus.")
        else:
            selected_data = self.collector.get_selected_info(selected_items)
            result_message = DataCollector.save_data(selected_data)
            if "erfolgreich" in result_message:
                messagebox.showinfo("Daten gespeichert", result_message)
            else:
                messagebox.showerror("Fehler beim Speichern", result_message)

    def load_csv_data(self):
        # Handler für den Klick auf den "Daten importieren" Button.
        data = DataCollector.load_data()
        if isinstance(data, str):  # Fehlermeldung zurückgegeben
            messagebox.showerror("Fehler beim Laden", data)
        else:
            self.clear_text_area()
            for entry in data:
                for key, value in entry.items():
                    self.text_area.insert(tk.END, f"{key}: {value}\n")
                self.text_area.insert(tk.END, "\n")

    def show_selected_values(self):
        # Handler für den Klick auf den "Ausgewählte Werte anzeigen" Button.
        selected_items = [item for item, var in self.checkbox_vars if var.get() == 1]
        if not selected_items:
            messagebox.showwarning("Keine Auswahl", "Bitte wählen Sie mindestens ein Element aus.")
        else:
            selected_data = self.collector.get_selected_info(selected_items)
            self.clear_text_area()
            for key, value in selected_data.items():
                self.text_area.insert(tk.END, f"{key}: {value}\n")

    def clear_text_area(self):
        # Leert das Textfeld.
        self.text_area.delete(1.0, tk.END)
