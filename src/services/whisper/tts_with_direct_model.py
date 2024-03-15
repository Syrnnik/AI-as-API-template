import soundfile
from fastapi import UploadFile
from transformers import WhisperModel, WhisperProcessor

from constants.whisper import model_name

processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperModel.from_pretrained(model_name)


def get_text_from_audio_file(uploaded_audio: UploadFile):
    audio_data, sampling_rate = soundfile.read(uploaded_audio.file)

    input_features = processor(
        audios=audio_data,
        sampling_rate=sampling_rate,
        return_tensors="pt"
    ).input_features

    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

    return transcription[0]
