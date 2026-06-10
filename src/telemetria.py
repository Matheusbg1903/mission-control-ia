"""Simulação de telemetria do satélite ConnectSat"""
import random

def coletar():
    """Gera dados simulados de telemetria do satélite"""
    return {
        "latencia_uplink_ms": round(random.uniform(20, 800), 1),
        "throughput_mbps": round(random.uniform(0.5, 100.0), 1),
        "temperatura_transponder_c": round(random.uniform(15, 95), 1),
        "saude_antena_percent": round(random.uniform(10, 100), 1),
        "energia_disponivel_percent": round(random.uniform(5, 100), 1), 
    }
