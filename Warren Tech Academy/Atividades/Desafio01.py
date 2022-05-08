# Alguns números inteiros positivos n possuem uma propriedade na qual a soma de n + reverso(n) resultam em números ímpares.
# Por exemplo, 36 + 63 = 99 e 409 + 904 = 1313. 
# Considere que n ou reverso(n) não podem começar com 0.
# Existem 120 números reversíveis abaixo de 1000.
# Construa um algoritmo que mostre na tela todos os números n onde a soma de n + reverso(n) resultem em números ímpares que estão abaixo de 1 milhão.
# Declaração Variáveis
def main():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    soma = n1 + n2
    i = 0
    ímpar = 1

    while i < soma: 
            # imprima o próximo número ímpar
        print(ímpar)

            # incremente p contador
        i = i + 1

            # determine o próximo ímpar
        ímpar = ímpar + 2      
       
main()
