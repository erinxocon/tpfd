import tpfd

#instantiate parser
p = tpfd.Parser()

#set up find rule, in this case anything inbetweeen a > and <
@p.on_find('>{}<')
def two_word_test(value):
    print(value)

#submit an iterator to the find method to get all the text in the html snippits.
def iter_find():
    l = ['<p>the <b>bold</b> text</p>', '<p>the <i>italicized</i> text</p>', '<p>the <u>underlined</u> text</p>']
    p.find(l)

if __name__ == '__main__':
    iter_find()
