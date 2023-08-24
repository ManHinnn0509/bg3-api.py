import uvicorn

from fastapi import FastAPI, Depends

from routes import ROUTER_PAIRS
from const import HOST_ADDRESS, HOST_PORT

import auth

app = FastAPI(
    # Comment out this line to enable doc pages
    docs_url=None, redoc_url=None
)

for endpoint, data in ROUTER_PAIRS.items():
    app.include_router(data['router'], prefix=endpoint)

@app.get('/')
async def index(api_key=Depends(auth.get_api_key)):
    d = {}
    for endpoint, data in ROUTER_PAIRS.items():
        d[endpoint] = {
            'description': data['description'],
            'url': f'{HOST_ADDRESS}:{HOST_PORT}{endpoint}'
        }
    
    return d

# --------------------------------------------------

if (__name__ == "__main__"):
    uvicorn.run(
        "app:app",
        host=HOST_ADDRESS, port=HOST_PORT,
        reload=True
    )