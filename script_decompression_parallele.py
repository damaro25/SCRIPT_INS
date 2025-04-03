import zipfile
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Dossier de sortie
output_dir = Path("dictionnaires")
output_dir.mkdir(exist_ok=True)

# Fichiers ZIP à traiter
backup_files = [f for f in os.listdir() if f.startswith("backup") and f.endswith(".zip")]

def process_backup(backup):
    backup_stem = Path(backup).stem
    print(f"📦 Traitement de {backup}...")

    with zipfile.ZipFile(backup, 'r') as zip_ref:
        inner_zips = [f for f in zip_ref.namelist() if f.endswith("Data.zip") or f.endswith("Input.zip")]

        for inner_zip_name in inner_zips:
            print(f"  ➤ Extraction de {inner_zip_name}")
            extracted_path = Path("temp_extraction") / backup_stem
            extracted_path.mkdir(parents=True, exist_ok=True)

            zip_ref.extract(inner_zip_name, extracted_path)
            inner_zip_path = extracted_path / inner_zip_name

            with zipfile.ZipFile(inner_zip_path, 'r') as inner_zip:
                for file in inner_zip.namelist():
                    if file.endswith(".csdb"):
                        base_name = Path(file).stem
                        ext = Path(file).suffix
                        new_name = f"{base_name}_{backup_stem}{ext}"
                        print(f"    ↳ Fichier extrait : {new_name}")
                        with inner_zip.open(file) as source, open(output_dir / new_name, "wb") as target:
                            target.write(source.read())

            inner_zip_path.unlink()

        try:
            extracted_path.rmdir()
        except OSError:
            pass  # Si le dossier n'est pas vide

# ⚙️ Lancement parallèle avec 4 threads (modifiable selon la puissance de ton PC)
with ThreadPoolExecutor(max_workers=6) as executor:
    executor.map(process_backup, backup_files)