import os

def split_large_file(input_file, output_directory, chunk_size):
    with open(input_file, 'rb') as f:
        chunk_number = 1
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            output_file = os.path.join(output_directory, f'output_chunk_{chunk_number}.txt')
            with open(output_file, 'wb') as chunk_file:
                chunk_file.write(data)
            chunk_number += 1

if __name__ == '__main__':
    input_file = 'input.txt'
    output_directory = 'output_chunks'
    chunk_size = 2 * 1024 * 1024 * 1024

    os.makedirs(output_directory, exist_ok=True)

    split_large_file(input_file, output_directory, chunk_size)
