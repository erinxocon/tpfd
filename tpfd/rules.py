import logging
#coding=utf-8

from collections import defaultdict
from parse import parse


class RuleMap(defaultdict):
    def __init__(self, default_factory, *args, **dict):
        self.debug = True
        return super(RuleMap, self).__init__(default_factory, *args, **dict)

    def add_rule(self, rule, func):
        try:
            self[rule.lower()].append(func)
        except AttributeError:
            self[rule].append(func)

    def query(self, string):
        """
        Default allback that looks in the function registry
        to see if the spoken text is a rule
        """
        if self.debug:
            logging.debug(string)

        key_registry = []
        try:
            for key in self.keys():
                try:
                    key_registry.append({'key': key, 'parse_resp': parse(key, string.lower())})
                except AttributeError:
                    key_registry.append({'key': key, 'parse_resp': parse(key, str(string))})

            key_registry = [x for x in key_registry if x['parse_resp']]

            if self.debug:
                logging.debug(key_registry)

            for i in key_registry:
                for func in self.get(i['key']):
                    if self.debug:
                        logging.debug(i['parse_resp'].named)
                        logging.debug(func)
                    return func(**i['parse_resp'].named)

        except KeyError as error:
            logging.debug("Rule '{0} not found or matched.'".format(error))


class Rule(object):
    pass
