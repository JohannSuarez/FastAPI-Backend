'''
App exceptions are implemented in the utils package. First, AppExceptionCase
is subclassed from base Exception and includes various attributes for defining custom
app Exception scenarios. The exception handler with the task of handling custom app exceptions
(added to main) is defined with a response containing information about about the app
exception.
'''
from typing import Any
from fastapi import Request
from starlette.responses import JSONResponse

class AppExceptionCase(Exception):
    def __init__(self, status_code: int, context: Any):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.context = context

    def __str__(self):
        return (f"<AppException {self.exception_case} - "
              + f"status_code={self.status_code} - context={self.context}>")


async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception_handler": exc.exception_case,
            "context": exc.context
        }
    )

'''
Second, defining and documenting custom exception scenarios happens in the
same module and requires subclassing form AppExceptionCase. Each app exception
includes a description with the docstring and defines the status code to be
returned to the client.

The class names are reporetd back to inform clients of the particular exception scenario -
see AppExceptionCase initialization, and JSONResponse within the app exception handler.
'''

class AppException:
    class FooCreateItem(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Item creation failed
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)


    class FooGetItem(AppExceptionCase):
        def __init__(self, context: dict=None):
            """
            Item not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class FooItemRequiresAuth(AppExceptionCase):
        def __init__(self, context: dict=None):
            '''
            Item is not public and requires auth
            '''
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)

    class BlogCreateItem(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Item creation failed
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)

    class BlogGetPost(AppExceptionCase):
        def __init__(self, context: dict=None):
            """
            Item not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class BlogItemRequiresAuth(AppExceptionCase):
        def __init__(self, context: dict=None):
            '''
            Item is not public and requires auth
            '''
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)

    class ImageVerification(AppExceptionCase):
        def __init__(self, context: dict = None):
            '''
            File isn't a proper image format.
            '''
            status_code = 406
            AppExceptionCase.__init__(self, status_code, context)

    class ImageSaving(AppExceptionCase):
        def __init__(self, context: dict = None):
            '''
            Something went wrong during image saving.
            '''
            status_code = 418
            AppExceptionCase.__init__(self, status_code, context)
