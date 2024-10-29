import re

from compression.performance.perform import measure_performance


def compression_str(dna: str) -> str:

    sequence = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11',
    }

    new_dna: str = ''.join(map(sequence.get, dna))

    with open('dna_compression.txt', 'w') as file:
        file.write(new_dna)

    return new_dna


def decompression_str(dna: str) -> str:

    sequence = {
        '00': 'A',
        '01': 'C',
        '10': 'G',
        '11': 'T',
    }

    compression_dna = re.findall(r'..', dna)
    new_dna = ''.join(map(sequence.get, compression_dna))

    return new_dna


if __name__ == '__main__':
    # Medir o desempenho da compressão
    compression_time, compression_memory, compressed_dna = measure_performance(compression_str, 'TAGGGAT')
    print(f'Compression: {compressed_dna}')
    print(f'Compression Time: {compression_time:.6f} seconds')
    print(f'Compression Memory Usage: {compression_memory:.6f} MB')

    # Medir o desempenho da descompressão
    decompression_time, decompression_memory, decompressed_dna = measure_performance(decompression_str, '11001010100011')
    print(f'Decompression: {decompressed_dna}')
    print(f'Decompression Time: {decompression_time:.6f} seconds')
    print(f'Decompression Memory Usage: {decompression_memory:.6f} MB')
