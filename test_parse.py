import pytest
import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p  = tpfd.Parser()
p.debug = True

@p.on_recognize('{Animal} are cool')
def main(kwargs):
    animal = kwargs.get('animal')
    return 'sloths'

def test_string_parse():
    assert p.parse_string('Sloths are cool') == 'sloths'

if __name__ == '__main__':
    pytest.main()