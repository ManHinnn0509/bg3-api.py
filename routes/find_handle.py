from fastapi import APIRouter, Depends, Request

import auth

from util.file_utils import read_json_file

from const import CASE_SENSITIVE

router = APIRouter(dependencies=[Depends(auth.get_api_key),])

'''
    Converted the xml files into json files, reasons:
    - It takes around 2 seconds to read 1 xml file
    - Easier to read

    So in here only json should be used
'''

ENGLISH_FILEPATH = './data/bg3/LocalizationFiles/english.json'
ZH_TW_FILEPATH = './data/bg3/LocalizationFiles/chinesetraditional.json'

JSON_ENGLISH: dict = read_json_file(ENGLISH_FILEPATH)
JSON_ZH_TW: dict = read_json_file(ZH_TW_FILEPATH)

@router.get('')
async def find_handle(request: Request, startswith: str=None, endswith: str=None, includes: str=None, equals: str=None):

    inputs = [i for i in (startswith, endswith, includes, equals) if (i != None)]
    if (len(inputs) == 0):
        return {}
    
    use_english = inputs[0].isascii()
    file = JSON_ENGLISH if (use_english) else JSON_ZH_TW

    if not (CASE_SENSITIVE):
        startswith = startswith.lower() if (startswith != None) else None
        endswith = endswith.lower() if (endswith != None) else None
        includes = includes.lower() if (includes != None) else None
        equals = equals.lower() if (equals != None) else None

    results = {}
    for handle, data in file.items():
        data: dict
        
        text: str = data['text']
        if not (CASE_SENSITIVE):
            text = text.lower()

        if (startswith != None):
            if not (text.startswith(startswith)):
                continue
        
        if (endswith != None):
            if not (text.endswith(endswith)):
                continue
        
        if (includes != None):
            if not (includes in text):
                continue
        
        if (equals != None):
            if not (text == equals):
                continue
        
        data['url'] = str(request.url_for('find_by_handle')) + f'?handle={handle}'
        results[handle] = data
    
    return results