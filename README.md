# Tarefa: Compactação e Descompactação de Sequências de DNA

![\[Assistir Vídeo\]()](docs/img/capa.png)

Objetivo: Implementar compactação e descompactação de sequências de DNA usando dois métodos: strings e operações bitwise.

Parte 1: Usando Strings

- Compactação: Mapeia nucleotídeos ('A', 'C', 'G', 'T') para strings de bits e salva em um arquivo de texto.
- Descompactação: Reconstrói a sequência original a partir da string de bits.

Parte 2: Usando Bitwise

- Compactação Bitwise: Desloca bits e usa OR para compactar nucleotídeos em um número inteiro.
- Salvar: Grava a sequência compactada em um arquivo binário.
- Descompactação Bitwise: Extrai e mapeia de volta para nucleotídeos usando operações de bits.

Comparação: Avalia o tamanho dos arquivos gerados e a economia de espaço da compactação bitwise usando os.path.getsize().

Parte 3: Análise de Performance

- Mede o tempo de execução e uso de memória (opcional) para sequências de 100, 1000, 2500, 5000, 7500 e 10000 nucleotídeos.
- Compara tempo, uso de memória e tamanhos dos arquivos entre as abordagens de strings e bitwise.


# Instalação

### Instruções de Uso
Este sistema foi desenvolvido utilizando o Poetry para gerenciamento de dependências. Caso você prefira não utilizar o Poetry, um arquivo requirements.txt está disponível na raiz do projeto, gerado por uma extensão do Poetry.

### Como Ler o DNA de um Arquivo
Coloque a sequência DNA em um arquivo de texto na pasta files

### Executando o Programa
Para rodar o programa, use o seguinte comando:
```bash
python3 compression/main.py
```

# Relátorio

## Desempenho de Compressão e Descompressão: Bit vs String

| Sequência | Bit Compression | Bit Decompression | String Compression | String Decompression |
|-----------|------------------|-------------------|--------------------|----------------------|
| 100       | 1.103           | 900              | 870               | 730                  |
| 1000      | 781             | 546              | 250               | 519                  |
| 2500      | 1.185           | 1.411            | 342               | 1.029                |
| 5000      | 5.234           | 3.346            | 509               | 798                  |
| 7500      | 4.528           | 5.345            | 407               | 1.139                |
| 10000     | 8.454           | 5.249            | 461               | 1.473                |


### Gráfico de Desempenho de Compressão e Descompressão: Bit vs String
![Desempenho de Compressão e Descompressão: Bit vs String](<docs/img/Desempenho de Compressão e Descompressão_ Bit vs String.png>)

## Comparação de armazenamento ".TXT" e ".BIT"

| Sequência | Arquivo TXT (bytes) | Arquivo Binário (bytes) | Redução (bytes) |
|-----------|----------------------|-------------------------|------------------|
| 100       | 200                  | 29                      | 171             |
| 1000      | 2000                 | 254                     | 1746            |
| 2500      | 5000                 | 629                     | 4371            |
| 5000      | 10000                | 1254                    | 8746            |
| 7500      | 15000                | 1879                    | 13121           |
| 10000     | 20000                | 2504                    | 1749            |


### Gráfico Comparação de armazenamento ".TXT" e ".BIT"

![Comparação de armazenamento ".TXT" e ".BIT"](<docs/img/Comparação de armazenamento _.TXT_ e _.BIT_.png>)

## Tabela para Comparação do Uso de Memória

| Sequência | Bit Compression | Bit Decompression | String Compression | String Decompression |
|-----------|------------------|-------------------|--------------------|----------------------|
| 100       | 0.0             | 0.0              | 0.0               | 0.0                 |
| 1000      | 0.0             | 0.0              | 0.0               | 0.0                 |
| 2500      | 0.0             | 0.0              | 0.125             | 0.0                 |
| 5000      | 0.0             | 0.0              | 0.0               | 0.125               |
| 7500      | 0.0             | 0.0              | 0.0               | 0.125               |
| 10000     | 0.0             | 0.0              | 0.0               | 0.25                |


## Relatório Compressão e Descompressão de Sequências de DNA
1. Eficiência de Espaço

- A compressão bit a bit é mais eficiente em termos de espaço, reduzindo significativamente o tamanho dos arquivos em comparação com a compressão de strings. Por exemplo, para uma sequência de 7500, a compressão bit a bit reduz o arquivo de 15000 bytes para 1879 bytes, enquanto a compressão de strings não alcança reduções tão drásticas.

2. Desempenho em Tempo

- A compressão de strings é mais rápida para sequências menores (100 a 1000), mas a compressão bit a bit se torna mais vantajosa em sequências maiores (acima de 5000). Nesse caso, a compressão e descompressão bit a bit superam as de strings em desempenho.

3. Uso de Memória RAM

- A compressão bit a bit consome menos memória RAM em comparação com a compressão de strings, especialmente para sequências maiores, o que pode ser um fator importante em sistemas com recursos limitados.

4. Desafios no Uso de Bitwise

- Manipular bits diretamente é mais complexo, exigindo maior conhecimento técnico. Isso pode dificultar a implementação e a manutenção em comparação com a manipulação de strings, que é mais intuitiva.

