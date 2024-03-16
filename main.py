'''Revision Program'''

import random


def read_file(file_name: str) -> list[str]:
    '''reads in the file and splits it up by line'''
    with open(file_name, encoding='utf-8') as file:
        raw_data = file.read()
    return raw_data.split('\n')


def clean_data(data: list[str]) -> list[str]:
    '''this function removes empty lines of a text'''
    for i in range(len(data)-1, -1, -1):
        if data[i] == '':
            data.pop(i)
    return data


def randomiser(quantity_lines: int, all_lines: list[str], extract_size: int = 1):
    '''to randomise the lines that are sent'''
    number = random.randint(0, quantity_lines - extract_size)
    return all_lines[number:number+extract_size]


def display_lines(lines: list[str]):
    '''this is to display the lines in a nice manner'''
    for line in lines:
        print(line)


def main():
    '''this function is to run everything and ask the user necessary questions'''
    num_lines_wanted = int(input("How many lines would you like?: "))
    source_data = read_file('example.txt')
    cleaned_data = clean_data(source_data)
    lines = randomiser(len(cleaned_data), cleaned_data, num_lines_wanted)
    display_lines(lines)


if __name__ == "__main__":
    main()
