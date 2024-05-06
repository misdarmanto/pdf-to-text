from fastapi import FastAPI
from app.routers import pdf_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


app = FastAPI()
app.include_router(pdf_route.router, prefix="/api")
