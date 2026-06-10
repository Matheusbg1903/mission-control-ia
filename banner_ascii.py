"""Gerador de banner ASCII — Mission Control AI."""
import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text
import argparse

console = Console()

def show_banner(font="ansi_shadow"):
    linha1 = pyfiglet.figlet_format("Global Solution", font=font)
    linha2 = pyfiglet.figlet_format("Mission Control AI", font=font)
    console.print(Align.center(Text(linha1, style="bold #A855F7")))
    console.print(Align.center(Text(linha2, style="bold #06B6D4")))
    console.print(Align.center(
        Text("── 2026.1 · Prompt Engineering and AI · FIAP ──",
             style="italic #8484A0")
    ))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-font", default="ansi_shadow")
    parser.add_argument("-text", default=None)
    parser.add_argument("-fonts", action="store_true")
    parser.add_argument("-demo", action="store_true")
    args = parser.parse_args()

    if args.fonts:
        for f in pyfiglet.FigletFont.getFonts():
            print(f)
    elif args.demo:
        for f in ["ansi_shadow", "slant", "big", "banner3", "block", "colossal", "doom", "epic"]:
            console.print(f"\n[bold yellow]Font: {f}[/bold yellow]")
            show_banner(font=f)
    elif args.text:
        console.print(Text(pyfiglet.figlet_format(args.text, font=args.font), style="bold #06B6D4"))
    else:
        show_banner(font=args.font)