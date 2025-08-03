import json

rua_busca = "Santa Maria Goretti"
cidade_busca = "caruaru"
tipo_imovel_busca = "comercial"

with open("informacoes/enderecos.json", "r") as enderecos:
    enderecos = json.load(enderecos)
if rua_busca in enderecos and cidade_busca in enderecos[rua_busca]["cidade"] and tipo_imovel_busca in enderecos[rua_busca]["tipo_imovel"]:
    valor_m2 = enderecos[rua_busca]["valor_m2"]
    print(valor_m2)