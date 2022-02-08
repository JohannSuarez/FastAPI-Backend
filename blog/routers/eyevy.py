from fastapi import FastAPI, File, UploadFile, APIRouter
from pathlib import Path

import shutil

router = APIRouter(
    prefix="/image",
    tags=["images"],
    responses = {404: {"description": "Not Found"}},
)

@router.post('/image/')
async def receive_image(image: UploadFile=(...)):

    filename: Path = Path(image.filename)
    directory: str = "received"

    with open(f"{directory}/{filename.with_suffix('.png')}", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename }
