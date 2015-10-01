__author__ = 'varg'


def insert_to_brackets(v):
    return "['" + str(v) + "']"


def find_key(data_structure, key):
    if isinstance(data_structure, list) or isinstance(data_structure, tuple):
        for i in range(0, len(data_structure)):
            path = find_key(data_structure[i], key)
            if path:
                return "[" + str(i) + "]" + path

    if isinstance(data_structure, dict):
        for dkey in data_structure:
            if key == dkey:
                return insert_to_brackets(key)

            dkey_path = find_key(data_structure[dkey], key)
            if dkey_path:
                return insert_to_brackets(dkey) + dkey_path

    return None
