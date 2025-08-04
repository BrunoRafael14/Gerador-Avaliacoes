import json
import os
from unidecode import unidecode

enderecos = {}
valor_m2_residencial = 0.0
valor_m2_comercial = 0.0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Selecione uma opção: ")
    print(" 1 - Calcular PTAM \n 2 - Calcular Desconto \n 3 - Adicionar valor de M² \n 4 - Sair")
    menu = int(input(""))

    if menu == 1:
        while menu == 1:
            os.system("cls" if os.name == "nt" else "clear")
            valor_m2 = 0.0
            rua_busca = unidecode(input("Digite a Rua de objeto: ").lower().replace("rua", "").strip())
            cidade_busca = unidecode(input("Digite a cidade do objeto: ").lower().strip())
            tipo_imovel_busca = unidecode(input("Digite o tipo de imóvel: ").lower().strip())
            area = float(input("Digite a área do imóvel em m²: ").replace(",", "."))

            with open("informacoes/enderecos.json", "r") as arquivo_enderecos:
                arquivo_enderecos = json.load(arquivo_enderecos)
            if rua_busca in arquivo_enderecos and cidade_busca in arquivo_enderecos[rua_busca]["cidade"]:
                valor_m2 = arquivo_enderecos[rua_busca][tipo_imovel_busca][f"valor_m2_{tipo_imovel_busca}"]

                valor_terreno = area * valor_m2
                valor_foro = valor_terreno * 0.003
                valor_laudemio = valor_terreno * 0.025
                valor_dominio = valor_terreno * 0.12

                print(f"Segue valores calculados: \n Valor do Terreno: {valor_terreno:.2f} \n Foro: {valor_foro:.2f} \n Foro últimos 5 anos: {valor_foro * 5:.2f} \n Laudemio: {valor_laudemio:.2f} \n Dominio: {valor_dominio:.2f}  ")
                resposta = input("Gostaria de calcular outro PTAM? (s/n): ").strip().lower()
                if resposta == "sim" or resposta == "s":
                    menu = 1
                else:
                    break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Imóvel não encontrado ou informações incorretas.")
                resposta = input("Gostaria de tentar novamente? (s/n): ").strip().lower()
                if resposta == "sim" or resposta == "s":
                    menu = 1
                else:
                    break

    elif menu == 2:
        while menu == 2:
            os.system("cls" if os.name == "nt" else "clear")
            valor_ptam = float(input("Digite o valor do PTAM: R$ "))
            desconto_08 = valor_ptam - (valor_ptam * 0.08)
            desconto_10 = valor_ptam - (valor_ptam * 0.10)
            desconto_12 = valor_ptam - (valor_ptam * 0.12)
            print(f"Desconto de 8%: R$ {desconto_08:.2f} \nDesconto de 10%: R$ {desconto_10:.2f} \nDesconto de 12%: R$ {desconto_12:.2f}")

            #Abaixo vou dar opção de valor persolanizado
            resposta_desconto_personalizado = input("Deseja fazer um desconto personalizado? (s/n): ").strip().lower()
            if resposta_desconto_personalizado == "sim" or resposta_desconto_personalizado == "s":
                desconto_personalizado = float(input("Digite o porcentagem do desconto personalizado: "))
                valor_desconto_personalizado = valor_ptam - (valor_ptam * (desconto_personalizado / 100))
                print(f"Valor com desconto personalizado: R$ {valor_desconto_personalizado:.2f}")

            continuar = input("Gostaria de colocar um novo valor de PTAM? (s/n): ")
            if continuar == "sim" or continuar == "s":
                menu = 2
            else:
                break
                
    elif menu == 3:
        while menu == 3:
            os.system("cls" if os.name == "nt" else "clear")
            print("Cadastramento de valor de M²\n-----------------------------")
            rua_cadastro = unidecode(input("Digite a Rua: ").lower().replace("rua", "").strip())
            cidade_cadastro = unidecode(input("Digite a Cidade: ").lower().strip())
            tipo_imovel_cadastro = unidecode(input("Digite o Tipo de Imóvel: ").lower().strip())
            valor_m2_cadastro = float(input("Digite o valor do M²: R$ ").replace(",", "."))

            with open("informacoes/enderecos.json", "r", encoding='utf-8') as arquivo_enderecos:
                enderecos = json.load(arquivo_enderecos)



            if rua_cadastro not in enderecos:
                enderecos[rua_cadastro] = {
                    "cidade": cidade_cadastro,
                    "residencial": {"valor_m2_residencial": 0.0},
                    "comercial": {"valor_m2_comercial": 0.0}
                }
            else:
                enderecos[rua_cadastro]["cidade"] = cidade_cadastro
                if "residencial" not in enderecos[rua_cadastro]:
                    enderecos[rua_cadastro]["residencial"] = {"valor_m2_residencial": null}
                if "comercial" not in enderecos[rua_cadastro]:
                    enderecos[rua_cadastro]["comercial"] = {"valor_m2_comercial": null}


            if tipo_imovel_cadastro == "residencial":
                enderecos[rua_cadastro]["residencial"]["valor_m2_residencial"] = valor_m2_cadastro

            elif tipo_imovel_cadastro == "comercial":
                enderecos[rua_cadastro]["comercial"]["valor_m2_comercial"] = valor_m2_cadastro

            else:
                print("Tipo de imóvel inválido. Por favor, escolha 'comercial' ou 'residencial'.")
                continue

            caminho_arquivo = "informacoes/enderecos.json"

            with open(caminho_arquivo, "w", encoding='utf-8') as arquivo_enderecos:
                json.dump(enderecos, arquivo_enderecos, ensure_ascii=False, indent=4)

            print("Valor de M² cadastrado com sucesso!")
            resposta = input("Gostaria de calcular outro PTAM? (s/n): ").strip().lower()
            if resposta == "sim" or resposta == "s":
                menu = 1
            else:
                break

        

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Obrigado Pela Preferência.")
        exit()