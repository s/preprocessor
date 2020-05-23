# -*- coding: utf-8 -*-

import os
import random
import unittest
import platform
import preprocessor as p


class UtilsTest(unittest.TestCase):
    _test_dictionary = {
        "key": "value",
        "_key": "_val"
    }
    _test_file_contents = [
        'Preprocessor now supports files. https://github.com/s/preprocessor',
        '#preprocessing is a cruical part of @ML projects.',
        '@RT @Twitter raw text data usually has lots of #residue. http://t.co/g00gl',
        '#emoji #smiley 😀😍 https://emojipedia.org'
    ]
    _current_dir = ""
    _output_file_name_prefix = "test_utils_output_"
    _artifact_dir_name = "artifacts"

    def setUp(self):
        self._current_dir = os.path.dirname(__file__)
        self._artifacts_dir = os.path.join(self._current_dir, self._artifact_dir_name)

    def test_get_file_extension(self):
        self.assertEqual(p.get_file_extension("file.txt"), ".txt")
        self.assertEqual(p.get_file_extension("file.xcodeproj"), ".xcodeproj")
        self.assertEqual(p.get_file_extension(".gitignore"), ".gitignore")
        self.assertEqual(p.get_file_extension("..."), "...")
        self.assertEqual(p.get_file_extension(""), None)
        self.assertEqual(p.get_file_extension("_.abc"), ".abc")
        self.assertIsNone(p.get_file_extension("/a/b/c"))

    def test_write_to_output_file(self):
        # Test invalid directory
        invalid_dir = os.path.join(self._current_dir, "/a/b/c")
        self.assertRaises(ValueError, p.write_to_output_file, invalid_dir, [])

        # Test protected directories on macOS and Linux
        # (Travis CI disables Windows Defender)
        if not self._is_running_on_windows():
            protected_directory = "/"
            output_file_name = self._output_file_name_prefix + "test_write_to_output_file.json"
            full_input_path = os.path.join(protected_directory, output_file_name)

            # Test file wasn't created due to protected directory
            self.assertRaises(OSError, p.write_to_json_file, full_input_path, {})

    def test_write_to_json_file(self):
        # Test file was created
        output_path = self._write_test_contents_to_cur_dir(p.InputFileType.json)
        self.assertTrue(os.path.exists(output_path))

        output_file_name = self._output_file_name_prefix + "dictionary.json"
        full_output_file_path = os.path.join(self._artifacts_dir, output_file_name)
        full_input_path = os.path.join(self._current_dir, full_output_file_path)
        output_path = p.write_to_json_file(full_input_path, self._test_dictionary)
        file_contents = p.get_json_file_contents(output_path)

        # Check the contents of written file is same as the one defined in this class
        self.assertEqual(file_contents["key"], self._test_dictionary["key"])
        self.assertEqual(file_contents["_key"], self._test_dictionary["_key"])

    def test_write_to_text_file(self):
        # Test file was created
        output_path = self._write_test_contents_to_cur_dir(p.InputFileType.text)
        self.assertTrue(os.path.exists(output_path))

        file_contents = p.get_file_contents(output_path)
        # Check the contents of written file is same as the one defined in this class
        p.are_lists_equal(file_contents, self._test_file_contents)

    def test_generate_random_file_name(self):
        output_file_name = self._output_file_name_prefix + "test_generate_random_file_name.json"
        full_output_file_path = os.path.join(self._artifacts_dir, output_file_name)
        file_path = os.path.join(self._current_dir, full_output_file_path)
        gen_path = p.generate_random_file_name(file_path)
        self.assertNotEqual(file_path, gen_path)

        file_path_ext = p.get_file_extension(file_path)
        gen_path_ext = p.get_file_extension(gen_path)
        self.assertEqual(file_path_ext, gen_path_ext)

        l_path_excl_file = os.path.split(file_path)
        self.assertTrue(len(l_path_excl_file) > 0)

        r_path_excl_file = os.path.split(gen_path)
        self.assertTrue(len(r_path_excl_file) > 0)

        self.assertEqual(l_path_excl_file[0], r_path_excl_file[0])

    def test_generate_random_alphanumeric_string(self):
        empty_str = p.generate_random_alphanumeric_string(str_length=0)
        self.assertEqual(len(empty_str), 0)

        output_str = p.generate_random_alphanumeric_string(str_length=100)
        self.assertEqual(len(output_str), 100)

        str_len = random.choice(range(4, 32))
        iteration_count = random.choice(range(1, 128))
        for i in range(1, iteration_count):
            lhs = p.generate_random_alphanumeric_string(str_length=str_len)
            rhs = p.generate_random_alphanumeric_string(str_length=str_len)
            self.assertNotEqual(lhs, rhs)

    def test_are_lists_equal(self):
        self.assertTrue(p.are_lists_equal([], []))
        self.assertFalse(p.are_lists_equal([], [1]))
        self.assertRaises(ValueError, p.are_lists_equal, "", [])
        self.assertTrue(p.are_lists_equal([[]], []))
        self.assertTrue(p.are_lists_equal([[2]], [2]))
        self.assertTrue(p.are_lists_equal(["Test"], ["Test"]))

    def _is_running_on_windows(self):
        return not platform.system() in ["Linux", "Darwin"]

    def _write_test_contents_to_cur_dir(self, ext):
        output_file_name = self._output_file_name_prefix + "_write_test_contents_to_cur_dir" + ext
        full_input_path = os.path.join(self._artifacts_dir, output_file_name)
        if p.InputFileType.json == ext:
            return p.write_to_json_file(full_input_path, self._test_file_contents)
        elif p.InputFileType.text == ext:
            return p.write_to_text_file(full_input_path, self._test_file_contents)


if __name__ == '__main__':
    unittest.main()
