import logging
#coding=utf-8

from collections import defaultdict
from parse import parse
from parse import findall


class RuleMap(defaultdict):
    def __init__(self, default_factory, *args, **dict):
        self.debug = True
        return super(RuleMap, self).__init__(default_factory, *args, **dict)

    def add_rule(self, rule, func):
        """Add rule to the rule map"""
        try:
            self[rule.lower()].append(func)
        except AttributeError:
            self[rule].append(func)

    def query_parse(self, string):
        """
        Method that looks in the function registry
        to see if input text is a rule
        """

        #set up an empty key registry
        key_registry = []

        try:
            #run through all keys and try and parse against them
            for key in self.keys():

                key_registry.append({'key': key, 'parse_resp': parse(key, str(string).lower())})

            #get rid of false keys or None responses
            key_registry = [x for x in key_registry if x['parse_resp'] is not None]

            #get key from registry
            for i in key_registry:

                #qury self dictionary for matching key and function
                for func in self.get(i['key']):

                    return func(**i['parse_resp'].named)

        except KeyError as error:
            logging.debug("Rule '{0} not found or matched.'".format(error))


    def query_find(self, string):

        #set up an empty key registry
        key_registry = []

        #run through all keys and try and parse against them
        for key in self.keys():

            key_registry.append({'key': key, 'find_resp': findall(key, str(string).lower())})

        #get rid of false keys or None responses
        key_registry = [x for x in key_registry if x['find_resp'] is not None]

        joined = ''

        #get key from registry and unpack it's associated response
        for i in key_registry:

            for j in i['find_resp']:

                joined += j[0]

            #qury self dictionary for matching key and function
            for func in self.get(i['key']):

                return func(joined)



