
import os

from compression.performance.perform import measure_performance


def compression_bit(dna: str) -> str:
    sequence = {
        'A': 0b00,
        'C': 0b01,
        'G': 0b10,
        'T': 0b11,
    }

    N_compression = 0

    for nucleotide in dna:
        N_compression = (N_compression << 2) | sequence[nucleotide]

    length = len(dna)
    length_bits = length.to_bytes(4, 'big')
    num_bytes = (N_compression.bit_length() + 7) // 8 or 1

    with open('compressed_dna.bin', 'wb') as file:
        file.write(length_bits)  # Escreve o comprimento primeiro
        file.write(N_compression.to_bytes(num_bytes, 'big'))

    return bin(N_compression)[2:]


def decompression_bit(compression_dna: int) -> str:
    sequence = {
        0b00: 'A',
        0b01: 'C',
        0b10: 'G',
        0b11: 'T',
    }

    with open('compressed_dna.bin', 'rb') as file:
        length_bytes = file.read(4)  # Lê o primeiro byte
        length = int.from_bytes(length_bytes, 'big')  # Converte para inteiro

        N_compression = int.from_bytes(file.read(), 'big')

    dna = ""

    for _ in range(length):
        dna_bits = N_compression & 0b11
        dna = sequence[dna_bits] + dna
        N_compression >>= 2

    return dna


if __name__ == '__main__':
    valores = {
        'dna': 'TAGGGAT',
        'dna_compression': 0b11001010100011,
    }

    print(f"Valor passado: {valores['dna']}")

    print('Medindo a performance da compressão')
    compression_time, compression_memory, compressed_result = measure_performance(compression_bit, valores['dna'])
    print("Resultado da Compressão:", compressed_result)
    print(f"Tempo de execução da compressão: {compression_time:.6f} segundos")
    print(f"Memória usada na compressão: {compression_memory:.6f} MB")

    print('\n' * 2)

    print('Medindo a performance da descompressão')
    decompression_time, decompression_memory, decompressed_result = measure_performance(decompression_bit, valores['dna_compression'])
    print("Resultado da Descompressão:", decompressed_result)
    print(f"Tempo de execução da descompressão: {decompression_time:.6f} segundos")
    print(f"Memória usada na descompressão: {decompression_memory:.6f} MB")

    print('\n' * 2)

    print('Comparando tamanhos dos arquivos')
    if os.path.exists('compressed_dna.bin'):
        tamanho_bin = os.path.getsize('compressed_dna.bin')
    else:
        tamanho_bin = 0
    print('Tamanho do arquivo binário comprimido:')
    print(f'bin: {tamanho_bin} bytes')
