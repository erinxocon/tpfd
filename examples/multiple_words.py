import tpfd

p = tpfd.Parser()

@p.on_recognize('Bring {words:^} hand grenade.')
def multi_word_test(words):
    print (words)

def word_parse():
    p.parse('Bring out           the       holy    hand grenade.')

if __name__ == '__main__':
    word_parse()