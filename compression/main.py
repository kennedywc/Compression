import os
import time

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.text import Text

from compression.performance.perform import measure_performance
from compression.questoes.bitwise import compression_bit, decompression_bit
from compression.questoes.string import compression_str, decompression_str


DIRETORIO = './files/'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def listar_arquivos_texto(diretorio="./files/"):
    return [f for f in os.listdir(diretorio) if f.endswith(".txt")]


def renderizar_tabela(arquivos):
    print('\n')
    tabela = Table(title="Arquivos de Texto (.txt) no Diretório files/",
                   expand=True,
                   row_styles=['blue', 'green']
    )
    tabela.add_column("Índice", justify="center")
    tabela.add_column("Nome do Arquivo", justify="left")

    for indice, arquivo in enumerate(arquivos):
        tabela.add_row(str(indice), arquivo)

    tabela.add_row(str(-1), 'voltar para home...', style='red')

    return tabela


def operation(dna: str):
    table = Table(title="Desempenho de compressão e descompressão", expand=True)

    # Colunas da tabela
    table.add_column("Método", justify="center", style="cyan")
    table.add_column("Tempo (s)", justify="center", style="magenta")
    table.add_column("Memória (bytes)", justify="center", style="green")
    table.add_column("Resultado", justify="center", style="yellow")

    # Bit
    compression_time_bit, compression_memory_bit, compressed_result_bit = measure_performance(compression_bit, dna)
    dna_bit = compression_bit(dna)
    decompression_time_bit, decompression_memory_bit, decompressed_result_bit = measure_performance(decompression_bit, int(dna_bit, 2))

    # Add bit na tabela
    table.add_row("Bit Compression", f"{compression_time_bit:.6f}", f"{compression_memory_bit}", str(compressed_result_bit), style='blue')
    table.add_row("Bit Decompression", f"{decompression_time_bit:.6f}", f"{decompression_memory_bit}", str(decompressed_result_bit), style='blue')

    # String
    compression_time_str, compression_memory_str, compressed_result_str = measure_performance(compression_str, dna)
    dna_str = compression_str(dna)
    decompression_time_str, decompression_memory_str, decompressed_result_str = measure_performance(decompression_str, dna_str)

    # Add string na tabela
    table.add_row("String Compression", f"{compression_time_str:.6f}", f"{compression_memory_str}", str(compressed_result_str), style='yellow')
    table.add_row("String Decompression", f"{decompression_time_str:.6f}", f"{decompression_memory_str}", str(decompressed_result_str), style='yellow')

    console.print(table)

    # Tamanho dos arquivos
    compressed_size = os.path.getsize('compressed_dna.bin')
    original_size = os.path.getsize('dna_compression.txt')

    console.print(f"\nTamanho do arquivo txt: {original_size} bytes")
    console.print(f"Tamanho do arquivo binario: {compressed_size} bytes")
    console.print(f"Tamanho reduzido: {original_size - compressed_size} bytes")
    _ = input()


while True:
    clear_screen()

    console = Console()

    console.print(
        Panel(Text(
                '1. selecionar dna em arquivo\t 2. digitar dna\t 3.atualizar tela\t 4. sair',
                justify='center'
              ),
              title="Menu",
              subtitle='[bright_white on dark_red blink] Tarefa: Compactação e Descompactação de Sequências de DNA [/]',
              padding=1,
              style='cyan2'
        )
    )

    print('\n')

    console.print(
        Text('OBS: add um arquivo de texto com o dna na pasta files/ do projeto antes de selecionar a opção 1, ele vai ser listado para seleção',
             style='yellow')
    )

    select = Prompt.ask("Qual sua escolha?: ",
                    choices=['1', '2', '3', '4'])

    match select:
        case '1':
            clear_screen()

            console.print(
                Panel(Text(
                        'Selecione um arquivo com o dna nos arquivos listados abaixo',
                        justify='center'
                    ),
                    title="Escolha o seu arquivo!",
                    subtitle='[bright_white on dark_red blink] Tarefa: Compactação e Descompactação de Sequências de DNA [/]',
                    padding=1,
                    style='cyan2'
                )
            )

            with console.status("Working..."):
                arquivos_texto = listar_arquivos_texto()

                if len(arquivos_texto) > 0:
                    console.print(renderizar_tabela(arquivos_texto))
                else:
                    console.print('[b]nem um arquivo foi encontrado...[/]')
                    continue
            
            indice = IntPrompt.ask('informe o indice do arquivo')
            if (indice < 0):
                continue

            arquivo = DIRETORIO + arquivos_texto[indice]

            print('\n')
            console.print(Text(f' arquivo selecionado {arquivo} ', style='bold bright_white on dark_orange blink'), justify='center')
            print('\n') 

            with open(arquivo, "r", encoding='utf-8') as f:
                conteudo = f.read()

            conteudo = conteudo.replace("\n", "").replace("\r", "").replace("\t", "").strip()

            operation(conteudo)
        case '2':
            clear_screen()

            console.print(
                Panel(Text(
                        'Informe o DNA que dejá comprimir!!!',
                        justify='center'
                    ),
                    title="Digite alguma coisa",
                    subtitle='[bright_white on dark_red blink] Tarefa: Compactação e Descompactação de Sequências de DNA [/]',
                    padding=1,
                    style='cyan2'
                )
            )

            print('\n')
            conteudo = Prompt.ask("Informe o dna: ")
            if (conteudo == '-1'):
                continue

            operation(conteudo)
        case '3':
            continue
        case '4':
            clear_screen()
            exit()

    time.sleep(0.4)
