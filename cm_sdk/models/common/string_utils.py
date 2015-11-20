from enum import Enum
import re

__author__ = 'e0d'


class Case(Enum):
    CAMEL = 1
    SNAKE = 2


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0].lower() + "".join(x.title() for x in components[1:])


def to_snake_case(camel):
    regex = re.compile(r'([A-Z])')
    return regex.sub(r'_\1', camel).lower()


def convert_dict_keys(dict_in, target_case=None):
    _renamed = {}

    if target_case == Case.CAMEL:
        converter = lambda name: to_camel_case(name)
        pass
    elif target_case == Case.SNAKE:
        converter = lambda name: to_snake_case(name)
    else:
        raise NotImplemented("Unsupported target case, {0}, provided.".format(target_case))

    for k, v in dict_in.items():
        _renamed[converter(k)] = v

    return _renamed