from unidecode import unidecode

texto = input("Digite um texto com acentos: ")
texto_sem_acentos = unidecode(texto)

print("Texto original:", texto)
print("Texto sem acentos:", texto_sem_acentos)