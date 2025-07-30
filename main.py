import json
import os

print("Selecione uma opção: ")
print(" 1 - Calcular PTAM \n 2 - Calcular Desconto \n 3 - Adicionar valor de M² \n 4 - Sair")

menu = int(input(""))

if menu == 1:
    print("1")
elif menu == 2:
    print("2")
elif menu == 3:
    print("3")
else:
    print("Saindo do programa.")
    exit()