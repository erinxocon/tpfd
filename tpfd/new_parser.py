# Sanity checking.
try:
    assert sys.version_info.major == 3
    assert sys.version_info.minor > 5
except AssertionError:
    raise RuntimeError('TPFD requires Python 3.6+!')

import requests_html as req

#coding=utf-8

"""
parser.py
This contains the main Parser class that can be instantiated to create rules.
"""
from .rules import RuleMap
from .compat import basestring


class Rules(object):
    """
    Parser exposes a couple methods for reading in strings.
    Currently only parse_file is working.
    """

    def __init__(self):
        """Initalizer"""
        self.debug = False
        self._parse_rule_map = RuleMap(list)
        self._find_rule_map = RuleMap(list)
        self._xpath_rule_map = RuleMap(list)

    def search(self, eventname):
        """
        Decorator for text parsing rules.
        """
        def parse_decorator(func):
            """Event decorator closure thing"""
            self._parse_rule_map.add_rule(eventname, func)
            return func
        return parse_decorator


    def find(self, eventname):
        """
        Decorator for css selector rules.
        """
        def find_decorator(func):
            """Event decorator closure thing"""
            self._find_rule_map.add_rule(eventname, func)
            return func
        return find_decorator


    def xpath(self, eventname):
        """
        Decorator for xpath selector rules.
        """
        def find_decorator(func):
            """Event decorator closure thing"""
            self._find_rule_map.add_rule(eventname, func)
            return func
        return find_decorator