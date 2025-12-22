from rich.console import Console
from rich.markdown import Markdown
from rich import box
from rich.progress import Progress

data = [2, 5, 3, 7, 9, 6, 4, 8, 5]
console = Console()

# Print title
console.print("Sparkline:", style="bold green")

# Create sparkline using Unicode block characters
spark_chars = "▁▂▃▄▅▆▇█"
max_val = max(data)
min_val = min(data)

sparkline = ""
for val in data:
    index = int((val - min_val) / (max_val - min_val) * (len(spark_chars) - 1))
    sparkline += spark_chars[index]

console.print(sparkline, style="bold cyan")
console.print("Sparkline chart created using rich.py.", style="dim")