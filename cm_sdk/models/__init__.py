import json
from json import JSONEncoder
from enum import Enum

__author__ = 'e0d'


class CloudManagerJSONEncoder(JSONEncoder):
    """
    A custom JSON encoder to provide transparent conversion between
    CloudManager JSON format and the Python classes that represent API
    objects in the SDK.
    """
    # credit
    # http://stackoverflow.com/questions/19053707/convert-snake-case-snake-case-to-lower-camel-case-lowercamelcase-in-python
    def to_camel_case(self, snake_str):
        # Deal with the case were @property creates class property 
        # keys with an initial '_'
        snake_str = snake_str.lstrip('_')
        # Split remaining name on '_'
        components = snake_str.split('_')
        return components[0].lower() + "".join(x.title() for x in components[1:])

    def default(self, o):  # pylint: disable=method-hidden
        if isinstance(o, CloudManagerEnum):
            return o.to_json()
        elif hasattr(o, "__dict__"):
            # converts class parameter names from snake case to camel case expected
            # by the API and prunes nulls
            return dict((self.to_camel_case(k), v) for k, v in o.__dict__.iteritems() if v)
        else:
            return None



class CommonEqualityMixin(object):
    """
    Mixin class to provide deep eqality as equivalence for API objects 
    """
    def __eq__(self, other):

        #
        # must be an instances of the same class
        #
        if not isinstance(other, self.__class__):
            return False

        # expectation that keys are the same breaks for entities
        # returned from the API
        my_keys, other_keys = (sorted(self.__dict__.keys()), sorted(other.__dict__.keys()))

        if not my_keys == other_keys:
            return False

        for k in my_keys:

            v0 = self.__dict__[k]
            v1 = other.__dict__[k]

            if v0 is not None:
                if isinstance(v0, list):

                    # Short circuit if the lists are not equal in length
                    if not len(v0) == len(v1):
                        return False

                    # Compare each item in the list
                    for item0, item1 in zip(v0, v1):
                        if not item0 == item1:
                            return False
                else:
                    if not v0 == v1:
                        return False
        return True


    def __ne__(self, other):
        return not self.__eq__(other)

class CloudManagerBase(CommonEqualityMixin):
    """
    Base class for python representations of API objects that provides
    utility methods for static initialization.
    """
    @classmethod
    def from_json(cls, json_in):

        _dict = json.loads(json_in)
        return cls.from_dict(_dict)

    @classmethod
    def from_dict(cls, dict_in):

        instance = cls()

        for k, v in dict_in.items():
            setattr(instance, k, v)
        return instance

    def to_json(self):
        return json.dumps(self, cls=CloudManagerJSONEncoder)

class CloudManagerEnum(Enum):

    def to_json(self):
        """
        Return the value of the current instance of the Enum for JSON
        serialization.
        """
        return str(self.value)
