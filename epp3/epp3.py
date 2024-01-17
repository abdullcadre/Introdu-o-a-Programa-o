# Nome: Isac Chaile 
# Número de Aluno: 2101849

def total_venda(transacao):
    """Calcula o preço total de uma venda."""
    preco_unitario, quantidade = transacao[1], transacao[2]

    if not isinstance(preco_unitario, (int, float)) or preco_unitario <= 0:
        raise ValueError("erro: preço deve ser um real positivo")
    elif not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("erro: quantidade deve ser um inteiro positivo")
    else:
        return float(preco_unitario * quantidade)

def total_compra(transacao):
    """Calcula o preço total de uma compra."""
    preco_unitario, quantidade = transacao[1], transacao[2]

    if not isinstance(preco_unitario, (int, float)) or preco_unitario <= 0:
        raise ValueError("erro: preço deve ser um real positivo")
    elif not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("erro: quantidade deve ser um inteiro positivo")
    else:
        return float(-preco_unitario * quantidade)

def total(transacao):
    """Calcula o preço total de uma transação."""
    tipo_transacao = transacao[0]

    if tipo_transacao == "VENDA":
        return total_venda(transacao)
    elif tipo_transacao == "COMPRA":
        return total_compra(transacao)
    else:
        raise ValueError("erro: transação inválida")

def filtra_por_total(transacoes, valor):
    """Filtra as transações com preço absoluto total não superior ao valor."""
    return [t for t in transacoes if abs(total(t)) <= valor]

def resumo_transacoes(saldo_inicial, transacoes):
    """Resumo das transações: saldo final, menor preço total de compra, maior preço total de venda."""
    saldo = saldo_inicial
    menor_compra = float('inf')
    maior_venda = 0

    for transacao in transacoes:
        preco_total = total(transacao)

        saldo += preco_total

        if transacao[0] == "COMPRA" and preco_total < menor_compra:
            menor_compra = preco_total
        elif transacao[0] == "VENDA" and preco_total > maior_venda:
            maior_venda = preco_total

    return (saldo, menor_compra if menor_compra != float('inf') else float('inf'), maior_venda)

# Exemplos de uso das funções
# Estes exemplos são apenas ilustrativos, pode testar com outros valores.
print(total_venda(("VENDA", 2.5, 4)))
print(total_venda(("VENDA", 2.0, 4)))

print(total_compra(("COMPRA", 2.5, 4)))
print(total_compra(("COMPRA", 1.0, 4)))

print(total(("VENDA", 2.5, 4)))
print(total(("COMPRA", 2.5, 4)))
print(total(("COMPRA", 2.0, 4)))

print(filtra_por_total([("VENDA", 2.5, 4), ("COMPRA", 2.5, 4), ("VENDA", 2.0, 2), ("COMPRA", 2.0, 1)], 4))
print(resumo_transacoes(10.0, [("VENDA", 2.5, 4), ("COMPRA", 2.5, 4), ("VENDA", 2.0, 2), ("COMPRA", 2.0, 1)]))
