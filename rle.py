import re
import os.path


def encode(content):
    current_index = 0
    encoded_content = str()

    while current_index < len(content):
        current_char_occurrences = 0
        current_char = content[current_index]

        if current_char.isdigit():
            print('Error, there is a digit in the content supplied. RLE has some limitations, here is one :)')
            return

        for c in content[current_index:]:
            if c == current_char:
                current_char_occurrences += 1
            else:
                break

        encoded_content += '{}{}'.format(current_char_occurrences, current_char)
        current_index += current_char_occurrences
    return encoded_content


def decode(content):
    split_content = re.findall(r'([0-9]+)([a-zA-Z])', content)
    decoded_content = str()
    for c in split_content:
        decoded_content += int(c[0]) * c[1]
    return decoded_content


def rate(decoded_content, encoded_content):
    return (len(decoded_content) / len(encoded_content)) * 100


def read_file_data(path):
    if os.path.isfile(path):
        with open(path) as file:
            return ''.join(file.readlines())
    print('Please supply a valid file path')
    return


def write_file_data(path, content):
    with(open(path, 'w')) as file:
        file.write(content)


if __name__ == '__main__':
    choice = input('Would you rather encode(e) or decode(d) a file :')

    input_path = input('Input file path : ')
    output_path = input('Output file path : ')
    write_file_data(output_path,
                    decode(read_file_data(input_path)) if choice == 'd' else encode(read_file_data(input_path)))
    print('Done!')
