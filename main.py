from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='API Backend Shipay')
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get('/')
async def root():
    return {'message': "IT'S HOME!"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app', host='0.0.0.0', port=9000, log_level='info', reload=True
    )
