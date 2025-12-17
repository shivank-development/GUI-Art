from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Top Movies 2025")

table.add_column("Rank", justify="right", style="cyan")
table.add_column("Movie", style="magenta")
table.add_column("Rating", justify="right", style="green")

table.add_row("1", "Interstellar 2", "9.3")
table.add_row("2", "The Quantum Realm", "8.7")
table.add_row("3", "AI Uprising", "8.4")

console.print(table)
