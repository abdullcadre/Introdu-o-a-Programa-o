# Nome: Isac Chaile
# Número de Aluno: 2101849

def balanco_topico(topico):
    """
    Esta função recursiva recebe um tópico e retorna a soma do valor total de todas as transações
    presentes nesse tópico, incluindo as transações dos sub-tópicos.
    """
    total = 0

    for elemento in topico["transações"]:
        if "produto" in elemento:
            total += elemento["preço unitário"] * elemento["quantidade"]
        elif "tópico" in elemento:
            total += balanco_topico(elemento)

    return total


def balanco_mensal(lista_topicos, mes, ano):
    """
    Esta função recursiva recebe uma lista de tópicos, um número inteiro correspondente ao mês e
    um número inteiro correspondente ao ano, e retorna a soma do valor total de todas as transações
    efetuadas nesse mês e ano, pertencentes aos tópicos presentes na lista, incluindo os sub-tópicos
    de cada tópico.
    """
    total = 0

    for topico in lista_topicos:
        for elemento in topico["transações"]:
            if "produto" in elemento and elemento["data"][1] == mes and elemento["data"][2] == ano:
                total += elemento["preço unitário"] * elemento["quantidade"]
            elif "tópico" in elemento:
                total += balanco_mensal([elemento], mes, ano)

    return total


def desenha_balanco_por_topico(lista_topicos):
    """
    Esta função recebe uma lista de tópicos e cria um gráfico de barras com a representação do
    balanço de cada tópico (não incluindo sub-tópicos), utilizando a biblioteca Matplotlib.
    """
    import matplotlib.pyplot as plt

    tópicos = []
    valores = []

    for topico in lista_topicos:
        total = balanco_topico(topico)
        tópicos.append(topico["tópico"])
        valores.append(total)

    plt.bar(tópicos, valores)
    plt.xlabel('Tópicos')
    plt.ylabel('Balanço')
    plt.title('Balanço por Tópico')
    plt.show()


def desenha_balanco_anual(lista_topicos, ano):
    """
    Esta função recebe uma lista de tópicos e um número inteiro correspondente a um ano, e cria
    um gráfico de linha com a representação do balanço de todos os meses do ano em consideração,
    de acordo com a lista de tópicos fornecida, utilizando a biblioteca Matplotlib.
    """
    import matplotlib.pyplot as plt

    meses = range(1, 13)
    valores = []

    for mes in meses:
        total = balanco_mensal(lista_topicos, mes, ano)
        valores.append(total)

    plt.plot(meses, valores, marker='o', color='b', linestyle='-')
    plt.xlabel('Mês')
    plt.ylabel('Balanço')
    plt.title(f'Balanço Anual de {ano}')
    plt.xticks(meses)
    plt.grid(True)
    plt.show()
