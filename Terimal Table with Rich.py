from rich.console import Console
from rich.table import Table

console = Console()

# Create a table with a title
table = Table(title="Fruits")

# Add columns
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Qty", style="magenta")

# Add rows
table.add_row("Apple", "10")
table.add_row("Banana", "20")
table.add_row("Mango", "15")

# Print the table
console.print(table)
