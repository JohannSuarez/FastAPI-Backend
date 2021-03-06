'''
The ServiceResult class defines a generic outcome of a
service operation. In case the operation is successful, the
outcome (or 'value') is returned contained within the value
attribute of the instance. In case of the custom app exception,
the service result instance contains information about the raised
exception (e.g. which status code should be returned to the client).
'''
import inspect

from ..utils.app_exceptions import AppExceptionCase
from loguru import logger

class ServiceResult:
    def __init__(self, arg):
        if isinstance(arg, AppExceptionCase):
            self.success = False
            self.exception_case = arg.exception_case
            self.status_code = arg.status_code
        else:
            self.success = True
            self.exception_case = None
            self.status_code = None
        self.value = arg

    def __str__(self):
        if self.success:
            return "[Success]"
        return f'[Exception] "{self.exception_case}"'

    def __repr__(self):
        if self.success:
            return "<ServiceResult Success>"
        return f"<ServiceResult AppException> {self.exception_case}"

    def __enter__(self):
        return self.value

    def __exit__(self, *kwargs):
        pass

def caller_info() -> str:
    info = inspect.getframeinfo(inspect.stack()[2][0])
    return f"{info.filename}:{info.function}:{info.lineno}"

def handle_result(result: ServiceResult):
    if not result.success:
        with result as exception:
            logger.error(f"{exception} | caller={caller_info()}")
            raise exception

    with result as result:
        return result
