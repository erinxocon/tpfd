#coding=utf-8
from collections import defaultdict
from requests_html import BaseParser
from typing import Text, List

import logging

# Sanity checking.
try:
    assert sys.version_info.major == 3
    assert sys.version_info.minor > 5
except AssertionError:
    raise RuntimeError('TPFD requires Python 3.6+!')



class RuleMap(defaultdict):
    def __init__(self, default_factory:List[Text] = list, *args, **dict):
        self.debug = True
        return super(RuleMap, self).__init__(default_factory, *args, **dict)

    def add_rule(self, rule, func):
        """Add rule to the rule map"""
            self[rule].append(func)


class TPFD(BaseParser):

    def __init__(self):
        super(TPFD, self).__init__()
        self.debug = False
        self._parse_rule_map = RuleMap()
        self._find_rule_map = RuleMap()
        self._xpath_rule_map = RuleMap()

    def search_pattern(self, template: str) - > callable:
        """
        Decorator for parse search pattern
        """
        def parse_decorator(func: callable) -> callable:
            self._parse_rule_map.add_rule(template, func)
            return func

        return parse_decorator


    def css_selector(self, selector: str, first: bool = False) -> callable:
        """
        Decorator for css selector rules.
        """
        def find_decorator(func: callable) -> callable:
            #self._find_rule_map.add_rule(eventname, func)
            return func
        return find_decorator


    def xpath(self, selector: str, first: bool = False) -> callable:
        """
        Decorator for xpath selector rules.
        """
        def find_decorator(func: callable) -> callable:
            #self._find_rule_map.add_rule(eventname, func)
            return func
        return find_decorator


    def parse(self, data: Text) - > None:
        self.
        self.search()
