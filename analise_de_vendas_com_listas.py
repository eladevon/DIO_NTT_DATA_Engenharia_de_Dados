def obter_entrada_vendas(entrada):
    """
    Converte a string de entrada em uma lista de inteiros.

    Args:
        entrada (str): Uma string contendo números inteiros separados por vírgulas.

    Returns:
        list: Uma lista de inteiros representando as vendas mensais.
    """
    return list(map(int, entrada.split(',')))

def calcular_vendas(vendas):
    """
    Calcula o total e a média das vendas.

    Args:
        vendas (list): Uma lista de inteiros representando as vendas mensais.

    Returns:
        str: Uma string com o total e a média das vendas, separados por espaço.
    """
    total = sum(vendas)
    media = total / len(vendas)
    return f"{total} {media:.2f}"

# Exemplos de uso
entrada1 = "120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190"
entrada2 = "10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120"
entrada3 = "5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60"

print(calcular_vendas(obter_entrada_vendas(entrada1)))
print(calcular_vendas(obter_entrada_vendas(entrada2)))
print(calcular_vendas(obter_entrada_vendas(entrada3)))