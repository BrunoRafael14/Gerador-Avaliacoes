def calcular_taxas(area, valor_m2):
    valor_terreno = area * valor_m2
    valor_foro = valor_terreno * 0.003
    valor_laudemio = valor_terreno * 0.025  
    valor_dominio = valor_terreno * 0.12   
    return valor_terreno, valor_foro, valor_laudemio, valor_dominio