import fastapi
from src.server.router import routers
from src.server.advanced_import import *
import settings
import uvicorn

app = fastapi.FastAPI(
    title='Game Shop API', 
    version='PreAlpha 0.2', 
    description='This shop is best in the world'
    )

[app.include_router(router=rout) for rout in routers]

@app.get(path='/', include_in_schema=False)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


def start_server() -> None:
    uvicorn.run(app=settings.APP, host=settings.HOST, port=settings.PORT)


if settings.DEBUG:
    if __name__ == "__main__":
        start_server()