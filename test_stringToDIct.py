from StringToDIct import string_to_dict

__author__ = 'varg'

import unittest


class TestStringToDict(unittest.TestCase):
    def test_stringToDict_valid(self):
        the_dict = {'K': [{'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'}]}
        # pprint(the_dict) {'K': [{'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'}]}
        self.assertEqual(the_dict, string_to_dict("""{'K': [{'k1': 'v'},
                                                        {'k': 'v1'},
                                                        {'k2': 'v1'}]}"""))

    def test_stringToDict_invalid(self):
        the_dict = {'K': [{'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'}]}
        # pprint(the_dict) {'K': [{'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'}]}
        self.assertEqual(None, string_to_dict("""{'K': [{'k1': 'v'},
                                                        {'k: 'v1'},
                                                        {'k2': 'v1'}]}"""))


if __name__ == '__main__':
    unittest.main()
