from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

'''
src and reading material:
    https://fastapi.tiangolo.com/tutorial/request-files/
    https://levelup.gitconnected.com/how-to-save-uploaded-files-in-fastapi-90786851f1d3
'''

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/image")
async def image(image: UploadFile = File(...)):

    print(image)
    directory: str = "received"
    with open(f"{directory}/{image.filename}.png", "wb") as buffer: # What is "wb"? Write, and binary mode (for images)
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}
