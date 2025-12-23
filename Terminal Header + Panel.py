from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Initialize console
console = Console()

# Create a table
table = Table(title="Top Languages")
table.add_column("Language", style="bold magenta")
table.add_column("Score", style="bold yellow")

# Add rows
table.add_row("Python", "10/10")
table.add_row("JavaScript", "9/10")
table.add_row("Go", "8/10")

# Print dashboard title and table
console.print(Panel("[bold cyan]# DASHBOARD[/bold cyan]", border_style="green"))
console.print(Panel(table, border_style="yellow"))
