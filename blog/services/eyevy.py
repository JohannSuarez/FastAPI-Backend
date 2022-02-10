"""
What should we put into this class?
What should we receive from this class?

EyevyService encapsulates all business logic of the service.
The return value are of type ServiceResult: Containing a value attribute
with returnable data or, in case of an exception, an AppException.

In both cases, the respective result is returned back "upwards" to the controller layer.


handle_result() that is invoked in Router expects either a ServiceResult. If ServiceResult.success
we return the entire ServiceResult

If the ServiceResult.success if false, ServiceResult literally just returns an exception.
otherise, it returns a non-specified data type (but most likely a JSON) that can be accessed
with the with statement.

"""

class EyevyService():
    """
    What is the service?
    We either return a ServiceResult fed with valid return data,
    or ServiceResult fed with Exception.
    """

    @staticmethod
    def verfication():

        pass


    def write(image):

        filename: Path = Path(image.filename)
        directory: str = "received"

        try:
            with open(f"{directory}/{filename.with_suffix('.png')}", "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
        except Exception as e:
            return e

        return ServiceResult(write_res)
