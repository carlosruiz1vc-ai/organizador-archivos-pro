import os
import shutil

EXTENSION_MAP = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Instaladores_Programas': ['.exe', '.msi', '.iso', '.zip', '.rar', '.7z'],
    'Audio_Musica': ['.mp3', '.wav', '.flac', '.m4a'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov']
}

def organize_folder(target_folder):
    """Clasifica y mueve archivos de una carpeta a subcarpetas ordenadas."""
    if not os.path.exists(target_folder):
        return False, "La carpeta no existe."

    moved_count = 0
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)
        
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            
            category_found = "Otros"
            for category, extensions in EXTENSION_MAP.items():
                if ext in extensions:
                    category_found = category
                    break
            
            dest_dir = os.path.join(target_folder, category_found)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_dir, item))
            moved_count += 1
            
    return True, f"Se organizaron {moved_count} archivos con éxito."
