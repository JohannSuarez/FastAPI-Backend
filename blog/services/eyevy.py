from pathlib import Path
from PIL import Image
from ..utils.app_exceptions import AppException

import shutil

"""
The return value are of type ServiceResult: Containing a value attribute
with returnable data or, in case of an exception, an AppException.
"""

from ..utils.app_exceptions import AppException
from ..utils.service_result import ServiceResult

class EyevyService():

    def image_handler(self, image) -> ServiceResult:
        '''
        Receives Image, first verifies.
        If verified, save image to server.
        '''
        validation_error: ServiceResult | None = self.is_invalid(image)

        if validation_error:
            return validation_error

        return self.write(image)


    def is_invalid(self, image) -> None | ServiceResult:
        '''
        If the image is invalid, it'll return a ServiceResult,
        otherwise we expect nothing.
        '''

        # Open image with PIL, use verify() to check if actually an image file.
        try:
            im = Image.open(image.file)
            im.verify()
        except Exception:
            context: dict = {"Format Error": f"{image.filename} file is not an image."}
            return ServiceResult(AppException.ImageVerification(context))


    def write(self, image) -> ServiceResult:
        """
        Save the image into the server, unless
        an error is raised along the way.
        """
        filename: Path = Path(image.filename)
        directory: str = "received"
        absolute_dir: Path = Path(__file__).parent.resolve()

        '''
        try:
            with open(f"{str(absolute_dir)}/{directory}/{filename.with_suffix('.png')}", "wb") as buffer:
                buffer.write(image.file.read()) 
                print(type(image.file))
                #shutil.copyfileobj(image.file, buffer)
        '''
        try:
            im = Image.open(image.file)
            im.save(f"{str(absolute_dir)}/{directory}/{filename.with_suffix('.png')}")
        except Exception:
            context: dict = {"Write Error": "Something went wrong during image save step."}
            return ServiceResult(AppException.ImageSaving(context))

        return ServiceResult({"Success":"Image Saved"})
