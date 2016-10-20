import tpfd

#instantiate parser
p = tpfd.Parser()

#look for a number type, if less than 5 print
@p.on_parse('{number:d}')
def two_word_test(number):
    if number < 5:
        print(number)

#provide generator to parse method to print out numbers
def iter_parse():
    p.parse(range(0,10))

if __name__ == '__main__':
    iter_parse()