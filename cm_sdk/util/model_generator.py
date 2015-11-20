from cm_sdk.models.common.common import CloudManagerBase
from cm_sdk.models.common.string_utils import to_snake_case

__author__ = 'e0d'

import json
import os
import argparse

CLASS_TEMPLATE = """
from cm_sdk.models import CloudManagerBase

class {class_name}(CloudManagerBase):
    children = {{}}
    my_api_attributes = [{my_attributes}]

    def __init__(self, {constructor_args}):
        CloudManagerBase.__init__(self, self.my_api_attributes)
        {attributes_setters}

"""


class ModelGenerator:
    """
    Convenience utility for generating model classes from JSON
    """
    def __init__(self, json_exemplar):
        self.exemplar = json_exemplar

    @classmethod
    def convert_keys(cls, keys):
        to_return = []
        for key in keys:
            snake_key = to_snake_case(key)

            if snake_key not in CloudManagerBase.COMMON_API_ATTRIBUTES:
                to_return.append(snake_key)
        return to_return

    def generate_model(self):

        with open(self.exemplar) as exemplar_file:
            exemplar = json.load(exemplar_file)

        model_keys = [k for k in exemplar]

        cleaned_keys = self.convert_keys(model_keys)

        cleaned_keys.sort()
        my_attributes = []
        constructor_args = []
        attributes_setters = []

        for key in cleaned_keys:

            constructor_args.append("{key} = None".format(key=key))
            my_attributes.append("\'{key}\'".format(key=key))
            attributes_setters.append("self.{key} = {key}".format(key=key))

        setters = os.linesep.join(attributes_setters)
        class_name = os.path.splitext(os.path.basename(args.json_exemplar))[0]

        return CLASS_TEMPLATE.format(class_name=class_name,
                                     my_attributes=",".join(my_attributes),
                                     constructor_args=", ".join(constructor_args),
                                     attributes_setters=setters)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json-exemplar', help='the path to the exemplar JSON file.')
    args = parser.parse_args()

    mg = ModelGenerator(args.json_exemplar)

    print mg.generate_model()
