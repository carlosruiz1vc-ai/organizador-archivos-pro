import os
from modules.organizer import organize_folder
from modules.duplicates import find_duplicate_files

def main():
    while True:
        print("\n" + "="*50)
        print("   ORGANIZADOR Y LIMPIADOR INTELIGENTE DE ARCHIVOS")
        print("="*50)
        print("1. Clasificar carpeta (Descargas/Escritorio)")
        print("2. Buscar archivos duplicados (Liberar espacio)")
        print("3. Salir")
        
        choice = input("\nSelecciona una opción: ").strip()
        
        if choice == "1":
            folder = input("Ingresa la ruta de la carpeta (ej. C:\\Users\\TuUsuario\\Downloads): ").strip('"')
            success, msg = organize_folder(folder)
            print(f"\n[+] {msg}" if success else f"\n[-] {msg}")
            
        elif choice == "2":
            folder = input("Ingresa la ruta a escanear: ").strip('"')
            print("\n[*] Escaneando archivos duplicados por hash...")
            dups = find_duplicate_files(folder)
            if dups:
                print(f"\n[!] Se encontraron {len(dups)} archivos duplicados:")
                for dup, original in dups:
                    print(f"  -> Duplicado: {os.path.basename(dup)} | Original: {os.path.basename(original)}")
            else:
                print("\n[+] No se encontraron archivos duplicados.")
                
        elif choice == "3":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n[-] Opción no válida.")

if __name__ == "__main__":
    main()

