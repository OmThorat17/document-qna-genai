from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 1. Validate PDF
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    # 2. Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # 3. Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "message": "PDF uploaded successfully",
        "path": file_path
    }
