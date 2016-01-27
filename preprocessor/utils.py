"""
preprocessor.utils
~~~~~~~~~~~~~~
This module includes utility methods which are used in Preprocessor
"""

from .constants import PRIORITISED_METHODS

class Util:

    def __init__(self):
        pass

    def get_worker_methods(self, object, prefix):
        all_methods = dir(object)
        relevant_methods = filter(lambda x: x.startswith(prefix), all_methods)
        prefixed_prioritised_methods = [prefix+m for m in PRIORITISED_METHODS]

        offset = 0
        for ind, pri_method in enumerate(prefixed_prioritised_methods):
            relevant_methods.remove(pri_method)
            relevant_methods.insert(offset+ind, pri_method)

        return relevant_methods