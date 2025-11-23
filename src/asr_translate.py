from faster_whisper import WhisperModel
from .config import ASR_MODEL_NAME, USE_GPU

class ASRTranslator:
    def __init__(self):
        device = "cuda" if USE_GPU else "cpu"
        compute_type = "float16" if USE_GPU else "int8"
        self.model = WhisperModel(ASR_MODEL_NAME, device=device, compute_type=compute_type)

    def transcribe_english(self, audio_array, sample_rate):
        segments, info = self.model.transcribe(
            audio_array,
            beam_size=1,
            task="translate",
            language=None
        )
        text = ""
        for segment in segments:
            text += segment.text.strip() + " "
        return text.strip()
