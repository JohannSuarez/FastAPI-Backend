from fastapi import FastAPI
from routers import foo
from utils.app_exceptions import AppExceptionCase, app_exception_handler

app = FastAPI()

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
