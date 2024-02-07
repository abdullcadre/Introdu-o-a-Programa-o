# Teste dos métodos definidos no módulo epp5.py

# Importar o módulo
from epp5 import *

# Exemplo de transações e tópicos
transacoes = [
    {"preço unitário": 1.0, "quantidade": 4, "produto": "garrafa de água", "data": (1, 1, 2024)},
    {"preço unitário": -2.5, "quantidade": 3, "produto": "Fanta", "data": (1, 2, 2024)},
    {"preço unitário": 2, "quantidade": 2, "produto": "Coca-cola Zero", "data": (1, 1, 2024)}
]

topico_refrigerantes = {
    "tópico": "Refrigerantes",
    "transações": [
        {"preço unitário": -2.5, "quantidade": 3, "produto": "Fanta", "data": (1, 2, 2024)},
        {"tópico": "Sem açúcar", "transações": [
            {"preço unitário": 2, "quantidade": 2, "produto": "Coca-cola Zero", "data": (1, 1, 2024)}
        ]}
    ]
}

topico_garrafas = {
    "tópico": "Garrafas",
    "transações": [
        {"preço unitário": 1.0, "quantidade": 4, "produto": "garrafa de água", "data": (1, 1, 2024)},
        topico_refrigerantes
    ]
}

topico_pastelaria = {
    "tópico": "Pastelaria",
    "transações": [
        {"preço unitário": 3, "quantidade": 6, "produto": "Pastel de Belém", "data": (7, 1, 2024)}
    ]
}

# Teste da função balanco_topico
print("Balanço do tópico 'Garrafas':", balanco_topico(topico_garrafas))  # Deve ser -3.5
print("Balanço do tópico 'Refrigerantes':", balanco_topico(topico_refrigerantes))  # Deve ser -7.5

# Teste da função balanco_mensal
print("Balanço do mês 1, ano 2024:", balanco_mensal([topico_garrafas, topico_pastelaria], 1, 2024))  # Deve ser 13.0
print("Balanço do mês 2, ano 2024:", balanco_mensal([topico_garrafas, topico_pastelaria], 2, 2024))  # Deve ser -7.5

# Teste da função desenha_balanco_por_topico
desenha_balanco_por_topico([topico_garrafas, topico_pastelaria])

# Teste da função desenha_balanco_anual
desenha_balanco_anual([topico_garrafas, topico_pastelaria], 2024)
