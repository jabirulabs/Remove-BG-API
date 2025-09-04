from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from bg_utils import enhance_image_bytes, remove_background_bytes, process_image_bytes

app = FastAPI()

@app.post("/enhance/")
async def enhance_image_api(file: UploadFile = File(...)):
    """
    Enhance image quality
    """
    try:
        img_bytes = await file.read()
        enhanced = enhance_image_bytes(img_bytes)
        return StreamingResponse(BytesIO(enhanced), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/remove-bg/")
async def remove_bg_api(file: UploadFile = File(...)):
    """
    Remove background from image
    """
    try:
        img_bytes = await file.read()
        no_bg = remove_background_bytes(img_bytes)
        return StreamingResponse(BytesIO(no_bg), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/process/")
async def process_image_api(file: UploadFile = File(...)):
    """
    Full pipeline: Enhance + Remove BG
    """
    try:
        img_bytes = await file.read()
        final = process_image_bytes(img_bytes)
        return StreamingResponse(BytesIO(final), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
