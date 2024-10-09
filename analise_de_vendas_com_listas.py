def analisar_vendas_anuais(entrada):
    
    vendas = list(map(int, entrada.split(',')))

    # Inicializamos uma lista para armazenar os resultados
    resultados = []

    # Iteramos sobre a lista de vendas, pegando grupos de 12 elementos
    for i in range(0, len(vendas), 12):
        ano = vendas[i:i+12]
        total = sum(ano)
        media = total / len(ano)
        resultados.append((total, media))

    return resultados

# Exemplo de uso
entrada = "120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60"

resultados = analisar_vendas_anuais(entrada)

# Imprimindo os resultados
for i, resultado in enumerate(resultados):
    print(f"{resultado[0]}, {resultado[1]:.2f}")

