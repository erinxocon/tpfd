TPFD - Text Parsing Function Dispatcher
=======================================
.. image:: https://travis-ci.org/erinxocon/tpfd.svg?branch=master
    :target: https://travis-ci.org/erinxocon/tpfd
.. image:: https://img.shields.io/pypi/v/tpfd.svg?maxAge=2592000   
    :target: https://pypi.python.org/pypi/tpfd/
.. image:: https://img.shields.io/pypi/l/tpfd.svg?maxAge=2592000   
    :target: https://opensource.org/licenses/MIT

**TPFD** is an easy way to parse strings and execute functions depending on their contents.  

Inspired by `Flask <https://github.com/mitsuhiko/flask>`_ and using `Parse <https://github.com/r1chardj0n3s/parse>`_ under the hood, this allows you to decorate functions with grammar rules and if a pattern that matches one of your grammar rules is found, the function will be run with a set of keyword arguments you've specified passed to it!  Great for parsing logs and executing macros on what it finds! 

Examples
--------
.. code-block:: python

    Aniamls.txt
    Turtles are cool
    Sloths are cool
    Mosquitos are dumb

    >>> p  = tpfd.Parser()

    >>> @p.on_parse('{Animal} are cool')
        def main(animal):
            print('I like {0}.'.format(animal))
    
    >>> p.parse_file('animals.txt')
    'I like turtles.'
    'I like sloths.'

    >>> p.parse(['Turtles are cool', 'Sloths are cool', 'Mosquitos are dumb'])
    'I like turtles.'
    'I like sloths.'
	
    >>> p.parse('Sloths are cool')
    'I like sloths.'
	
    >>> p.parse('Mosquitos are dumb')
    None
    
    >>> @p.on_find('>{}<')
	def find_example(words):
    	print (words)
    
    >>> p.find_string('<p>the <b>bold</b> text</p>')
    'the bold text'

To Install
----------

::

    $ pip install tpfd

Notes
-----
Any format spec supported by parse is supported by this library since it's all parse under the hood.  
Example: ``{[field name]:[format spec]}``

Current Features
----------------

* Support for parsing text files
* Support for accepting generators that output text or ints
* Support for parsing unicode strings
* Supports parsing strings, ints and interator/generator's automagically with new ``parse`` method.  


TODO
----
* Expose custom types functionality that `Parse <https://github.com/r1chardj0n3s/parse>`_ already offers
