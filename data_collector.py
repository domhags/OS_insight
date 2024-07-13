import platform
import sys
import csv
from datetime import datetime


class DataCollector:
    def __init__(self):
        # Initialisiert die Attribute für Plattforminformationen, Python-Version und Zeitstempel.
        self.platform_info = platform.platform()
        self.python_version = sys.version
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.machine = platform.machine()

    def get_platform_info(self):
        # Gibt die gesammelten Plattforminformationen zurück.
        return self.platform_info

    def get_python_version(self):
        # Gibt die gesammelte Python-Version zurück.
        return self.python_version

    def get_machine(self):
        # Gibt die gesammelte Maschineninformation zurück.
        return self.machine

    def get_timestamp(self):
        # Gibt den gesammelten Zeitstempel zurück.
        return self.timestamp

    def get_selected_info(self, selected_items):
        # Gibt eine Sammlung der gesammelten Informationen zurück.
        info = {
            "Timestamp": self.get_timestamp(),
            "Platform": self.get_platform_info(),
            "Python Version": self.get_python_version(),
            "Machine": self.get_machine()
        }
        return {key: info[key] for key in selected_items}

    @staticmethod
    def save_data(data):
        # Speichert die bereitgestellten Daten in einer CSV-Datei.
        try:
            with open("system_info.csv", "a", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data.keys())

                # Schreibt die Kopfzeile, falls die Datei leer ist
                if csvfile.tell() == 0:
                    writer.writeheader()

                writer.writerow(data)
            return "Daten wurden erfolgreich in system_info.csv gespeichert."
        except Exception as e:
            return f"Fehler beim Speichern: {str(e)}"

    @staticmethod
    def load_data():
        # Lädt Daten aus der system_info.csv-Datei
        try:
            with open("system_info.csv", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader if any(row.values())]
            return data
        except FileNotFoundError:
            return f"Fehler. Datei system_info.csv nicht gefunden"
        except Exception as e:
            return f"Fehler beim Laden: {str(e)}"
