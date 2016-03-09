import pytest
import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = True

LIST_RESULTS = []


@p.on_recognize('{Animal} are cool')
def main(kwargs):
    animal = kwargs.get('animal')
    return animal


@p.on_recognize('List test {number}')
def list_test(kwargs):
    number = kwargs.get('number')
    LIST_RESULTS.append(True)


def test_string_parse1():
    assert p.parse_string('Sloths are cool') == 'sloths'


def test_string_parse2():
    assert p.parse_string('Turtles are cool') == 'turtles'


def test_string_parse3():
    assert p.parse_string('Bears beats Battle Star Galactica') == None


def test_iter_parse1():
    l = ['List test 1', 'List test 2', 'List antitest 1']
    p.iter_parse(l)
    assert 2 == len(LIST_RESULTS)


if __name__ == '__main__':
    pytest.main()
