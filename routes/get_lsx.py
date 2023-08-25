import os

from fastapi import APIRouter, Depends, Request, Response

import auth

from util.file_utils import read_file

router = APIRouter(dependencies=[Depends(auth.get_api_key),])

LSX_DIRS = [
    './data/bg3/Gustav/Public/Gustav/RootTemplates/',
    './data/bg3/Gustav/Public/GustavDev/RootTemplates/',
    './data/bg3/Shared/Public/Shared/RootTemplates/',
    './data/bg3/Shared/Public/SharedDev/RootTemplates/',
]

CONTENTS = {dir:[i for i in os.listdir(dir) if (i.endswith('.lsx'))] for dir in LSX_DIRS}

@router.get('')
async def get_lsx(request: Request, mapKey: str=None):

    if (mapKey == None):
        return {}
    
    target_filename = mapKey + '.lsx'
    for dir, contents in CONTENTS.items():
        if (target_filename in contents):
            s = read_file(dir + target_filename)
            return Response(content=s, media_type="application/xml")

    return {}