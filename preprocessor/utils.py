"""
preprocessor.utils
~~~~~~~~~~~~~~
This module includes utility methods which are used in Preprocessor
"""

from .defines import Defines

class Utils:

    def __init__(self):
        pass

    def get_worker_methods(self, object, prefix):
        all_methods = dir(object)
        relevant_methods = list(filter(lambda x: x.startswith(prefix), all_methods))

        # Filtering according to user's options
        prefixed_filtered_methods = [prefix+fm for fm in Defines.FILTERED_METHODS]
        filtered_methods = list(filter(lambda x: x in prefixed_filtered_methods, relevant_methods))

        # Prioritising
        offset = 0
        for ind, pri_method in enumerate(Defines.PRIORITISED_METHODS):
            prefixed_pri_method = prefix + pri_method
            if pri_method in filtered_methods:
                filtered_methods.remove(prefixed_pri_method)
                filtered_methods.insert(offset+ind, prefixed_pri_method)

        return filtered_methods