#15. Remover letra específica ('e'):
frase = input("Informe uma frase(que contenha a letra 'e'): ")
removerE = frase.replace("e"," ").replace("E"," ")
print(f"Letras 'e' removidas: {removerE}")
