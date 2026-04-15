#19. Substituir palavra em uma frase:
frase = input("Digite uma frase: ")
print(f"Sua frase: {frase}")
antiga = input("Qual palavra deseja substituir?: ")
nova = input("Qual será a nova palavra?:  ")
print(f"Frase com palavra substituída: {frase.replace(antiga,nova,1)}")
