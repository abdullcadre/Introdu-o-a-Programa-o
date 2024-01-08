# Nome: Isac Chaile
# Número de Aluno: Isac Chaile

def soma_divisores_proprios(n):
    """Calcula a soma dos divisores próprios de um número n."""
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

def perfeito(n):
    """Verifica se um número n é perfeito."""
    return soma_divisores_proprios(n) == n

def multiplica_perfeitos(a, b):
    """Calcula o produto dos números primos perfeitos entre a e b (inclusive)."""
    produto = 1
    for num in range(a, b + 1):
        if perfeito(num):
            produto *= num
    return produto

# Exemplos de uso das funções
# Estes exemplos são apenas ilustrativos, pode testar com outros valores.
print(soma_divisores_proprios(1))
print(soma_divisores_proprios(12))
print(soma_divisores_proprios(28))
print(soma_divisores_proprios(496))

print(perfeito(1))
print(perfeito(12))
print(perfeito(28))
print(perfeito(496))

print(multiplica_perfeitos(1, 5))
print(multiplica_perfeitos(1, 12))
print(multiplica_perfeitos(1, 28))
print(multiplica_perfeitos(1, 496))
