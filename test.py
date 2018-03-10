from tpfd import TPFD

t = TPFD()

@t.search_pattern('Python is a {} language')
def foo(data):
    print(data)

t.parse('http://python.org')