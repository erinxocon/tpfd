import tpfd

p = tpfd.Parser()

@p.on_parse('{number:d}')
def two_word_test(number):
    if number < 5:
        print(number)

def iter_parse():
    p.parse(range(0,10))

if __name__ == '__main__':
    iter_parse()