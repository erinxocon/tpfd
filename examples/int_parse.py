import tpfd

#instantiate parser
p = tpfd.Parser()

#set up a parse rule that searches for a number
@p.on_parse('The answer is {number:d}')
def two_word_test(number):
    print (type(number), number)

#parse the string for a number
def int_parse1():
    p.parse('The answer is 42')


if __name__ == '__main__':
    int_parse1()