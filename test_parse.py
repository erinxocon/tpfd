import pytest
import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = True


@p.on_recognize('{Animal} are cool')
def main(kwargs):
    animal = kwargs.get('animal')
    return animal

def test_string_parse():
    assert p.parse_string('Sloths are cool') == 'sloths'
    assert p.parse_string('Turtles are cool') == 'turtles'
    assert p.parse_string('Bears beats Battle Star Galactica') == None

if __name__ == '__main__':
    pytest.main()
