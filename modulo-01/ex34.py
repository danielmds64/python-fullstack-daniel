import json
from typing import Any


config_inicial = {
    "app": {"nome": "MeuApp", "versao": "1.0.0", "debug": False},
    "banco": {"host": "localhost", "porta": 5432, "usuario": "admin", "nome": "meu_banco"},
    "email": {"servidor": "smtp.exemplo.com", "porta": 587, "remetente": "no-reply@exemplo.com"},
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config_inicial, f, indent=2, ensure_ascii=False)


def carregar_config(caminho: str) -> dict:
    """Carrega um arquivo de configuração JSON.

    Args:
        caminho (str): Caminho do arquivo config.json.

    Returns:
        dict: Configurações carregadas.

    Example:
        >>> carregar_config("config.json")["app"]["versao"]
        '1.0.0'
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def obter_valor(config: dict, chave: str, padrao: Any = None) -> Any:
    """Obtém um valor aninhado usando notação de ponto.

    Args:
        config (dict): Dicionário de configuração.
        chave (str): Chave com notação de ponto (ex.: "app.versao").
        padrao (Any): Valor retornado se a chave não existir. Padrão: None.

    Returns:
        Any: Valor encontrado ou o valor padrão.

    Example:
        >>> obter_valor({"app": {"versao": "1.0.0"}}, "app.versao")
        '1.0.0'
    """
    atual: Any = config
    for parte in chave.split("."):
        if isinstance(atual, dict) and parte in atual:
            atual = atual[parte]
        else:
            return padrao
    return atual


config = carregar_config("config.json")

print(obter_valor(config, "app.versao"))
print(obter_valor(config, "banco.porta"))
print(obter_valor(config, "email.servidor"))
print(obter_valor(config, "app.debug"))
print(obter_valor(config, "banco.senha", "não definida"))