# pdf_routes.py

from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.pdf_converter import pdf_to_text
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    text = pdf_to_text(file_path)
    return {"filename": file.filename, "text": text}
