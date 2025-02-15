from urllib.request import Request

from fastapi import FastAPI
from config import settings
from api.handlers import router
from infrastructure.middleware import cache_response_middleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="Trading results",
        docs_url="/api/docs",
        debug=settings.DEBUG,
    )
    @app.middleware("http")
    async def cache_response(request: Request, call_next):
        response = await cache_response_middleware(request, call_next)
        return response

    app.include_router(router)
    return app


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:create_app", host="0.0.0.0", port=8000, reload=True)