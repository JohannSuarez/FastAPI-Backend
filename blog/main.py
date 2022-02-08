from .utils.app_exceptions import AppExceptionCase, app_exception_handler
from .routers import foo
from .routers import blog
from .routers import eyevy
from .config.database import create_tables
from fastapi import FastAPI

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


from .utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler
)

create_tables()

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)

@app.exception_handler(AppExceptionCase) # This decorator is from FastAPI
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


'''
Routers and their routes are
defined in modules within the routers package. Each
route instantiates the respective service and passes on the database
session from the request dependency. Handled by handle_result(), the
service result (either the requested data as the result of a successful
operation or an exception) is returned. In case of an exception, instead of
(and before) returning any response, the app exception handler in main picks
up handling the exception and returns a response.
'''

app.include_router(foo.router)
app.include_router(blog.router)
app.include_router(eyevy.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
