import tkinter as tk
from gui import SystemInfoGUI


def main():
    # Hauptfunktion zum Starten der Anwendung.
    root = tk.Tk()
    app = SystemInfoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
