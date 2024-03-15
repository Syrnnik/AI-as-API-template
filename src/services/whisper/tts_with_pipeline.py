from fastapi import UploadFile
from transformers import pipeline

from constants.whisper import model_name, task_name

pipe = pipeline(
    task=task_name,
    model=model_name
)


def get_text_from_audio_file(uploaded_audio: UploadFile):
    file_content = uploaded_audio.file.read()

    prediction = pipe(
        inputs=file_content,
        # Uncomment this arg if you need timestamps of text parts
        # return_timestamps=True
    )
    return prediction
