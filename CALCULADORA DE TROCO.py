#calculadora de troco

valor_01 = float(input("Digite o valor do produto 1: "))
valor_02 = float(input("Digite o valor do produto 2: "))
total = valor_01 + valor_02

print("O valor total da compra é: R$", total)
dinheiro = float(input("Digite o valor que você pagou: "))
troco = dinheiro - total
print("O troco é: R$", troco)
