import os
import funcoes.funcoes_calculos

menu = 2
while menu == 2:
    os.system("cls" if os.name == "nt" else "clear")
    valor_terreno = float(input("Digite o valor do Terreno: R$ "))
    quantidade_foros = int(input("Digite a quantidade de anos de Foro a ser considerado (máx 5 anos): "))
    valor_foro, valor_laudemio, valor_dominio = funcoes.funcoes_calculos.calcular_taxas(valor_terreno)

    print("Digite Tipo de desconto que deseja aplicar: \n1 - Pré-definidos \n2 - Personalizado")
    tipo_desconto = int(input(""))
    if tipo_desconto == 1:
        
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
            print(f"Desconto de 10% sobre o Foro, Laudêmio e Dominio: R$ {((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio) - (((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio) * 0.1):.2f} \nDesconto de 8% sobre o Foro e Laudêmio, com parcelamento de 3 vezes sobre Domínio: R$ {((valor_foro * quantidade_foros) + valor_laudemio) - (((valor_foro * quantidade_foros) + valor_laudemio) * 0.08):.2f} + 3x R$ {valor_dominio / 3:.2f}")
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
    elif tipo_desconto == 2:
        desconto_personalizado = float(input("Digite o porcentagem do desconto personalizado: "))
        print("----------------------------------------------------")
        print(f"Valor Foro com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_foro * quantidade_foros, desconto_personalizado) :.2f} \nValor Laudêmio com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_laudemio, desconto_personalizado) :.2f} \nValor Domínio Direto com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado(valor_dominio, desconto_personalizado) :.2f} \nValor Total com desconto personalizado: R$ {funcoes.funcoes_calculos.calculo_desconto_personalizado((valor_foro * quantidade_foros) + valor_laudemio + valor_dominio, desconto_personalizado) :.2f}")
        print("----------------------------------------------------")

        continuar = input("Gostaria de colocar um novo valor de PTAM? (s/n): ")
        if continuar == "sim" or continuar == "s":
            menu = 2
        else:
            break









            # desconto_08 = valor_ptam - (valor_ptam * 0.08)
            # desconto_10 = valor_ptam - (valor_ptam * 0.10)
            # desconto_12 = valor_ptam - (valor_ptam * 0.12)
            # print(f"Desconto de 8%: R$ {desconto_08:.2f} \nDesconto de 10%: R$ {desconto_10:.2f} \nDesconto de 12%: R$ {desconto_12:.2f}")

            # #Abaixo vou dar opção de valor persolanizado
            # resposta_desconto_personalizado = input("Deseja fazer um desconto personalizado? (s/n): ").strip().lower()
            # if resposta_desconto_personalizado == "sim" or resposta_desconto_personalizado == "s":
            #     desconto_personalizado = float(input("Digite o porcentagem do desconto personalizado: "))
            #     valor_desconto_personalizado = valor_ptam - (valor_ptam * (desconto_personalizado / 100))
            #     print(f"Valor com desconto personalizado: R$ {valor_desconto_personalizado:.2f}")

            # continuar = input("Gostaria de colocar um novo valor de PTAM? (s/n): ")
            # if continuar == "sim" or continuar == "s":
            #     menu = 2
            # else:
            #     break
                