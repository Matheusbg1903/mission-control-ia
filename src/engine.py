"""Motor de análise da Mission Control AI."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "connectsat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de monitoramento de satélites."

class MissionEngine:
    """Motor de análise do ConnectSat."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):
        return True

    def status_snapshot(self):
        """Retorna resumo do estado atual da telemetria."""
        dados = coletar()
        alertas = avaliar(dados)

        linhas = ["📡 STATUS ATUAL DO CONNECTSAT\n"]
        linhas.append(f"  Latência uplink:        {dados['latencia_uplink_ms']} ms")
        linhas.append(f"  Throughput:             {dados['throughput_mbps']} Mbps")
        linhas.append(f"  Temperatura transponder:{dados['temperatura_transponder_c']} °C")
        linhas.append(f"  Saúde da antena:        {dados['saude_antena_percent']} %")
        linhas.append(f"  Energia disponível:     {dados['energia_disponivel_percent']} %")

        if alertas:
            linhas.append("\n⚠️ ALERTAS ATIVOS:")
            for a in alertas:
                linhas.append(f"  [{a['nivel']}] {a['mensagem']}")
                linhas.append(f"  → {a['acao']}")
        else:
            linhas.append("\n✅ Todos os parâmetros dentro do normal.")

        return "\n".join(linhas)

    def analyze(self, pergunta_usuario):
        """Analisa a pergunta com base na telemetria + alertas + IA."""
        dados = coletar()
        alertas = avaliar(dados)

        alertas_texto = ""
        if alertas:
            for a in alertas:
                alertas_texto += f"- [{a['nivel']}] {a['parametro']}: {a['valor']} — {a['mensagem']} Ação: {a['acao']}\n"
        else:
            alertas_texto = "Nenhum alerta ativo. Todos os parâmetros dentro do normal."

        prompt = f"""
Dados de telemetria coletados agora:
- Latência uplink: {dados['latencia_uplink_ms']} ms
- Throughput: {dados['throughput_mbps']} Mbps
- Temperatura do transponder: {dados['temperatura_transponder_c']} °C
- Saúde da antena: {dados['saude_antena_percent']} %
- Energia disponível: {dados['energia_disponivel_percent']} %

Alertas detectados:
{alertas_texto}

Pergunta do operador: {pergunta_usuario}
"""
        return llm(prompt, system=self.system_prompt)