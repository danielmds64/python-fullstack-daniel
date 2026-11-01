from typing import Callable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """Aplica uma função a cada elemento de uma lista.

    Args:
        dados (List[T]): Lista de entrada.
        funcao (Callable[[T], R]): Função aplicada a cada elemento.

    Returns:
        List[R]: Lista com os resultados da transformação.

    Example:
        >>> aplicar_transformacao(["a", "b"], str.upper)
        ['A', 'B']
    """
    return [funcao(item) for item in dados]


print(aplicar_transformacao(["python", "json", "typing"], str.upper))
print(aplicar_transformacao([3.14159, 2.71828, 1.41421], lambda x: round(x, 2)))

pessoas = [{"nome": "Ana", "idade": 25}, {"nome": "Bruno", "idade": 30}, {"nome": "Carla", "idade": 28}]
print(aplicar_transformacao(pessoas, lambda d: d["nome"]))