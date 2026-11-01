def converter_moeda(valor_brl: float) -> tuple[float, float]:
    """Converte um valor em reais para dólar e euro.

    Args:
        valor_brl (float): Valor em reais (BRL).

    Returns:
        tuple[float, float]: Tupla (valor_usd, valor_eur).

    Example:
        >>> converter_moeda(515.0)
        (100.0, 92.29)
    """
    valor_usd = round(valor_brl / 5.15, 2)
    valor_eur = round(valor_brl / 5.58, 2)
    return valor_usd, valor_eur

usd, eur = converter_moeda(515.0)
print(f"USD: {usd} | EUR: {eur}")