import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from util.file_utils import read_xml_file, write_json_file

english_filepath = './data/bg3/LocalizationFiles/english.xml'
zh_tw_filepath = './data/bg3/LocalizationFiles/chinesetraditional.xml'

filepath = english_filepath
xml = read_xml_file(filepath)

contents = xml.getElementsByTagName('content')

d = {}
for content in contents:
    handle = content.attributes['contentuid'].value
    version = content.attributes['version'].value
    text = content.firstChild.data

    d[handle] = {
        'text': text,
        'version': int(version)
    }

print(
    write_json_file(
        filepath.replace('.xml', '.json'),
        d
    )
)