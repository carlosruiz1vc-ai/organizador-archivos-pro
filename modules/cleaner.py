import os
import shutil
import tempfile
import psutil

def get_system_status():
    """Obtiene el estado del disco principal y la memoria RAM."""
    disk = psutil.disk_usage('/')
    ram = psutil.virtual_memory()
    
    return {
        "disk_total_gb": round(disk.total / (1024**3), 1),
        "disk_free_gb": round(disk.free / (1024**3), 1),
        "disk_percent": disk.percent,
        "ram_percent": ram.percent,
        "ram_used_gb": round(ram.used / (1024**3), 1),
        "ram_total_gb": round(ram.total / (1024**3), 1)
    }

def clean_temp_files():
    """Limpia los archivos temporales del usuario actual."""
    temp_dir = tempfile.gettempdir()
    deleted_files = 0
    freed_bytes = 0

    for root, _, files in os.walk(temp_dir):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                os.remove(file_path)
                deleted_files += 1
                freed_bytes += size
            except Exception:
                continue

    freed_mb = round(freed_bytes / (1024**2), 2)
    return deleted_files, freed_mb
