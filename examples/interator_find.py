import tpfd

p = tpfd.Parser()

@p.on_find('>{}<')
def two_word_test(value):
    print(value)

def iter_find():
    l = ['<p>the <b>bold</b> text</p>', '<p>the <i>italicized</i> text</p>', '<p>the <u>underlined</u> text</p>']
    p.find(l)

if __name__ == '__main__':
    iter_find()
