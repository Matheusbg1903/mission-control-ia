"""Interface CLI estilo Claude Code — usa Rich + prompt-toolkit."""
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))

def show_banner():
    """Exibe banner ASCII colorido no início."""
    banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
    console.print(Text(banner, style="bold #06B6D4"))
    console.print(Panel.fit(
        "Sistema de monitoramento do satélite ConnectSat.\n"
        "Use /help para ver os comandos · /exit para sair.\n"
        "Modelo: gpt-oss:120b via Ollama Cloud",
        title="◆ CONNECTSAT MISSION CONTROL",
        border_style="#06B6D4"
    ))

def show_response(text):
    """Renderiza resposta da IA em painel com timestamp."""
    now = datetime.now().strftime("%H:%M")
    console.print(Panel(text, title="◆ Mission Control AI",
                        subtitle=now, border_style="#06B6D4"))

def run_cli(engine):
    """Loop principal da CLI."""
    show_banner()

    if not engine.is_ready():
        console.print("⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n", style="yellow")

    while True:
        try:
            user_input = session.prompt("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not user_input:
            continue

        if user_input == "/exit":
            console.print("Encerrando Mission Control AI. Até logo!", style="#06B6D4")
            break

        if user_input == "/help":
            console.print(Panel(
                "/help    → mostra os comandos disponíveis\n"
                "/status  → exibe telemetria atual do satélite\n"
                "/about   → informações sobre o sistema\n"
                "/clear   → limpa a tela\n"
                "/exit    → encerra o sistema",
                title="◆ Comandos disponíveis",
                border_style="#06B6D4"
            ))
            continue

        if user_input == "/status":
            show_response(engine.status_snapshot())
            continue

        if user_input == "/about":
            show_response(
                "Mission Control AI — ConnectSat\n"
                "Trilha: Conectividade Rural\n"
                "Disciplina: Prompt Engineering and AI — FIAP 2026.1\n"
                "Stack: Python + Ollama Cloud (gpt-oss:120b) + Rich + prompt-toolkit"
            )
            continue

        if user_input == "/clear":
            console.clear()
            show_banner()
            continue

        # Qualquer outra entrada vai para o motor de análise
        console.print("⏳ Analisando...", style="yellow")
        resposta = engine.analyze(user_input)
        show_response(resposta)