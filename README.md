# LiveTranscribeX

LiveTranscribeX is a Windows desktop tool that listens to any audio (movies, YouTube, meetings) in any language and shows low-latency English subtitles in a small always-on-top overlay.

## Project Goals

- Capture system audio and microphone audio on Windows
- Perform multilingual speech recognition in real-time
- Translate recognized speech to English
- Display live subtitles with minimal delay (target ~0.5–1.5 s)
- Package as a simple, usable desktop app

## High-Level Architecture

1. Audio Capture  
   - Capture system audio via virtual audio device (VB-Cable/Stereo Mix).  
   - Chunk audio into small windows (e.g. 300–700 ms).

2. Streaming ASR  
   - Multilingual speech-to-text using a streaming-capable model (e.g. faster-whisper, Vosk).  
   - Provide partial and final transcripts.

3. Translation  
   - Translate transcripts to English using a local model or external API.  
   - Work incrementally for low latency.

4. Subtitle Overlay  
   - Always-on-top overlay window.  
   - Shows 1–2 lines of current and previous subtitles.

## Tech Stack (planned)

- Python
- Audio: sounddevice or PyAudio, Windows virtual audio device
- ASR: faster-whisper / whisper.cpp / Vosk (to be evaluated)
- Translation: local transformer model or external API
- UI: PySide6 or PyQt5 for overlay
- Concurrency: threading/asyncio with queues

## Roadmap

### Phase 0 – Offline Prototype
- [ ] Set up environment and install ASR model
- [ ] Transcribe and translate a pre-recorded foreign-language audio file
- [ ] Log latency and output quality

### Phase 1 – Microphone Live Captions (Console)
- [ ] Capture microphone audio in small chunks
- [ ] Stream audio into ASR model and print English text
- [ ] Experiment with chunk sizes and model sizes

### Phase 2 – Basic Subtitle Window
- [ ] Create a small desktop window that shows text from a test script
- [ ] Connect ASR output to the window instead of console
- [ ] Show last 1–2 lines only

### Phase 3 – System Audio Integration
- [ ] Capture system audio via VB-Cable or Stereo Mix
- [ ] Run full pipeline: system audio → ASR → translation → overlay
- [ ] Evaluate latency while playing a movie

### Phase 4 – Optimization & Polish
- [ ] Add Voice Activity Detection (VAD) to skip silence
- [ ] Tune model size and decoding parameters for latency vs accuracy
- [ ] Add configuration panel (choose input device, model size)
- [ ] Package as an executable for Windows

## How I Will Track Work

I will:

- Use Git commits to document progress step by step
- Use GitHub Issues for features and bugs (ASR, translation, UI, optimization)
- Update this README as the architecture and implementation evolve

## Status

- Project initialized
- Architecture and roadmap defined
