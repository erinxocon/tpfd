#coding=utf-8

"""
parser.py
This contains the main Parser class that can be instantiated to create rules.
"""
from .rules import RuleMap
from .compat import basestring


class Parser(object):
    """
    Parser exposes a couple methods for reading in strings.
    Currently only parse_file is working.
    """

    def __init__(self):
        """Initalizer"""
        self.debug = False
        self._parse_rule_map = RuleMap(list)
        self._find_rule_map = RuleMap(list)


    def on_parse(self, eventname):
        """
        Decorator for rules. Calls the associated functions when the rule
        is invoked via parse found
        """
        def parse_decorator(func):
            """Event decorator closure thing"""
            self._parse_rule_map.add_rule(eventname, func)
            return func
        return parse_decorator


    def on_find(self, eventname):
        """
        Decorator for rules. Calls the associated functions when the rule
        is invoked via parse found
        """
        def find_decorator(func):
            """Event decorator closure thing"""
            self._find_rule_map.add_rule(eventname, func)
            return func
        return find_decorator


    def parse_file(self, file):
        """Parses through a file"""
        with open(file, 'r') as f:
            for line in f:
                self._parse_rule_map.query_parse(line)


    def iter_parse(self, iterable):
        """Parses an interator/generator"""
        for item in iterable:
            self._parse_rule_map.query_parse(item)


    def parse_string(self, string):
        """Parses and int or string"""
        return self._parse_rule_map.query_parse(string)


    def parse(self, item):
        """Magical method that automatically chooses parse string or iter parse"""
        if isinstance(item,  basestring):
            return self.parse_string(item)
        else:
            self.iter_parse(item)


    def find_string(self, string):
        """finds an int or string based on input pattern"""
        return self._find_rule_map.query_find(string)


    def iter_find(self, iterable):
        """Finds an string based on an input pattern and interable/generator"""
        for item in iterable:
            self._find_rule_map.query_find(item)


    def find_file(self, file):
        """find a string based on an input pattern from a file"""
        with open(file, 'r') as f:
            for line in f:
                self._parse_rule_map.query_parse(line)


    def find(self, item):
        """Magical method that chooses between iter_find and find_string"""
        if isinstance(item,  basestring):
            return self.find_string(item)
        else:
            self.iter_find(item)
