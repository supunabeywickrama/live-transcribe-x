import queue
import sounddevice as sd
from .config import AUDIO_SAMPLE_RATE, AUDIO_CHUNK_DURATION

class AudioCapture:
    def __init__(self, device=None):
        self.device = device
        self.sample_rate = AUDIO_SAMPLE_RATE
        self.chunk_duration = AUDIO_CHUNK_DURATION
        self.chunk_size = int(self.sample_rate * self.chunk_duration)
        self.queue = queue.Queue()
        self.stream = None

    def _callback(self, indata, frames, time, status):
        if status:
            return
        self.queue.put(indata.copy())

    def start(self):
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            device=self.device,
            callback=self._callback
        )
        self.stream.start()

    def read_chunk(self):
        return self.queue.get()

    def stop(self):
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
            self.stream = None
