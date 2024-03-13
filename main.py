'''Revision Program'''


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


if __name__ == "__main__":
    source_data = read_file('example.txt')
    cleaned_data = clean_data(source_data)
    print(cleaned_data)
