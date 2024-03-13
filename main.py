

def read_file(file_name: str) -> list[str]:
    '''reads in the file and splits it up by line'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def clean_data(data: list[str]) -> list[str]:
    '''this function removes empty lines of a text'''
    for i in range(len(data)-1, -1, -1):
        if data[i] == '':
            data.pop(i)
    return data


if __name__ == "__main__":
    data = read_file('example.txt')
    data = clean_data(data)
    print(data)
