import json
import os
import statistics

dir_path = os.path.dirname(os.path.realpath(__file__))

# carregar dados do arquivo json
with open(os.path.join(dir_path, "dados.json"), "r") as f:
    dados = json.load(f)

faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]
menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = statistics.mean(faturamento)
dias_acima_da_media = sum(valor > media_mensal for valor in faturamento)

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")