from fastapi import FastAPI, Request
from pages.router import router as router_page
from fastapi.templating import Jinja2Templates
from data import get_data as gd

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.include_router(router_page)


def conection():
    url = "http://erinrv.qscalp.ru/"
    test = gd.get_data_class(url)
    a = test.connect_method()
    print(a)


@app.get("/")
async def root(request: Request):
    test = conection()
    return templates.TemplateResponse("index.html", {"request": request, "test": test})

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
