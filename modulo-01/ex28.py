def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """Calcula o montante final com juros compostos.

    Args:
        capital (float): Valor inicial investido.
        taxa (float): Taxa de juros por período, em porcentagem (ex.: 5 para 5%).
        periodo (int): Número de períodos.

    Returns:
        float: Montante final após os juros compostos.

    Raises:
        ValueError: Se capital ou taxa forem negativos.

    Example:
        >>> round(calcular_juros_compostos(1000, 10, 2), 2)
        1210.0
    """
    if capital < 0 or taxa < 0:
        raise ValueError("capital e taxa não podem ser negativos")
    return capital * (1 + taxa / 100) ** periodo


print(calcular_juros_compostos(1000, 10, 2))
try:
    calcular_juros_compostos(-1000, 10, 2)
except ValueError as e:
    print(f"Erro: {e}")