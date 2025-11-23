import sys
import time
from .asr_translate import ASRTranslator

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.test_offline_transcribe <audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    print(f"Loading model...")
    start_model = time.time()
    translator = ASRTranslator()
    end_model = time.time()
    print(f"Model loaded in {end_model - start_model:.2f} s")

    print(f"Transcribing and translating: {audio_path}")
    start = time.time()
    text = translator.transcribe_english_file(audio_path)
    end = time.time()

    print("\n=== ENGLISH TRANSCRIPT ===\n")
    print(text)
    print("\n==========================\n")
    print(f"Processing time: {end - start:.2f} s")

if __name__ == "__main__":
    main()
