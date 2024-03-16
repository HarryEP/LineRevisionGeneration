'''this is the test file for main.py'''
from main import clean_data


def test_clean_data_removes_empty_lines():
    '''clean data function removes all empty lines'''
    lines = ['hello', '', '', 'how are you']
    all_lines = clean_data(lines)
    assert all_lines == ['hello', 'how are you']
