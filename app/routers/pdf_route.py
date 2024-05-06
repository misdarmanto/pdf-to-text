

from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.pdf_converter import extract_text_from_pdf
import io
from app.configs import app_configs

router = APIRouter()
templates = Jinja2Templates(directory="app/views")

@router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        pdf_file = io.BytesIO(content)
        text = extract_text_from_pdf(pdf_file)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
