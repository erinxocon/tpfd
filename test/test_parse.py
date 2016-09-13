import pytest
import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = True

LIST_RESULTS = []

FILE_RESULTS = []


@p.on_recognize('{Animal} are cool')
def main(kwargs):
    animal = kwargs.get('animal')
    return animal

@p.on_recognize('List test {number}')
def list_test(kwargs):
    number = kwargs.get('number')
    LIST_RESULTS.append(True)

@p.on_recognize('{Animal} beats Battlestar galactica')
def file_test(kwargs):
    FILE_RESULTS.append(True)

@p.on_recognize('The awnser is {number:d}')
def int_test(kwargs):
    number = kwargs.get('number')
    return number

@p.on_recognize('The {noun} who say {thing}!')
def two_word_test(kwargs):
    noun = kwargs.get('noun')
    exp = kwargs.get('thing')
    return (noun, exp)
    

def test_string_parse1():
    assert p.parse_string('Sloths are cool') == 'sloths'


def test_string_parse2():
    assert p.parse_string('Turtles are cool') == 'turtles'


def test_string_parse3():
    assert p.parse_string('Bears beats Battle Star Galactica') == None

def test_string_parse4():
    assert p.parse_string('The knights who say Ni!') == ('knights', 'ni')


def test_iter_parse1():
    l = ['List test 1', 'List test 2', 'List antitest 1']
    p.iter_parse(l)
    assert 2 == len(LIST_RESULTS)

def test_iter_file1():
    p.parse_file('Test.txt')
    assert 1 == len(FILE_RESULTS)

def test_int_parse1():
    assert p.parse_string('The awnser is 42') == 42
    
    


if __name__ == '__main__':
    pytest.main()
