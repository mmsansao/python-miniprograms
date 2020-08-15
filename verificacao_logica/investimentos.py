def investimentos(investimento, taxa_juros, imposto, desejado):
    anos = 0
    while investimento < desejado:
        juros = investimento * taxa_juros
        acumulado = investimento + juros
        recolhido = juros * imposto
        investimento = acumulado - recolhido
        anos += 1
    return anos
