import time
import queue
import numpy as np
import sounddevice as sd
from .config import AUDIO_SAMPLE_RATE, AUDIO_CHUNK_DURATION
from .asr_translate import ASRTranslator

MANUAL_DEVICE_INDEX = 1

PREFERRED_DEVICE_KEYWORDS = [
    "stereo mix",
    "loopback",
    "what u hear",
]

def auto_find_device():
    devices = sd.query_devices()
    for idx, dev in enumerate(devices):
        name = dev.get("name", "").lower()
        max_in = dev.get("max_input_channels", 0)
        if max_in > 0:
            for key in PREFERRED_DEVICE_KEYWORDS:
                if key in name:
                    return idx
    return None

def main():
    print("Loading model...")
    translator_start = time.time()
    translator = ASRTranslator()
    translator_end = time.time()
    print(f"Model loaded in {translator_end - translator_start:.2f} s")

    device_index = MANUAL_DEVICE_INDEX

    if device_index is None:
        device_index = auto_find_device()

    if device_index is None:
        print("\n❗ Could not automatically find a loopback or Stereo Mix device.\n")
        print("Run: python -m src.list_audio_devices")
        print("Then set MANUAL_DEVICE_INDEX in system_audio_console.py to the index of your 'Stereo Mix' or virtual cable device.\n")
        return

    dev_info = sd.query_devices(device_index)
    print(f"\nUsing system audio input device index: {device_index}")
    print(dev_info)

    q = queue.Queue()

    def callback(indata, frames, time_info, status):
        if status:
            return
        q.put(indata.copy())

    stream = sd.InputStream(
        device=device_index,
        channels=1,
        samplerate=AUDIO_SAMPLE_RATE,
        blocksize=int(AUDIO_SAMPLE_RATE * AUDIO_CHUNK_DURATION),
        callback=callback,
    )

    stream.start()
    print("\n🎧 Listening to system audio... Play a movie / YouTube / any sound. Press Ctrl+C to stop.")

    last_text = ""

    try:
        while True:
            chunk = q.get()
            audio = chunk.flatten().astype(np.float32)

            rms = np.sqrt(np.mean(audio**2))
            if rms < 0.005:
                continue

            start = time.time()
            text = translator.transcribe_english_array(audio, AUDIO_SAMPLE_RATE)
            end = time.time()

            text = text.strip()
            if not text:
                continue

            if text == last_text:
                continue

            last_text = text

            print(f"\n[{end - start:.2f} s]: {text}")
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        stream.stop()
        stream.close()


if __name__ == "__main__":
    main()
