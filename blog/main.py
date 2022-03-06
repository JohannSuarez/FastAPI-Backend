from .utils.app_exceptions import AppExceptionCase, app_exception_handler
from .routers import foo, blog, eyevy, dht
from .config.database import create_tables
from fastapi import Depends, FastAPI

from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordBearer
from starlette.exceptions import HTTPException as StarletteHTTPException

from pydantic import BaseModel


from .utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler
)

create_tables()

app = FastAPI()

'''
When we create an instance of the OAuth2PasswordBearer class we pass
in the tokenUrl parameter. The parameter contains the URL that the client
(the frontend running in the user's browser) will use to send the username
and password in order to to get a token.

Tip:

Here tokenUrl="token" refers to a relative URL token that we haven't created yet.
As it's a relative URL, it's equivalent to ./token.

Because we are using a relative URL, if your API was located at https://example.com,
then it would refer to https://example.com/token. But if your API was located at
https://example.com/api/v1/ , then it would refer to https://example.com/api/v1/token.
'''
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
app.include_router(dht.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

'''
Now you can pass that oauth2_scheme in a dependency with Depends.
This dependency will provide a str that is assigned to the parameter token of the path
operation funciton.

FastAPI will know that it can use this dependency to define a "security scheme" in the
OpenAPI schema (and the automatic API docs).
'''

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: str | None = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    user = fake_decode_token(token)
    return user

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
