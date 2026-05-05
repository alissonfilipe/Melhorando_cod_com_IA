import random
import statistics
import time
import sys

# ─────────────────────────────────────────────
# IMPLEMENTAÇÕES ORIGINAIS
# ─────────────────────────────────────────────

def calcular_media_original(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    return soma / len(lista_numeros)

def encontrar_maximo_original(lista_numeros):
    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
    return maximo

def encontrar_minimo_original(lista_numeros):
    minimo = lista_numeros[0]
    for numero in lista_numeros:
        if numero < minimo:
            minimo = numero
    return minimo

def ordenar_lista_original(lista_numeros):
    lista = lista_numeros[:]
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# ─────────────────────────────────────────────
# IMPLEMENTAÇÕES OTIMIZADAS
# ─────────────────────────────────────────────

def calcular_media_otimizada(lista_numeros):
    if not lista_numeros:
        return None
    return statistics.mean(lista_numeros)

def encontrar_maximo_otimizado(lista_numeros):
    if not lista_numeros:
        return None
    return max(lista_numeros)

def encontrar_minimo_otimizado(lista_numeros):
    if not lista_numeros:
        return None
    return min(lista_numeros)

def ordenar_lista_otimizada(lista_numeros):
    return sorted(lista_numeros)

# ─────────────────────────────────────────────
# BENCHMARK
# ─────────────────────────────────────────────

def medir_tempo(func, *args, repeticoes=5):
    """Executa a função N vezes e retorna o tempo médio em ms."""
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        func(*args)
        fim = time.perf_counter()
        tempos.append((fim - inicio) * 1000)
    return sum(tempos) / len(tempos)

def formatar_ganho(t_original, t_otimizado):
    if t_otimizado == 0:
        return "∞x mais rápido"
    ganho = t_original / t_otimizado
    if ganho >= 1:
        return f"{ganho:.1f}x mais rápido"
    else:
        return f"{1/ganho:.1f}x mais lento"

def separador(char="─", largura=62):
    print(char * largura)

def executar_benchmark(tamanho: int, repeticoes: int = 5):
    lista = [random.randint(0, 10_000) for _ in range(tamanho)]

    funcoes = [
        ("Média",    calcular_media_original,    calcular_media_otimizada,    (lista,)),
        ("Máximo",   encontrar_maximo_original,   encontrar_maximo_otimizado,   (lista,)),
        ("Mínimo",   encontrar_minimo_original,   encontrar_minimo_otimizado,   (lista,)),
        ("Ordenação",ordenar_lista_original,      ordenar_lista_otimizada,      (lista,)),
    ]

    separador("═")
    print(f"  BENCHMARK — {tamanho:,} elementos | {repeticoes} repetições por função")
    separador("═")
    print(f"  {'Função':<12} {'Original':>12} {'Otimizado':>12} {'Ganho':>16}")
    separador()

    total_original  = 0
    total_otimizado = 0

    for nome, orig, otim, args in funcoes:
        t_orig = medir_tempo(orig, *args, repeticoes=repeticoes)
        t_otim = medir_tempo(otim, *args, repeticoes=repeticoes)
        total_original  += t_orig
        total_otimizado += t_otim
        ganho = formatar_ganho(t_orig, t_otim)
        print(f"  {nome:<12} {t_orig:>10.4f}ms {t_otim:>10.4f}ms {ganho:>16}")

    separador()
    ganho_total = formatar_ganho(total_original, total_otimizado)
    print(f"  {'TOTAL':<12} {total_original:>10.4f}ms {total_otimizado:>10.4f}ms {ganho_total:>16}")
    separador("═")
    print()

if __name__ == "__main__":
    random.seed(42)
    cenarios = [100, 1_000, 5_000, 10_000]
    for tamanho in cenarios:
        executar_benchmark(tamanho, repeticoes=5)
