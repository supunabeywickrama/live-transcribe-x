import time
import numpy as np
from .audio_capture import AudioCapture
from .asr_translate import ASRTranslator
from .config import AUDIO_SAMPLE_RATE

def main():
    print("Loading model...")
    model_start = time.time()
    translator = ASRTranslator()
    model_end = time.time()
    print(f"Model loaded in {model_end - model_start:.2f} s")

    capture = AudioCapture()
    capture.start()
    print("Listening on microphone. Press Ctrl+C to stop.")

    try:
        while True:
            chunk = capture.read_chunk()
            audio = chunk.flatten().astype(np.float32)
            start = time.time()
            text = translator.transcribe_english_array(audio, AUDIO_SAMPLE_RATE)
            end = time.time()
            if text.strip():
                print(f"\n[{end - start:.2f} s] {text}")
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        capture.stop()

if __name__ == "__main__":
    main()
