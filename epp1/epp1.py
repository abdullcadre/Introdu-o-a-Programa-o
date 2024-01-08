# Nome: [Seu Nome]
# Número de Aluno: [Seu Número]

def verificar_numero_perfeito(numero):
    soma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i

    return soma_divisores == numero

def main():
    print("Introduza um número inteiro positivo:")
    numero = int(input())

    if numero > 0:
        if verificar_numero_perfeito(numero):
            print(f"{numero} é perfeito")
        else:
            print(f"{numero} não é perfeito")
    else:
        print("Por favor, introduza um número inteiro positivo.")

if __name__ == "__main__":
    main()
