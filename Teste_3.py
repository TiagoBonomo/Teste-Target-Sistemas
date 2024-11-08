# -*- coding: utf-8 -*-
"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
    a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
    b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

# Carregar dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Filtrar dias com faturamento (exclui dias com valor 0.0)
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor e o maior valor de faturamento
menor_valor = min(dias_com_faturamento)
maior_valor = max(dias_com_faturamento)

# Calcular a média mensal de faturamento
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contar os dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

# Exibir resultados
print(f"Menor valor de faturamento em um dia do mês: {menor_valor}")
print(f"Maior valor de faturamento em um dia do mês: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")