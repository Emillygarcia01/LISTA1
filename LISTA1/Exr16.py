valor = float(input("Digite o valor da prestação em atraso: "))
taxa = float(input("Digite a taxa de juros em percentual: "))
tempo = int(input("Digite o tempo em atraso em dias: "))

prestacao = valor + (valor * (taxa/100) * (tempo/30))

print(f"O valor da prestação em atraso é: R${prestacao:.2f}")