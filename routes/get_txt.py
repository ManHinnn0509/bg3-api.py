import os

from fastapi import APIRouter, Depends, Request, Response

import auth

from util.file_utils import read_file
from util.str_utils import split_on_empty_lines

router = APIRouter(dependencies=[Depends(auth.get_api_key),])

TXT_PATHS = [
    './data/bg3/Gustav/Public/Gustav/Stats/Generated/',
    './data/bg3/Gustav/Public/Gustav/Stats/Generated/Data/',
    
    './data/bg3/Gustav/Public/GustavDev/Stats/Generated/',
    './data/bg3/Gustav/Public/GustavDev/Stats/Generated/Data/',
    
    './data/bg3/Shared/Public/Shared/Stats/Generated/',
    './data/bg3/Shared/Public/Shared/Stats/Generated/Data/',
    
    './data/bg3/Shared/Public/SharedDev/Stats/Generated/',
    './data/bg3/Shared/Public/SharedDev/Stats/Generated/Data/',
]

CONTENTS = {}
for path in TXT_PATHS:
    d = {}
    files = [i for i in os.listdir(path) if (i.endswith('.txt'))]
    for filename in files:
        filepath = path + filename
        content = read_file(filepath)
        items = split_on_empty_lines(content)

        d[filename] = items
    
    CONTENTS[path] = d

@router.get('')
async def get_txt(request: Request, mapKey: str=None):
    if (mapKey == None):
        return None
    
    result = {}
    for path, files in CONTENTS.items():
        path: str
        files: dict

        d = {}
        for filename, contents in files.items():
            for content in contents:
                content: str

                if (mapKey not in content):
                    continue
                
                if (filename not in d):
                    d[filename] = []
                
                # Split it into lines, since there might be multiple results
                content = content.split("\n")
                d[filename].append(content)

        if (len(d) != 0):
            short_path = path.split('bg3/')[-1]
            result[short_path] = d
    
    return result