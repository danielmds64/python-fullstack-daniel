import json
import os
from datetime import datetime
from typing import Any, Dict, List


def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Registra um evento de log em um arquivo JSON.

    Args:
        arquivo (str): Caminho do arquivo de log.
        nivel (str): Nível do evento (INFO, WARNING ou ERROR).
        mensagem (str): Texto do evento.

    Returns:
        None

    Example:
        >>> registrar_evento("app_log.json", "INFO", "Sistema iniciado")
    """
    logs = ler_logs(arquivo)
    logs.append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "nivel": nivel.upper(),
        "mensagem": mensagem,
    })
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def ler_logs(arquivo: str) -> List[Dict[str, Any]]:
    """Lê todos os eventos de um arquivo de log JSON.

    Args:
        arquivo (str): Caminho do arquivo de log.

    Returns:
        list: Lista de eventos, vazia se o arquivo não existir.

    Example:
        >>> ler_logs("inexistente.json")
        []
    """
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def filtrar_por_nivel(logs: List[Dict[str, Any]], nivel: str) -> List[Dict[str, Any]]:
    """Filtra eventos de log por nível.

    Args:
        logs (list): Lista de eventos.
        nivel (str): Nível desejado (INFO, WARNING ou ERROR).

    Returns:
        list: Eventos do nível informado.

    Example:
        >>> filtrar_por_nivel([{"nivel": "INFO"}, {"nivel": "ERROR"}], "ERROR")
        [{'nivel': 'ERROR'}]
    """
    return [log for log in logs if log["nivel"] == nivel.upper()]


ARQUIVO = "app_log.json"
if os.path.exists(ARQUIVO):
    os.remove(ARQUIVO)

registrar_evento(ARQUIVO, "INFO", "Sistema iniciado")
registrar_evento(ARQUIVO, "INFO", "Usuário autenticado")
registrar_evento(ARQUIVO, "WARNING", "Uso de memória acima de 80%")
registrar_evento(ARQUIVO, "ERROR", "Falha ao conectar ao banco de dados")
registrar_evento(ARQUIVO, "ERROR", "Timeout na requisição externa")
registrar_evento(ARQUIVO, "INFO", "Backup concluído")

logs = ler_logs(ARQUIVO)
print(f"Total de eventos: {len(logs)}")

for nivel in ("INFO", "WARNING", "ERROR"):
    filtrados = filtrar_por_nivel(logs, nivel)
    print(f"\n{nivel} ({len(filtrados)}):")
    for log in filtrados:
        print(f"  [{log['timestamp']}] {log['mensagem']}")