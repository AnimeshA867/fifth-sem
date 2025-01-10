import numpy as np
import wave
from pynput import keyboard

# Constants
SAMPLE_RATE = 44100  # Hertz
DURATION = 0.5  # Seconds for each note
VOLUME = 0.5  # Volume level
OUTPUT_FILE = "piano_notes.wav"

# Frequency of piano notes (C4 to B4)
note_frequencies = {
    'a': 261.63,  # C4
    'w': 277.18,  # C#4
    's': 293.66,  # D4
    'e': 311.13,  # D#4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    't': 369.99,  # F#4
    'g': 392.00,  # G4
    'y': 415.30,  # G#4
    'h': 440.00,  # A4
    'u': 466.16,  # A#4
    'j': 493.88,  # B4
    'k': 523.25   # C5
}

recorded_notes = []

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    return wave

def save_notes_to_wav(notes, filename):
    audio = np.concatenate(notes) * 32767  # Convert to 16-bit PCM
    audio = audio.astype(np.int16)
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        f.writeframes(audio.tobytes())

def on_press(key):
    try:
        if key.char in note_frequencies:
            frequency = note_frequencies[key.char]
            wave = generate_sine_wave(frequency, DURATION, SAMPLE_RATE)
            recorded_notes.append(wave * VOLUME)
            print(f"Played note: {key.char}")
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save the recorded notes to a WAV file
if recorded_notes:
    save_notes_to_wav(recorded_notes, OUTPUT_FILE)
    print(f"Notes saved to {OUTPUT_FILE}")
else:
    print("No notes were recorded.")
