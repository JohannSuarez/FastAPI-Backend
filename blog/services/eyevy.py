from ..utils.app_exceptions import AppException
from ..utils.service_result import ServiceResult

class ReceiveImage():
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

 
