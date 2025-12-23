from rich import print
import pyfiglet
import datetime

print(f"[yellow]{pyfiglet.figlet_format('Happy Thanksgiving')}[/yellow]")

name = input("Your name: ")
year = datetime.datetime.now().year

print(f"\n[bold green]Welcome, {name}![/bold green]")
print("[cyan]Gratitude + Growth + Code[/cyan]\n")

for f in [
    "Python powers AI, Web & Data",
    "Every expert was once a beginner",
    "Small practice daily = Big success"
]:
    print(f"[yellow]{f}[/yellow]")

print(f"\n[bold white]Thank you for coding in {year}![/bold white]")
print("[bold red]- Powered by CLCODING[/bold red]")
