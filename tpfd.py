#coding=utf-8
from collections import defaultdict
from requests_html import BaseParser
from typing import Text, List

import logging
import sys

# Sanity checking.
try:
    assert sys.version_info.major == 3
    assert sys.version_info.minor > 5
except AssertionError:
    raise RuntimeError('TPFD requires Python 3.6+!')



class Rule:

    def __init__(self, rule: Text, func: callable, rule_type: Text) -> None:
        self._rule = rule
        self._func = func
        self._rule_type = rule_type

    @property
    def rule(self) -> Text:
        return self._rule

    @property
    def function(self) -> callable:
        return self._func

    @property
    def rule_type(self) -> Text:
        return self._rule_type




class TPFD:

    def __init__(self):
        self.debug = False
        self._rules = []

    @property
    def rules(self)  -> List:
        return self._rules


    def search_pattern(self, template: Text) -> callable:
        """
        Decorator for parse search pattern
        """
        def parse_decorator(func: callable) -> callable:
            self._rules.append(Rule(template, func, 'search'))
            return func

        return parse_decorator


    def css_selector(self, selector: Text, first: bool = False) -> callable:
        """
        Decorator for css selector rules.
        """
        def find_decorator(func: callable) -> callable:
            self._rules.append(Rule(selector, func, 'find'))
            return func

        return find_decorator


    def xpath(self, selector: str, first: bool = False) -> callable:
        """
        Decorator for xpath selector rules.
        """
        def find_decorator(func: callable) -> callable:
            self._rules.append(Rule(selector, func, 'xpath'))
            return func

        return find_decorator


    def parse(self, data: Text) -> None:
        pass



