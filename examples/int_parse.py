import tpfd

p = tpfd.Parser()

@p.on_recognize('The answer is {number:d}')
def two_word_test(number):
    print (type(number), number)

def int_parse1():
    p.parse_string('The answer is 42')


if __name__ == '__main__':
    int_parse1()