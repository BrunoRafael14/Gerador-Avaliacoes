import json
import os


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Selecione uma opção: ")
    print(" 1 - Calcular PTAM \n 2 - Calcular Desconto \n 3 - Adicionar valor de M² \n 4 - Sair")
    menu = int(input(""))

    if menu == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("1")

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
        os.system("cls" if os.name == "nt" else "clear")
        print("3")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Obrigado Pela Preferência.")
        exit()