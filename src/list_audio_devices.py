import sounddevice as sd

def main():
    devices = sd.query_devices()
    print("\nAvailable audio devices:\n")
    for idx, dev in enumerate(devices):
        name = dev.get("name", "")
        max_in = dev.get("max_input_channels", 0)
        max_out = dev.get("max_output_channels", 0)
        print(f"[{idx}] {name} | in: {max_in} | out: {max_out}")
    default_in = sd.default.device[0]
    default_out = sd.default.device[1]
    print(f"\nDefault input device index: {default_in}")
    print(f"Default output device index: {default_out}\n")

if __name__ == "__main__":
    main()
