from fastapi import FastAPI, Request, UploadFile
from starlette.responses import FileResponse

from pages.router import router as router_page
from fastapi.templating import Jinja2Templates
from data import get_data as gd

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.include_router(router_page)


def conection(a, dir):
    url = "http://erinrv.qscalp.ru/"
    test = gd.get_data_class(url)
    a = test.connect_method()
    dir = test.get_dir()
    return a, dir


def list_dir():
    pass


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dir")
async def say_hello(request: Request):
    url = "http://erinrv.qscalp.ru/"
    test = gd.get_data_class(url)
    a = test.connect_method()
    dirs = test.get_dir()

    return templates.TemplateResponse("base.html", {"request": request, 'test': test, 'a': a, 'dirs': dirs, 'url': url})


@app.get("/dir/{date}")
async def list_files(request: Request, date: str):
    url = "http://erinrv.qscalp.ru/"
    test = gd.get_data_class(url)
    a = test.connect_method()
    dirs = test.get_dir()

    files = test.get_list_files(date)
    return templates.TemplateResponse("list.html",
                                      {"request": request, "date": date, 'files': files, 'url': url})
    # return {"message": f"Hello {date}"}


@app.get("/dir/{date}/{files}")
async def download_file(request: Request, date: str, files: str):
    # async def download_file(request: Request, date: str, files: str):
    return FileResponse(path="http://erinrv.qscalp.ru/{date}/{files}".format(date=date, files=files))

# http://erinrv.qscalp.ru/2024-04-16/VTBR.2024-04-16.Deals.qsh
# async def say_hello(request: Request, date: str, file: UploadFile):
#     url = "http://erinrv.qscalp.ru/"
#     test = gd.get_data_class(url)
#     a = test.connect_method()
#     dirs = test.get_dir()
#     r_dir = f'{url}/{date}/{file}'
#     file = test.download_file(r_dir)
#     return {'filename': file.filename, 'file': file, 'dirs': dirs, 'url': url}
