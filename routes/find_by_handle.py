from fastapi import APIRouter, Depends, Request

import auth

from util.file_utils import read_json_file

router = APIRouter(dependencies=[Depends(auth.get_api_key),])

JSON_PATHS = [
    './data/bg3/Gustav/Public/Gustav/RootTemplates/_merged.json',
    './data/bg3/Gustav/Public/GustavDev/RootTemplates/_merged.json',
    './data/bg3/Shared/Public/Shared/RootTemplates/_merged.json',
    './data/bg3/Shared/Public/SharedDev/RootTemplates/_merged.json',
]

JSONS = [read_json_file(p) for p in JSON_PATHS]

def extract_path(index: int, map_key: str):
    json_path = JSON_PATHS[index].split('bg3/')[-1]
    path = json_path.replace("_merged.json", "")
    return path + map_key + '.lsx'

def format_urls(request: Request, map_key: str):
    return [
        # get lsx
        # get txt (Generated)
    ]

@router.get('')
async def find_by_handle(request: Request, handle: str=None):

    if (handle == None):
        return {}
    
    results = {}
    for i, json in enumerate(JSONS):
        json: dict
        for map_key, attributes in json.items():
            map_key: str
            attributes: list
            if (len(attributes) == 0):
                continue

            for attr in attributes:
                if (attr['@handle'] != handle):
                    continue

                # results[map_key] = extract_path(i, map_key)
                results[map_key] = format_urls(request, map_key)
    
    return results
                