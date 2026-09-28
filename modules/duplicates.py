import hashlib
import os

def get_file_hash(file_path):
    """Calcula el hash SHA256 de un archivo para comparar integridad exacta."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def find_duplicate_files(target_folder):
    """Busca y agrupa archivos duplicados basándose en su contenido hash."""
    hashes = {}
    duplicates = []
    
    for root, _, files in os.walk(target_folder):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = get_file_hash(full_path)
            if file_hash:
                if file_hash in hashes:
                    duplicates.append((full_path, hashes[file_hash]))
                else:
                    hashes[file_hash] = full_path
    return duplicates
