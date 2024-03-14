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


def randomiser(quantity_lines: int):
    '''to randomise the lines that are sent'''
    number = random.randint(1, quantity_lines)
    print(number)


if __name__ == "__main__":
    # get user inputs like how many lines/which book they want etc
    randomiser(4)
    source_data = read_file('example.txt')
    cleaned_data = clean_data(source_data)
    print(cleaned_data)
