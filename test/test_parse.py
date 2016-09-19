#coding=utf-8

import pytest
import tpfd
import logging

from tpfd import with_pattern

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = False

LIST_RESULTS = []

FILE_RESULTS = []


@p.on_parse('{Animal} are cool')
def main(animal):
    return animal

@p.on_parse('List test {number}')
def list_test(number):
    LIST_RESULTS.append(True)


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
def two_word_test(words):
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


def test_string_find():
    p.find_string('<p>the <b>bold</b> text</p>') == 'the bold text'


def test_iter_parse1():
    l = ['List test 1', 'List test 2', 'List antitest 1']
    p.parse(l)
    assert 2 == len(LIST_RESULTS)


def test_iter_file1():
    p.parse_file('Test.txt')
    assert 1 == len(FILE_RESULTS)


def test_int_parse1():
    assert p.parse('The awnser is 42') == 42
    

if __name__ == '__main__':
    pytest.main()
