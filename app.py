import uvicorn

from fastapi import FastAPI, Depends

from routes import ROUTER_PAIRS
from const import HOST_ADDRESS, HOST_PORT

import auth

app = FastAPI(
    # Comment out this line to enable doc pages
    docs_url=None, redoc_url=None
)

for endpoint, router in ROUTER_PAIRS.items():
    app.include_router(router, prefix=endpoint)

@app.get('/')
async def index(api_key=Depends(auth.get_api_key)):
    return {
        'availableRoutes': [
            key for key in ROUTER_PAIRS.keys()
        ]
    }

# --------------------------------------------------

if (__name__ == "__main__"):
    uvicorn.run(
        "app:app",
        host=HOST_ADDRESS, port=HOST_PORT,
        reload=True
    )