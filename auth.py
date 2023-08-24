# IDK this is from: https://itsjoshcampos.codes/fast-api-api-key-authorization

from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN

from const import API_SECRET

api_key_header = APIKeyHeader(name='access_token', auto_error=False)

async def get_api_key(api_key_header: str=Security(api_key_header)):

    # If you're debugging, you can just directly return `api_key_header` in here
    return api_key_header

    if (api_key_header == API_SECRET):
        return api_key_header
    
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
