import random
import statistics
from typing import Optional


def gerar_lista_aleatoria(tamanho: int, limite: int) -> list[int]:
    """
    Gera uma lista de números inteiros aleatórios.

    Args:
        tamanho: Quantidade de elementos na lista.
        limite: Valor máximo (inclusive) dos números gerados.

    Returns:
        Lista de inteiros aleatórios entre 0 e limite.
    """
    return [random.randint(0, limite) for _ in range(tamanho)]


def calcular_media(lista_numeros: list[float]) -> Optional[float]:
    """
    Calcula a média aritmética dos elementos da lista.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Média dos elementos, ou None se a lista estiver vazia.
    """
    if not lista_numeros:
        return None
    return statistics.mean(lista_numeros)


def calcular_mediana(lista_numeros: list[float]) -> Optional[float]:
    """
    Calcula a mediana dos elementos da lista.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Mediana dos elementos, ou None se a lista estiver vazia.
    """
    if not lista_numeros:
        return None
    return statistics.median(lista_numeros)


def calcular_moda(lista_numeros: list[float]) -> Optional[float]:
    """
    Calcula a moda dos elementos da lista.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Moda dos elementos, ou None se a lista estiver vazia.
    """
    if not lista_numeros:
        return None
    return statistics.mode(lista_numeros)


def encontrar_maximo(lista_numeros: list[float]) -> Optional[float]:
    """
    Encontra o maior valor da lista.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Maior elemento, ou None se a lista estiver vazia.
    """
    if not lista_numeros:
        return None
    return max(lista_numeros)


def encontrar_minimo(lista_numeros: list[float]) -> Optional[float]:
    """
    Encontra o menor valor da lista.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Menor elemento, ou None se a lista estiver vazia.
    """
    if not lista_numeros:
        return None
    return min(lista_numeros)


def ordenar_lista(lista_numeros: list[float]) -> list[float]:
    """
    Retorna uma nova lista com os elementos ordenados em ordem crescente.

    Args:
        lista_numeros: Lista de números.

    Returns:
        Nova lista ordenada (a original não é modificada).
    """
    return sorted(lista_numeros)


if __name__ == "__main__":
    tamanho = int(input("Informe o tamanho da lista (padrão 10): ") or 10)
    limite = int(input("Informe o limite máximo dos números (padrão 100): ") or 100)

    numeros = gerar_lista_aleatoria(tamanho, limite)

    print(f"\nLista gerada:    {numeros}")
    print(f"Lista ordenada:  {ordenar_lista(numeros)}")
    print(f"Média:           {calcular_media(numeros):.2f}")
    print(f"Mediana:         {calcular_mediana(numeros)}")
    print(f"Moda:            {calcular_moda(numeros)}")
    print(f"Máximo:          {encontrar_maximo(numeros)}")
    print(f"Mínimo:          {encontrar_minimo(numeros)}")
