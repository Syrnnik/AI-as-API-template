from fastapi import APIRouter, UploadFile

from services.whisper import tts_with_direct_model, tts_with_pipeline

generate_router = APIRouter(tags=["AI"])


@generate_router.post("/with-pipeline")
def generate(uploaded_audio: UploadFile):
    return tts_with_pipeline.get_text_from_audio_file(uploaded_audio)


# @generate_router.post("/directly")
# def generate(uploaded_audio: UploadFile):
#     return tts_with_direct_model.get_text_from_audio_file(uploaded_audio)
