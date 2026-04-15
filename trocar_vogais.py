#16. Trocar vogais por *:
frase = input("Informe uma frase: ").lower()
resultado = (frase
.replace("a","*")
.replace("e","*")
.replace("i","*")
.replace("0","*")
.replace("u","*"))
print(f"Vogais substituídas: {resultado}")
