import tpfd
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('test')

p = tpfd.Parser()

@p.on_find('>{}<')
def find_example(words):
    print (words)

def find_string():
    p.find_string('<p>the <b>bold</b> text</p>')


if __name__ == '__main__':
    find_string()