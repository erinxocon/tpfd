import tpfd

#instantiate parser
p = tpfd.Parser()

#set up a 2 word capture rule
@p.on_parse('The {noun} who say {thing}!')
def two_word_test(noun, thing):
    print (noun, thing)

#parse with two emoji
def utf_parse1():
    p.parse('The ???? who say ??!')

#parse with one emoji
def utf_parse2():
    p.parse('The ?? who say chipmunk!')

#parse with 2 emoji
def utf_parse3():
    p.parse('The ? who say ??!')

if __name__ == '__main__':
    utf_parse1()
    utf_parse2()
    utf_parse3()