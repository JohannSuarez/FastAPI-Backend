from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import shutil


app = FastAPI()

'''
src and reading material:
    https://fastapi.tiangolo.com/tutorial/request-files/
    https://levelup.gitconnected.com/how-to-save-uploaded-files-in-fastapi-90786851f1d3
'''
@app.get('/')
async def root():
    return {"root": "Hey I do have a root"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/image")
async def image(image: UploadFile = File(...)):

    filename: PosixPath = Path(image.filename)
    directory: str = "received"
    with open(f"{directory}/{filename.with_suffix('.png')}", "wb") as buffer: # What is "wb"? Write, and binary mode (for images)
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}
