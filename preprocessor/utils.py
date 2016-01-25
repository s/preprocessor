"""
preprocessor.utils
~~~~~~~~~~~~~~
This module includes utility methods which are used in Preprocessor
"""

class Util:

    def __init__(self):
        pass

    def get_worker_methods(self, object, prefix):
        all_methods = dir(object)
        relevant_methods = filter(lambda x: x.startswith(prefix), all_methods)
        return relevant_methods