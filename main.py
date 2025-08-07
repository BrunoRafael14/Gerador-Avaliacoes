import json
import os
from unidecode import unidecode
import funcoes.funcoes_calculos

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
                valor_foro, valor_laudemio, valor_dominio = funcoes.funcoes_calculos.calcular_taxas(valor_terreno)

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
            valor_terreno = float(input("Digite o valor do Terreno: R$ ").replace(",", "."))
            quantidade_foros = int(input("Digite a quantidade de anos de Foro a ser considerado (máx 5 anos): "))
            if quantidade_foros > 5:
                print("Quantidade de anos de Foro não pode ser maior que 5.")
                a = input("")
                continue
            valor_foro, valor_laudemio, valor_dominio = funcoes.funcoes_calculos.calcular_taxas(valor_terreno)

            print("Digite Tipo de desconto que deseja aplicar: \n1 - Pré-definidos \n2 - Personalizado")
            tipo_desconto = input("")
            if tipo_desconto == "sair":
                break
            if tipo_desconto == "1":
                while True:
                    print("Escolha as taxas para desconto: \n1 - Apenas foro \n2 - Foro e Laudêmio \n3 - Foro, Laudemio e Dominio \n4 - Foro e Dominio")
                    taxas_escolhidas = int(input(""))
                    if taxas_escolhidas == 1:
                        print("----------------------------------------------------")
                        print(f"Desconto de 5% sobre o Foro: R$ {(valor_foro * quantidade_foros) - ((valor_foro * quantidade_foros) * 0.05):.2f}")
                        print("----------------------------------------------------")
                        teste = input("Gostaria de calcular outro desconto? (s/n): ").strip().lower()
                        if teste == "sim" or teste == "s":
                            continue
                        else:
                            break
                    elif taxas_escolhidas == 2:
                        print("----------------------------------------------------")
                        print(f"Desconto de 8% sobre o Foro e Laudêmio: R$ {((valor_foro * quantidade_foros) + valor_laudemio) - (((valor_foro * quantidade_foros) + valor_laudemio) * 0.08):.2f} \nDesconto de 10% sobre o Foro e Laudêmio: R$ {((valor_foro * quantidade_foros) + valor_laudemio) - (((valor_foro * quantidade_foros) + valor_laudemio) * 0.10):.2f}")
                        print("----------------------------------------------------")
                        teste = input("Gostaria de calcular outro desconto? (s/n): ").strip().lower()
                        if teste == "sim" or teste == "s":
                            continue
                        else:
                            break
                    elif taxas_escolhidas == 3:
                        print("----------------------------------------------------")
                        print(f"Desconto de 8% sobre o Foro, Laudêmio e Dominio: R$ {((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio) - (((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio) * 0.08):.2f} \nDesconto de 8% sobre o Foro e Laudêmio, com parcelamento de 3 vezes sobre Domínio: R$ {((valor_foro * quantidade_foros) + valor_laudemio) - (((valor_foro * quantidade_foros) + valor_laudemio) * 0.08):.2f} + 3x R$ {valor_dominio / 3:.2f}")
                        print("----------------------------------------------------")
                        teste = input("Gostaria de calcular outro desconto? (s/n): ").strip().lower()
                        if teste == "sim" or teste == "s":
                            continue
                        else:
                            break
                    elif taxas_escolhidas == 4:
                        print("----------------------------------------------------")
                        print(f"Desconto de 8% sobre o Foro e Dominio: R$ {((valor_foro * quantidade_foros) + valor_dominio) - (((valor_foro * quantidade_foros) + valor_dominio) * 0.08):.2f}")
                        print(f"Desconto de 10% sobre o Foro e Dominio: R$ {((valor_foro * quantidade_foros) + valor_dominio) - (((valor_foro * quantidade_foros) + valor_dominio) * 0.10):.2f}")
                        print("----------------------------------------------------")
                        teste = input("Gostaria de calcular outro desconto? (s/n): ").strip().lower()
                        if teste == "sim" or teste == "s":
                            continue
                        else:
                            break
            elif tipo_desconto == "2":
                desconto_personalizado = float(input("Digite o porcentagem do desconto personalizado: "))
                print("----------------------------------------------------")
                print(f"Valor Foro com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_foro * quantidade_foros, desconto_personalizado) :.2f} \nValor Laudêmio com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_laudemio, desconto_personalizado) :.2f} \nValor Domínio Direto com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_dominio, desconto_personalizado) :.2f} \nValor Total com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio, desconto_personalizado) :.2f}")
                print("----------------------------------------------------")

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
                    "comercial": {"valor_m2_comercial": 0.0},
                    "apartamento": {"valor_m2_apartamento": 0.0}
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

            elif tipo_imovel_cadastro == "apartamento":
                enderecos[rua_cadastro]["apartamento"]["valor_m2_apartamento"] = valor_m2_cadastro

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