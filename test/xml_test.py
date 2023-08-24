import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from util.file_utils import read_xml_file, read_json_file

english_filepath = './data/bg3/LocalizationFiles/english.xml'
zh_tw_filepath = './data/bg3/LocalizationFiles/chinesetraditional.xml'

import time

t = time.time()
xml = read_xml_file(english_filepath)
print(time.time() - t)

t = time.time()
json = read_json_file(english_filepath.replace(".xml", ".json"))
print(time.time() - t)