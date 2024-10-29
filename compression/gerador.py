import random

# Função para gerar uma sequência de nucleotídeos aleatória
def gerar_sequencia(tamanho):
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(bases) for _ in range(tamanho))

# Tamanhos das sequências desejadas
tamanhos = [100, 1000, 2500, 5000, 7500, 10000]

# Gerar e salvar sequências em arquivos
for tamanho in tamanhos:
    sequencia = gerar_sequencia(tamanho)
    nome_arquivo = f'sequencia_{tamanho}.txt'  # Nome do arquivo
    with open(nome_arquivo, 'w') as f:
        f.write(sequencia)  # Escrever a sequência no arquivo

print("Sequências geradas e salvas com sucesso.")
