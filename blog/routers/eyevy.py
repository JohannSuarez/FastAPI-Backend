from fastapi import FastAPI, File, UploadFile, APIRouter
from ..services.eyevy import EyevyService
from ..utils.service_result import handle_result
from pathlib import Path

import shutil, os

router = APIRouter(
    prefix="/eyevy",
    tags=["eyevy"],
    responses = {404: {"description": "Not Found"}},
)


@router.post('/eyevy/')
def receive_image(image: UploadFile = File(...)):
    result = EyevyService().image_handler(image)
    return handle_result(result)
