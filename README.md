# Mission Control AI — ConnectSat

Sistema de monitoramento operacional do satélite ConnectSat, desenvolvido para a Global Solution 2026.1 da FIAP. O sistema simula telemetria em tempo real, detecta anomalias via lógica Python e usa IA generativa para analisar o estado da missão em linguagem natural, conectando cada alerta técnico ao impacto nas comunidades atendidas na Terra.

---

## Integrantes

|       Nome     |   RM   | Turma |
|----------------|--------|-------|
| Matheus Borges | 574085 | 1CCR  |
| Murilo Ignacio | 573621 | 1CCR  | 
| Ryan Luther    | 572993 | 1CCR  |

---

## Sobre o projeto

O ConnectSat é um satélite de telecomunicações em órbita baixa (LEO) responsável por levar internet a escolas rurais, postos de saúde isolados e comunidades ribeirinhas no Brasil. O Mission Control AI monitora cinco parâmetros de telemetria e usa o modelo `gpt-oss:120b` via Ollama Cloud para interpretar anomalias e recomendar ações corretivas, sempre articulando o problema técnico com o impacto nas comunidades atendidas.

### O que o sistema faz

- Gera dados simulados de telemetria a cada consulta
- Detecta anomalias automaticamente via regras de threshold implementadas em Python
- Injeta os dados no modelo de linguagem via Ollama Cloud
- Exibe diagnóstico, impacto terrestre e ações recomendadas em linguagem natural
- Interface CLI com banner ASCII, painéis formatados e prompt editável

---

## Persona atendida

**NOC Engineer** — engenheiro de operações responsável por monitorar a saúde do satélite e tomar decisões rápidas para manter o serviço de conectividade ativo. O sistema traduz dados técnicos em diagnósticos compreensíveis, permitindo respostas ágeis mesmo em situações de crise.

---

## Parâmetros monitorados

|           Parâmetro             |      Normal      |    Alerta    |     Crítico      |
|---------------------------------|------------------|--------------|------------------|
| Latência uplink (ms)            | menor que 300 ms | 300 a 500 ms | acima de 500 ms  |
| Throughput (Mbps)               | acima de 20 Mbps | 5 a 20 Mbps  | abaixo de 5 Mbps |
| Temperatura do transponder (°C) | abaixo de 65°C   | 65 a 80°C    | acima de 80°C    |
| Saúde da antena (%)             | acima de 60%     | 30 a 60%     | abaixo de 30%    |
| Energia disponível (%)          | acima de 40%     | 20 a 40%     | abaixo de 20%    |

---

## Tecnologias utilizadas

- Python 3.10+
- Ollama Cloud API — modelo `gpt-oss:120b`
- ollama 0.6.2
- python-dotenv 1.2.2
- rich 15.0.0
- prompt-toolkit 3.0.52
- pyfiglet 1.0.4

---

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/Matheusbg1903/mission-control-ia.git
cd mission-control-ia
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure a API Key**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
OLLAMA_API_KEY=sua_chave_aqui
```
Crie sua chave gratuita em https://ollama.com

**4. Execute o sistema**
```bash
python main.py
```

### Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `/status` | Exibe a telemetria atual do satélite |
| `/help` | Lista os comandos disponíveis |
| `/about` | Informações sobre o sistema |
| `/clear` | Limpa a tela |
| `/exit` | Encerra o sistema |

---

## Demonstração

![Interface inicial do sistema](assets/screenshot_banner.png)

![IA analisando dados de telemetria](assets/screenshot_analise.png)

---

## System Prompt

O system prompt completo está em `prompts/system_prompt.md`. O modelo é instruído a sempre estruturar as respostas em três seções: diagnóstico técnico, impacto terrestre e ação recomendada.

---

## Cenários de teste

1. Operação normal — todos os parâmetros dentro do range esperado
2. Latência crítica — conexão degradada, comunidades sem acesso estável
3. Temperatura crítica do transponder — risco de falha de hardware
4. Throughput reduzido — aulas e telemedicina comprometidas
5. Energia baixa — ativação do modo economia de energia
6. Antena degradada — risco de perda de cobertura regional

---

## Limitações conhecidas

- Os dados de telemetria são gerados aleatoriamente a cada consulta, sem persistência de histórico entre sessões
- O sistema não mantém memória de contexto entre perguntas consecutivas
- A simulação não replica parâmetros físicos reais de satélites LEO com precisão científica
- A disponibilidade do serviço depende do plano gratuito da Ollama Cloud

---

## Proposta de valor e modelo de negócio

**Problema terrestre**
Mais de 5 milhões de brasileiros em áreas rurais e ribeirinhas não têm acesso à internet via fibra ou rádio. Sem conectividade, escolas não conseguem ofertar ensino híbrido, postos de saúde não realizam teleconsultas e pequenos negócios ficam fora da economia digital. O ConnectSat resolve esse problema levando banda larga via satélite LEO a regiões onde nenhuma outra infraestrutura chega.

**Quem paga pela solução**
Modelo híbrido: o setor público, por meio de programas como Conecta Escola e Telessaúde, financia a conectividade para escolas e postos de saúde. O setor privado, incluindo operadoras regionais, cooperativas agrícolas e empresas de logística, paga por planos de acesso comercial.

**Métrica de impacto**
Com o ConnectSat operando com saúde plena por um ano, aproximadamente 800 escolas rurais mantêm aulas online sem interrupção, cerca de 200 postos de saúde realizam teleconsultas diariamente e em torno de 50.000 pessoas em comunidades ribeirinhas têm acesso contínuo a serviços digitais essenciais.

**Modelo de negócio**
Dado-como-serviço combinado com SaaS: a operadora cobra por banda consumida para clientes privados e fecha contratos públicos por disponibilidade de serviço com SLA de uptime garantido. O Mission Control AI é o sistema interno que assegura o cumprimento desses SLAs, reduzindo o tempo de resposta a incidentes e evitando penalidades contratuais.

---

## Video de demonstracao

Link: https://youtu.be/aSN01p6lcLc

Configurado como "Nao listado" no YouTube.

---

## Estrutura do projeto

```
mission-control-ia/
├── main.py
├── banner_ascii.py
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── ui.py
│   ├── engine.py
│   ├── telemetria.py
│   └── alertas.py
├── prompts/
│   └── system_prompt.md
├── data/
│   └── cenarios.json
└── assets/
    ├── screenshot_banner.png
    └── screenshot_analise.png
```

---

FIAP · Ciencia da Computacao · Global Solution 2026.1 · Disciplina: Prompt Engineering and Artificial Intelligence