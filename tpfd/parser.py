"""
parser.py
This contains the main Parser class that can be instantiated to create rules.
"""
import logging
from .rules import RuleMap


class Parser(object):
    """
    Parser exposes a couple methods for reading in strings.
    Currently only parse_file is working.
    """

    def __init__(self):
        """Initalizer"""
        self.debug = False
        self._rule_map = RuleMap(list)

    def on_recognize(self, eventname):
        """
        Decorator for rules. Calls the associated functions when the rule
        is invoked via voice
        """
        def eventdecorator(func):
            """Event decorator closure thing"""
            self._rule_map.add_rule(eventname, func)
            return func
        return eventdecorator

    def parse_file(self, file):
        #raise NotImplamentedError()
        with open(file, 'r') as f:
            for line in f:
                self._rule_map.query(line)

    def iter_parse(self, iterable):
        for item in iterable:
            self._rule_map.query(item)

    def parse_string(self, string):
        if self.debug:
            logging.debug(string)
        return self._rule_map.query(string)
