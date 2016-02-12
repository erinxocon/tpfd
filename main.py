import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()
p.debug = True


@p.on_recognize('{Animal} are cool')
def main(kwargs):
    logging.debug('Inside main')
    animal = kwargs.get('animal')
    return '{0}'.format(animal)

test = p.parse_string('Sloths are cool')
print(test)
