import json
from datetime import datetime

resposta_api = """
{
    "cidade": "Manaus",
    "pais": "BR",
    "temperatura": {
        "atual": 32.4,
        "minima": 26.1,
        "maxima": 35.8,
        "sensacao": 38.2
    },
    "umidade": 87,
    "condicao": "Parcialmente nublado",
    "vento": { "velocidade_kmh": 12, "direcao": "NE" },
    "atualizado_em": "2025-01-15T14:30:00"
}
"""

dados = json.loads(resposta_api)
temp = dados["temperatura"]
vento = dados["vento"]
atualizado = datetime.fromisoformat(dados["atualizado_em"])

print("=" * 40)
print(f"BOLETIM METEOROLÓGICO - {dados['cidade']}/{dados['pais']}")
print("=" * 40)
print(f"Condição: {dados['condicao']}")
print(f"Temperatura atual: {temp['atual']}°C (sensação de {temp['sensacao']}°C)")
print(f"Mínima: {temp['minima']}°C | Máxima: {temp['maxima']}°C")
print(f"Umidade: {dados['umidade']}%")
print(f"Vento: {vento['velocidade_kmh']} km/h ({vento['direcao']})")
print(f"Atualizado em: {atualizado.strftime('%d/%m/%Y às %H:%M')}")