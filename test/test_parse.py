#coding=utf-8

import pytest
import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = False

PARSE_LIST_RESULTS = []

FIND_LIST_RESULTS = []

FILE_RESULTS = []


@p.on_parse('{Animal} are cool')
def main(animal):
    return animal

@p.on_parse('List test {number}')
def list_test(number):
    PARSE_LIST_RESULTS.append(True)


@p.on_parse('{Animal} beats Battlestar galactica')
def file_test(animal):
    FILE_RESULTS.append(True)


@p.on_parse('The awnser is {number:d}')
def int_test(number):
    return number


@p.on_parse('The {noun} who say {thing}!')
def two_word_test(noun, thing):
    return (noun, thing)


@p.on_find('>{}<')
def html_find(words):
    FIND_LIST_RESULTS.append(True)


@p.on_find('the')
def word_find(words):
    print (words)
    

def test_string_parse1():
    assert p.parse('Sloths are cool') == 'sloths'


def test_string_parse2():
    assert p.parse('Turtles are cool') == 'turtles'


def test_string_parse3():
    assert p.parse('Bears beats Battle Star Galactica') == None


def test_string_parse4():
    assert p.parse('The knights who say Ni!') == ('knights', 'ni')


def test_utf_parse1():
    assert p.parse('The 🇬🇧 who say ⚡️!') == ('🇬🇧', '⚡️')


def test_string_find1():
    p.find('The man drove the car to the store.') == 'the the the'


def test_string_find3():
    p.find('This string should return None') == None


def test_iter_parse1():
    l = ['List test 1', 'List test 2', 'List antitest 1']
    p.parse(l)
    assert 2 == len(PARSE_LIST_RESULTS)


def test_iter_find1():
    l = ['<p>the <b>bold</b> text</p>', '<p>the <i>italicized</i> text</p>', 'This statement has no html tags']
    p.find(l)
    assert 5 == len(FIND_LIST_RESULTS)


def test_iter_parse_file1():
    p.parse_file('Test1.txt')
    assert 1 == len(FILE_RESULTS)


def test_int_parse1():
    assert p.parse('The awnser is 42') == 42
    

if __name__ == '__main__':
    pytest.main()
