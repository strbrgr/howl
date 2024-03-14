import pyaudio


def list_audio_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(
            f"Device {i}: {info['name']}, InputChannels: {info['maxInputChannels']}, OutputChannels: {info['maxOutputChannels']}"
        )


if __name__ == "__main__":
    list_audio_devices()
