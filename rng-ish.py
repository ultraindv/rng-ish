import random
import sys
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def set_terminal_title(title):
    # \x1b]2; is the start of the escape sequence for the title
    # \x07 is the end (BEL character)
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()

set_terminal_title("rng-ish")

while True:
    rng = random.randint(1, 100)

    os.system("clear")

    rnoutput = Text(f"{rng}", style="bold #add8e6", justify="center")
    console.print(Panel(rnoutput, border_style="#00008B"))
    
    console.print("Press Enter To Roll", style="bold #add8e6")
    console.print("To Exit, the program. [bold red]Press 2[/bold red]")

    rinput = input("[?]: ")
    if rinput == "":
        os.system("clear")

    elif rinput == "2":
        os.system("clear")
        sys.exit()

    else:
        os.system("clear")
