import os
import json
from passman.config import DATA_FILE, console

def load_data() -> dict:
    if not os.path.exists(DATA_FILE):
        return {"master_hash": None, "passwords": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        console.print("[red]⚠ File data rusak! Membuat data baru...[/red]")
        return {"master_hash": None, "passwords": []}

def save_data(data: dict) -> bool:
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        console.print(f"[red]✗ Gagal menyimpan data: {e}[/red]")
        return False