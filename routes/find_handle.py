from fastapi import APIRouter, Depends

import auth

router = APIRouter(dependencies=[Depends(auth.get_api_key),])

@router.get('')
async def find_handle(startswith: str=None, endswith: str=None, includes: str=None):
    return {'s': startswith, 'e': endswith, 'i': includes}