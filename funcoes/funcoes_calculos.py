def calcular_taxas(valor_terreno):
    valor_foro = valor_terreno * 0.003
    valor_laudemio = valor_terreno * 0.025  
    valor_dominio = valor_terreno * 0.12   
    return valor_foro, valor_laudemio, valor_dominio

def calculo_desconto_personalizado(valor_taxa, desconto_personalizado):
    desconto = valor_taxa - (valor_taxa * (desconto_personalizado / 100))
    return desconto