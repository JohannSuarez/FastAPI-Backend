from fastapi import FastAPI, File, UploadFile, APIRouter
from ..services.blog import eyevy
from ..utils.service_result import handle_result
from pathlib import Path

import shutil, os

router = APIRouter(
    prefix="/eyevy",
    tags=["eyevy"],
    responses = {404: {"description": "Not Found"}},
)

@router.post('/eyevy/')
async def receive_image(image: UploadFile):
#async def receive_image(image: UploadFile = File(...)):

    filename: Path = Path(image.filename)
    directory: str = "received"

    absolute_dir: Path = Path(__file__).parent.resolve()

    with open(f"{str(absolute_dir)}/{directory}/{filename.with_suffix('.png')}", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    print("RECEIVED IMAGE")
    print(f"Saving to: {directory}/{filename.with_suffix('.png')} ")

    return {"filename": image.filename }
