import tpfd

#instantiate parser
p = tpfd.Parser()

#Set up a rule using a regular expression classifer
@p.on_parse('Bring {words:^} hand grenade.')
def multi_word_test(words):
    print (words)

#Test weird string statement
def word_parse():
    p.parse('Bring out           the       holy    hand grenade.')

if __name__ == '__main__':
    word_parse()