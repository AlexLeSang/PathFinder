from Finder import find_key

__author__ = 'varg'

import unittest


class FinderTest(unittest.TestCase):
    def test_no_key_in_dict(self):
        data_structure = {'k': 'v'}
        k = 'a'
        self.assertEqual(None, find_key(data_structure, k))

    def test_key_in_dict(self):
        data_structure = {'k': 'v'}
        k = 'k'
        self.assertEqual("['k']", find_key(data_structure, k))

    def test_key_in_list(self):
        data_structure = [{'k1': 'v'}, {'k1': 'v1'}, {'k': 'v1'}]
        k = 'k'
        self.assertEqual("[2]['k']", find_key(data_structure, k))

    def test_key_in_tuple(self):
        data_structure = ({'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'})
        k = 'k'
        self.assertEqual("[1]['k']", find_key(data_structure, k))

    def test_key_in_nested_dict(self):
        data_structure = {'K': {'k': 'v'}}
        k = 'k'
        self.assertEqual("['K']['k']", find_key(data_structure, k))

    def test_key_in_list_nested_dict(self):
        data_structure = {'K': [{'k1': 'v'}, {'k': 'v1'}, {'k2': 'v1'}]}
        k = 'k'
        self.assertEqual("['K'][1]['k']", find_key(data_structure, k))


if __name__ == '__main__':
    unittest.main()
