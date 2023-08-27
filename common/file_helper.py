###############################
### Dianyi Jiang            ###
###############################

import os

def find_file(search_path, filename):
    result = []

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
            return ''.join(result)
    return None

def find_dir(search_path, path):
    result = []

    for root, dirs, files in os.walk(search_path):
        if path in dirs:
            result.append(os.path.join(root, path))
            return ''.join(result)
    return None

