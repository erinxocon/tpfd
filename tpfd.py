#coding=utf-8
from collections import defaultdict
from requests_html import HTMLResponse
from typing import Text, List

import requests
import logging
import sys

# Sanity checking.
try:
    assert sys.version_info.major == 3
    assert sys.version_info.minor > 5
except AssertionError:
    raise RuntimeError('TPFD requires Python 3.6+!')


class Rule:

    def __init__(self, rule: Text, func: callable, rule_type: Text, first: bool = False) -> None:
        self._rule = rule
        self._func = func
        self._rule_type = rule_type
        self._first = first


    @property
    def rule(self) -> Text:
        return self._rule


    @property
    def function(self) -> callable:
        return self._func


    @property
    def rule_type(self) -> Text:
        return self._rule_type


    @property
    def first(self) -> bool:
        return self._first


class TPFD:

    def __init__(self, response: HTMLResponse) -> None:
        self.debug = False
        self._rules = []
        self._response = response


    @property
    def rules(self) -> List:
        return self._rules


    @property
    def response(self) -> HTMLResponse:
        return self._result


    @response.setter
    def response(self, response: HTMLResponse) -> None:
        self._response = response


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
            self._rules.append(Rule(selector, func, 'find', first))
            return func

        return find_decorator


    def xpath(self, selector: str, first: bool = False) -> callable:
        """
        Decorator for xpath selector rules.
        """
        def find_decorator(func: callable) -> callable:
            self._rules.append(Rule(selector, func, 'xpath', first))
            return func

        return xpath_decorator


    def parse(self) -> None:

        for i in self._rules:

            if i.rule_type is 'search':
                r = self._response.html.search(i.rule)

                if r is not None:
                    i.function(r[0])

            if i.rule_type is 'find':
                r = self._response.html.find(i.rule, first=i.first)

                if r is not None:
                    i.function(r)
