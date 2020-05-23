# -*- coding: utf-8 -*-
"""
preprocessor.utils
~~~~~~~~~~~~~~
This module includes utility methods which are used in Preprocessor
"""

import json
import random
import string
from os import path
from datetime import datetime
from .defines import Defines, InputFileType


def get_worker_methods(obj, prefix):
    all_methods = dir(obj)
    relevant_methods = list(filter(lambda x: x.startswith(prefix), all_methods))

    # Filtering according to user's options
    prefixed_filtered_methods = [prefix + fm for fm in Defines.FILTERED_METHODS]
    filtered_methods = list(filter(lambda x: x in prefixed_filtered_methods, relevant_methods))

    # Prioritising
    offset = 0
    for ind, pri_method in enumerate(Defines.PRIORITISED_METHODS):
        prefixed_pri_method = prefix + pri_method
        if pri_method in filtered_methods:
            filtered_methods.remove(prefixed_pri_method)
            filtered_methods.insert(offset + ind, prefixed_pri_method)

    return filtered_methods


def get_file_contents(file_path):
    """
    Returns the type of the file in InputFileType enum type
        if the file exists at given path.
    :param file_path: Absolute path for the file.
    :return: file_type (json, text, unsupported)
    :rtype: InputFileType or None
    :raises: This method raises OSError if it cannot read file_path.
    """
    if not path.exists(file_path):
        return None
    file_ext = get_file_extension(file_path)
    if InputFileType.json == file_ext:
        return get_json_file_contents(file_path)
    else:
        return get_text_file_contents(file_path)


def get_json_file_contents(file_path):
    """
    Returns contents of a JSON file as a string array.
    :param file_path: Absolute path for the file.
    :return: str array or None
    :rtype: List<str>
    :raises: This method raises OSError if it cannot read file_path.
    """
    with open(file_path, encoding='utf-8') as handler:
        return json.load(handler)


def get_text_file_contents(file_path):
    """
    Returns contents of a JSON file as a string array.
    :param file_path: Absolute path for the file.
    :return: str array or None
    :rtype: List<str>
    :raises: This method raises OSError if it cannot read file_path.
    """
    with open(file_path, encoding='utf-8') as handler:
        content = handler.readlines()
        return [line.rstrip("\n") for line in content]


def get_file_extension(file_path):
    """
    Returns extension for a given file path.
    :param file_path: Absolute path for the file.
    :return: file extension
    :rtype: str
    """
    components = list(filter(None, path.splitext(file_path)))
    if len(components) == 1 and not components[0].startswith("."):
        return None

    return components[-1] if len(components) > 0 else None


def write_to_output_file(file_path, file_contents, add_timestamp=False):
    """
    Writes the given file_contents to the file_path directory in given file format
    if current user's permissions grants to do so.
    :param file_path: str: Absolute path for the file
    :param file_contents: List<str>: Contents of the file
    :param add_timestamp: If True, adds current timestamp to the filename
    :return: Output path
    :rtype: str
    :raises: ValueError if file_format is neither json nor text.
    """
    file_format = get_file_extension(file_path)
    if not file_format:
        raise ValueError('Given file path:'+file_path+' does not have a file name and extension.')

    output_file_path = generate_random_file_name(file_path, add_timestamp)
    if InputFileType.json == file_format:
        return write_to_json_file(output_file_path, file_contents)
    elif InputFileType.text == file_format:
        return write_to_text_file(output_file_path, file_contents)
    else:
        raise ValueError('Unrecognized file format. '
                         'Cannot write to file path:'+file_path+' in '+file_format+' format.')


def write_to_json_file(file_path, file_contents):
    """
    Writes the given file_contents to the file_path in JSON format if current
    user's permissions grants to do so.
    :param file_path: Absolute path for the file
    :param file_contents: Contents of the output file
    :return: Output path
    :rtype: str
    :raises: This method raises OSError if it cannot write to file_path.
    """
    with open(file_path, mode='w', encoding='utf-8') as handler:
        json.dump(file_contents, handler)
    return file_path


def write_to_text_file(file_path, file_contents):
    """
    Writes the given file_contents to the file_path in text format
    if current user's permissions grants to do so.
    :param file_path: Absolute path for the file
    :param file_contents: List<str> List of lines
    :return: void
    :rtype: void
    :raises: This method raises OSError if it cannot write to file_path.
    """
    with open(file_path, mode='w', encoding='utf-8') as handler:
        for line in file_contents:
            handler.write("%s\n" % line)
    return file_path


def generate_random_file_name(file_path, add_timestamp=False):
    """
    Generates a random file name for the given absolute file path.
    :param file_path: Absolute path for the file
    :param add_timestamp: If True, adds current timestamp to the filename
    :return: Absolute path for the file with a random file name
    :rtype: str
    """
    file_path_components = list(path.split(file_path))
    if len(file_path_components) == 0 or len(file_path) == 0:
        raise ValueError('Found faulty file path: ' + file_path + ' while trying to write to JSON file.')

    random_file_name = generate_random_alphanumeric_string()
    if add_timestamp:
        timestamp_str = get_current_timestamp("%d%m%Y_%H%M%S%f")
        random_file_name = timestamp_str + "_" + random_file_name

    file_name = random_file_name + "_" + file_path_components[-1]
    file_path_components[-1] = file_name
    return path.join(*file_path_components)


def generate_random_alphanumeric_string(str_length=12):
    """
    Generates a random string of length: str_length
    :param str_length: Character count of the output string
    :return: Randomly generated string
    :rtype: str
    """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(str_length)))


def are_lists_equal(lhs_list, rhs_list):
    """
    Compares two lists element by element and returns True if all of them are equal.
    :param lhs_list: First list to compare
    :param rhs_list: Second list to compare
    :return: True if lists are equal. False otherwise.
    :rtype: bool
    """
    if not isinstance(lhs_list, list) or not isinstance(rhs_list, list):
        raise ValueError("One of the parameters isn't type of list.")
    lhs = []
    rhs = []

    if len(lhs_list) < len(rhs_list):
        lhs = rhs_list
        rhs = lhs_list
    return len((list(set(lhs) - set(rhs)))) == 0


def get_current_timestamp(format_specifier):
    """
    Returns current date and time in specified format
    :param format_specifier: format specifier for the date time object
    :return: Formatted date time string
    :rtype: str
    """
    date_time = datetime.now()
    return date_time.strftime(format_specifier)
