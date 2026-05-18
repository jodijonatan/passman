from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from passman.config import console

def show_banner():
    banner_text = """
 ██████╗ █████╗  ██████╗██╗    ██╗██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝██║    ██║██╔══██╗██╔════╝
╚█████╗ ███████║██║     ██║    ██║██████╔╝█████╗  
 ╚═══██╗██╔══██║██║     ██║    ██║██╔══██╗██╔══╝  
██████╔╝██║  ██║╚██████╗╚██████╔╝██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
       ██╗    ██╗█████╗ ██╗    ██╗██╗  ████████╗
       ██║    ██║██╔══██╗██║    ██║██║  ╚══██╔══╝
       ██║    ██║███████║██║    ██║██║     ██║  
       ╚██╗  ██╔╝██╔══██║██║    ██║██║     ██║  
        ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║  
         ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  
"""
    console.print(Panel(
        Align.center(
            Text(banner_text, style="bold cyan") +
            Text("\n🔐 Password Manager Modern  v1.0.0\n", style="bold yellow") +
            Text("Kelola password Anda dengan aman & mudah", style="dim white")
        ),
        border_style="cyan",
        padding=(0, 2)
    ))

def show_menu():
    menu_items = [
        ("1", "👁  Lihat Semua Password", "cyan"),
        ("2", "➕  Tambah Password Baru", "green"),
        ("3", "🔍  Cari Password", "yellow"),
        ("4", "🗑  Hapus Password", "red"),
        ("5", "🎲  Generate Password Acak", "magenta"),
        ("6", "📊  Statistik", "blue"),
        ("0", "🚪  Keluar", "white"),
    ]
    menu_text = Text()
    for number, label, color in menu_items:
        menu_text.append(f"  [{number}]", style=f"bold {color}")
        menu_text.append(f"  {label}\n", style="white")
    
    console.print(Panel(
        menu_text,
        title="[bold cyan]📋 MENU UTAMA[/bold cyan]",
        border_style="cyan",
        padding=(1, 3)
    ))