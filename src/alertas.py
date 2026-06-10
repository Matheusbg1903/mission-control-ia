"""Regras de threshold e alertas do ConnectSat."""

def avaliar(dados):
    """Avalia os dados de telemetria e retorna lista de alertas."""
    alertas = []

    if dados["latencia_uplink_ms"] > 500:
        alertas.append({
            "nivel": "CRITICO",
            "parametro": "latencia_uplink_ms",
            "valor": dados["latencia_uplink_ms"],
            "mensagem": "Latência crítica — conexão degradada para comunidades atendidas.",
            "acao": "Iniciando roteamento alternativo de sinal."
        })
    elif dados["latencia_uplink_ms"] > 300:
        alertas.append({
            "nivel": "ALERTA",
            "parametro": "latencia_uplink_ms",
            "valor": dados["latencia_uplink_ms"],
            "mensagem": "Latência elevada — qualidade de conexão reduzida.",
            "acao": "Monitorar próximos ciclos."
        })

    if dados["throughput_mbps"] < 5.0:
        alertas.append({
            "nivel": "CRITICO",
            "parametro": "throughput_mbps",
            "valor": dados["throughput_mbps"],
            "mensagem": "Throughput crítico — serviços de telemedicina e educação comprometidos.",
            "acao": "Redirecionando carga para feixe reserva."
        })
    elif dados["throughput_mbps"] < 20.0:
        alertas.append({
            "nivel": "ALERTA",
            "parametro": "throughput_mbps",
            "valor": dados["throughput_mbps"],
            "mensagem": "Throughput abaixo do ideal.",
            "acao": "Monitorar próximos ciclos."
        })

    if dados["temperatura_transponder_c"] > 80:
        alertas.append({
            "nivel": "CRITICO",
            "parametro": "temperatura_transponder_c",
            "valor": dados["temperatura_transponder_c"],
            "mensagem": "Temperatura do transponder crítica — risco de falha de hardware.",
            "acao": "Ativando modo de resfriamento emergencial."
        })
    elif dados["temperatura_transponder_c"] > 65:
        alertas.append({
            "nivel": "ALERTA",
            "parametro": "temperatura_transponder_c",
            "valor": dados["temperatura_transponder_c"],
            "mensagem": "Temperatura elevada no transponder.",
            "acao": "Reduzindo carga de processamento."
        })

    if dados["saude_antena_percent"] < 30:
        alertas.append({
            "nivel": "CRITICO",
            "parametro": "saude_antena_percent",
            "valor": dados["saude_antena_percent"],
            "mensagem": "Antena phased-array com falha grave — cobertura comprometida.",
            "acao": "Ativando antena de backup."
        })
    elif dados["saude_antena_percent"] < 60:
        alertas.append({
            "nivel": "ALERTA",
            "parametro": "saude_antena_percent",
            "valor": dados["saude_antena_percent"],
            "mensagem": "Saúde da antena degradada.",
            "acao": "Verificar próximo ciclo de manutenção."
        })

    if dados["energia_disponivel_percent"] < 20:
        alertas.append({
            "nivel": "CRITICO",
            "parametro": "energia_disponivel_percent",
            "valor": dados["energia_disponivel_percent"],
            "mensagem": "Energia crítica — risco de desligamento do satélite.",
            "acao": "Ativando modo economia de energia. Desligando sistemas não essenciais."
        })
    elif dados["energia_disponivel_percent"] < 40:
        alertas.append({
            "nivel": "ALERTA",
            "parametro": "energia_disponivel_percent",
            "valor": dados["energia_disponivel_percent"],
            "mensagem": "Energia abaixo do nível recomendado.",
            "acao": "Reduzindo consumo de sistemas secundários."
        })

    return alertas