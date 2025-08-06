import funcoes.funcoes_calculos

area = 100
valor_m2 = 1500.0

valor_terreno, valor_foro, valor_laudemio, valor_dominio = funcoes.funcoes_calculos.calcular_taxas(area, valor_m2)

print(f"Valor do Terreno: {valor_terreno:.2f}, Foro: {valor_foro:.2f}, Laudemio: {valor_laudemio:.2f}, Dominio: {valor_dominio:.2f}")