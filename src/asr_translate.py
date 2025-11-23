from faster_whisper import WhisperModel
from .config import ASR_MODEL_NAME, USE_GPU, SOURCE_LANGUAGE

class ASRTranslator:
    def __init__(self):
        device = "cuda" if USE_GPU else "cpu"
        compute_type = "float16" if USE_GPU else "int8"
        self.model = WhisperModel(ASR_MODEL_NAME, device=device, compute_type=compute_type)
        self.language = SOURCE_LANGUAGE

    def transcribe_english_array(self, audio_array, sample_rate):
        segments, info = self.model.transcribe(
            audio_array,
            beam_size=1,
            task="translate",
            language=self.language,
            temperature=0.0,
            best_of=1,
        )
        print(f"Detected language: {info.language} (p={info.language_probability:.2f})")
        text = ""
        for segment in segments:
            text += segment.text.strip() + " "
        return text.strip()

    def transcribe_english_file(self, audio_path):
        segments, info = self.model.transcribe(
            audio_path,
            beam_size=1,
            task="translate",
            language=self.language,
            temperature=0.0,
            best_of=1,
        )
        print(f"Detected language: {info.language} (p={info.language_probability:.2f})")
        text = ""
        for segment in segments:
            text += segment.text.strip() + " "
        return text.strip()
