import logging
import collections

class RuleMap(collections.defaultdict):
    def __init__(self, default_factory, *args, **dict):
        return super().__init__(default_factory, *args, **dict)


    def add_rule(self, rule, func):
        self[rule.lower()].append(func)


    def query(self, string):
        """
        Default allback that looks in the function registry
        to see if the spoken text is a rule
        """

        key_registry = []
        try:
            for key in self.keys():
                key_registry.append({'key': key, 
                                        'parse_resp': parse(key, string.lower())})

            key_registry = [x for x in key_registry if x['parse_resp']]

            for i in key_registry: 
                for func in self.get(i['key']):
                    func(i['parse_resp'].named)

        except KeyError as error:
            logging.debug("Rule '{0} not found or matched.'".format(error))


class Rule(object):
    pass