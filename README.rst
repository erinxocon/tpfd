TPFD - Text Based Function Dispatcher
=====================================

.. code-block:: python

    Aniamls.txt
    Turtles are cool
    Sloths are cool
    Mosquitos are dumb

    >>> p  = tpfd.Parser()

    >>> @p.on_recognize('{Animal} are cool')
        def main(kwargs):
            animal = kwargs.get('animal')
            print('I like {0}.'.format(animal))
    
    >>> p.parse_file('animals.txt')
    'I like turtles.'
    'I like sloths.'


Tpfd is an easy way to parse strings and execute functions depending on their contents.  Inspired by `flask <https://github.com/mitsuhiko/flask>`_ and using `parse <https://github.com/r1chardj0n3s/parse>`_ under the hood, this allows you to decorate functions with grammar rules and if a pattern that matches one of your grammar rules is found, the function will be run with a set of keyword arguments you've specified passed to it!  Great for parsing logs and executing macros on what it finds!

Current Features
----------------

* Support for parsing text files
* Support for accepting generators that output text.


TODO
----
* Support streams
* various built in converters to translate numbers/day names/dates