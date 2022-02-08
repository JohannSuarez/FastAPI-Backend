from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/image",
    tags=["images"]
    responses{404: {"description": "Not Found"}}
)

@router.post('/image/', response_model=BlogPostItem)
async def receive_image(image: UploadFile=(...)):

    filename: PosixPath = Path(image.filename)
    directory: str = "received"

    with open(f"{directory}/{filename.with_suffix('.png')}")

