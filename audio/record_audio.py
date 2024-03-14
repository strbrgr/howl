import pyaudio
import wave
from datetime import datetime, timedelta


def record_audio():
    # Saving
    FPATH = "export/"
    FNAME = "scream"
    FEXTENSION = ".wav"
    now = datetime.now()
    previous_day = now - timedelta(days=1)
    recording_date = previous_day.strftime("%y%m%d")

    # Recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print("* Recording... Press Ctrl+C to stop.")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            now = datetime.now()
            if now.hour == 6 and now.minute == 0 and now.second == 0:
                break
    except KeyboardInterrupt:
        pass

    print("* Stopped recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(f"{FPATH}{FNAME}_{recording_date}{FEXTENSION}", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()


if __name__ == "__main__":
    record_audio()

