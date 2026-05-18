import os
import time
from rich.progress import Progress, SpinnerColumn, TextColumn
from passman.config import console

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading(message: str, duration: float = 1.5):
    with Progress(
        SpinnerColumn(style="cyan"),
        TextColumn(f"[cyan]{message}...[/cyan]"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("", total=100)
        steps = int(duration * 20)
        for _ in range(steps):
            progress.update(task, advance=100 / steps)
            time.sleep(duration / steps)