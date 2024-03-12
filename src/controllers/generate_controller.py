from fastapi import APIRouter

from src.models.generate_model import GenerateBody

generate_router = APIRouter(tags=["AI"])


@generate_router.post("/")
def generate(body: GenerateBody):
    pass
