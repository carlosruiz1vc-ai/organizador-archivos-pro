import os
import tkinter as tk
from tkinter import ttk, messagebox
from modules.organizer import organize_folder
from modules.cleaner import get_system_status, clean_temp_files

class EasyAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente Fácil del Sistema")
        self.root.geometry("550x420")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        # Título principal
        title_label = ttk.Label(root, text="💡 Asistente y Limpiador de PC", font=("Segoe UI", 14, "bold"))
        title_label.pack(pady=15)

        # Panel de Estado del Sistema
        status_frame = ttk.LabelFrame(root, text=" Estado de tu Equipo ")
        status_frame.pack(fill="x", padx=20, pady=5)

        self.lbl_ram = ttk.Label(status_frame, text="Memoria RAM: Cargando...", font=("Segoe UI", 10))
        self.lbl_ram.pack(anchor="w", padx=10, pady=4)

        self.lbl_disk = ttk.Label(status_frame, text="Disco Principal: Cargando...", font=("Segoe UI", 10))
        self.lbl_disk.pack(anchor="w", padx=10, pady=4)

        # Panel de Acciones Sencillas
        actions_frame = ttk.LabelFrame(root, text=" Soluciones Rápidas ")
        actions_frame.pack(fill="x", padx=20, pady=15)

        btn_clean = ttk.Button(actions_frame, text="🧹 Limpiar Archivos Basura", command=self.run_cleaner)
        btn_clean.pack(fill="x", padx=10, pady=6)

        btn_organize = ttk.Button(actions_frame, text="📁 Organizar Mi Carpeta de Descargas", command=self.run_organizer)
        btn_organize.pack(fill="x", padx=10, pady=6)

        # Barra de estado inferior
        self.lbl_status = ttk.Label(root, text="Listo para ayudar.", font=("Segoe UI", 9, "italic"))
        self.lbl_status.pack(side="bottom", pady=10)

        self.update_system_info()

    def update_system_info(self):
        try:
            info = get_system_status()
            self.lbl_ram.config(text=f"Memoria RAM: {info['ram_percent']}% en uso ({info['ram_used_gb']} GB / {info['ram_total_gb']} GB)")
            self.lbl_disk.config(text=f"Disco Principal: {info['disk_free_gb']} GB libres de {info['disk_total_gb']} GB ({info['disk_percent']}% lleno)")
        except Exception:
            self.lbl_ram.config(text="Memoria RAM: No disponible")

    def run_cleaner(self):
        self.lbl_status.config(text="Limpiando archivos temporales...")
        self.root.update()
        count, freed_mb = clean_temp_files()
        self.update_system_info()
        messagebox.showinfo("Limpieza Completada", f"Se eliminaron {count} archivos basura.\nSe liberaron {freed_mb} MB de espacio.")
        self.lbl_status.config(text="Limpieza realizada con éxito.")

    def run_organizer(self):
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        if os.path.exists(downloads_path):
            success, msg = organize_folder(downloads_path)
            if success:
                messagebox.showinfo("Éxito", f"Carpeta de Descargas organizada.\n{msg}")
            else:
                messagebox.showerror("Error", msg)
        else:
            messagebox.showwarning("Atención", "No se encontró la carpeta de Descargas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EasyAssistantApp(root)
    root.mainloop()
