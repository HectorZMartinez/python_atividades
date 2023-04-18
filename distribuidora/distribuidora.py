valor_total = 67836.43 + 36678.66 + 29229.88 + 27165.48 + 19849.53

# Dicionário com os valores de faturamento de cada estado
valores = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do percentual de representação de cada estado
percentuais = {}
for estado, valor in valores.items():
    percentuais[estado] = (valor / valor_total) * 100

# Impressão dos resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
