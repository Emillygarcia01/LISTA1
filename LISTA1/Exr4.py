num = int(input("Digite um número no formato CDU: "))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

print("Centena={centena}")
print("Dezena={dezena}")
print("Unidade={unidade}")