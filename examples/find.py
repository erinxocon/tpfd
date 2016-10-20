import tpfd

#instantiate parser
p = tpfd.Parser()

#set up find rule, in this case anything inbetweeen a > and <
@p.on_find('>{}<')
def find_example(words):
    print (words)

#parse a string to evaluate against find rules
def find_string():
    p.find('<p>the <b>bold</b> text</p>')


if __name__ == '__main__':
    find_string()