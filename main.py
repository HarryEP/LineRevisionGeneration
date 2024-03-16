'''Revision Program'''

import random
import requests


def fetch_google_file(url):
    '''function to get the file from a google docs file'''
    try:
        response = requests.get(url, timeout=120)
        return response.status_code
    except response.Timeout:
        print("Request timed out, please try again")
    except Exception as e:
        print(f"An error ({e} occured")
    return None


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


def randomiser(quantity_lines: int, extract_size: int = 1):
    '''to randomise the lines that are sent'''
    number = random.randint(0, quantity_lines - extract_size)
    print(number)


if __name__ == "__main__":
    # get user inputs like how many lines/which book they want etc
    randomiser(4)
    source_data = read_file('example.txt')
    cleaned_data = clean_data(source_data)
    print(cleaned_data)
