# Nome: Isac Chaile
# Número de Aluno: 2101849

def processa_csv(nome_ficheiro):
    """
    Esta função recebe o nome de um ficheiro CSV e retorna uma lista de dicionários,
    em que cada dicionário representa uma linha do CSV, com as chaves sendo os títulos
    das colunas e os valores sendo os dados correspondentes.
    """
    dados = []  # Inicializa a lista que irá conter os dicionários

    # Abre o ficheiro CSV em modo de leitura
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        linhas = ficheiro.readlines()  # Lê todas as linhas do ficheiro

        # Extrai os cabeçalhos (títulos das colunas)
        cabecalho = linhas[0].strip().split(',')

        # Itera sobre as linhas do ficheiro, excluindo o cabeçalho
        for linha in linhas[1:]:
            valores = linha.strip().split(',')  # Divide a linha nos valores separados por vírgula
            linha_dict = {}  # Dicionário para armazenar os valores desta linha

            # Itera sobre os títulos das colunas e os valores correspondentes
            for i in range(len(cabecalho)):
                linha_dict[cabecalho[i]] = valores[i] if i < len(valores) else ''  # Valor vazio se não houver correspondência

            dados.append(linha_dict)  # Adiciona o dicionário à lista de dados

    return dados


def gera_csv(dados, nome_ficheiro):
    """
    Esta função recebe uma lista de dicionários representando os dados a serem
    escritos num ficheiro CSV e o nome do ficheiro a ser criado. Ela gera um
    ficheiro CSV com os dados fornecidos.
    """
    # Verifica se todos os dicionários têm as mesmas chaves
    chaves = set(dados[0].keys())
    for d in dados:
        if set(d.keys()) != chaves:
            raise ValueError("dados incoerentes")

    # Abre o ficheiro CSV em modo de escrita
    with open(nome_ficheiro, 'w', encoding='utf-8') as ficheiro:
        # Escreve o cabeçalho
        ficheiro.write(','.join(chaves) + '\n')

        # Escreve os dados
        for d in dados:
            linha = ','.join([d[chave] for chave in chaves])  # Obtém os valores na ordem das chaves
            ficheiro.write(linha + '\n')


# Exemplo de utilização das funções:
if __name__ == "__main__":
    # Teste da função processa_csv
    print(processa_csv('compras.csv'))

    # Teste da função gera_csv com dados coerentes
    try:
        gera_csv([{'produto': 'maçãs', 'preço unitário': '0.50€', 'quantidade': '10'}, 
                  {'produto': 'garrafas de água', 'preço unitário': '0.33€', 'quantidade': '6'}, 
                  {'produto': 'vassoura', 'preço unitário': '15€', 'quantidade': '1'}], "compras2.csv")
    except ValueError as e:
        print(e)  # Imprime a mensagem de erro

    # Teste da função gera_csv com dados incoerentes
    try:
        gera_csv([{'produto': 'maçãs', 'preço unitário': '0.50€'}, 
                  {'produto': 'garrafas de água', 'preço unitário': '0.33€', 'quantidade': '6'}, 
                  {'produto': 'vassoura', 'preço unitário': '15€', 'quantidade': '1'}], "compras3.csv")
    except ValueError as e:
        print(e)  # Imprime a mensagem de erro

