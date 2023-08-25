import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import xmltodict

from util.file_utils import read_json_file, read_xml_file, write_json_file

dirs = [
    r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Modders-Multitool\UnpackedData\Gustav\Public\Gustav\RootTemplates\cvt',
    r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Modders-Multitool\UnpackedData\Gustav\Public\GustavDev\RootTemplates\cvt',
    r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Modders-Multitool\UnpackedData\Shared\Public\Shared\RootTemplates\cvt',
    r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Modders-Multitool\UnpackedData\Shared\Public\SharedDev\RootTemplates\cvt'
]

counter = 1
for dir in dirs:
    d = {}
    xmls = [f'{dir}\\{i}' for i in os.listdir(dir)]
    for xml in xmls:
        with open(xml, 'rb') as f:
            b = f.read()
        
        data = xmltodict.parse(b)

        # Check if this xml file is just an empty template
        try:
            attributes = data['save']['region']['node']['children']['node']['attribute']
        except Exception as e:
            # print(e)
            # print(xml)
            pass
    
        attributes_with_handle = []

        for attribute in attributes:
            if (attribute['@id'] == 'MapKey'):
                map_key = attribute['@value']
            
            if ('@handle' in attribute):
                attributes_with_handle.append(attribute)

        d[map_key] = attributes_with_handle
    
    write_json_file(f'./{counter}.json', d)
    counter += 1
    
        

    