from tpfd import TPFD
from requests_html import HTMLSession

session = HTMLSession()
response = session.get('http://python.org')

t = TPFD(response=response)

@t.search_pattern('Python is a {} language')
def foo(data):
    print(data)


@t.css_selector('#about', first=True)
def foo1(data):
    print(data.text)
    print(data.links)


t.parse()