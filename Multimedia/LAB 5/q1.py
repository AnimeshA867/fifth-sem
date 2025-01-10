# Given the wave file, write python program to get different parameters of the wave file such as number of channels, sampling width (bit depth), sampling rate, number of samples. Use wave library.

import wave

def get_wave_params(filename):
    with wave.open(filename, 'rb') as wave_file:
        params = wave_file.getparams()
        num_channels = params.nchannels
        sample_width = params.sampwidth * 8  # in bits
        frame_rate = params.framerate
        num_frames = params.nframes

    return {
        "Number of Channels": num_channels,
        "Sample Width (bits)": sample_width,
        "Frame Rate (Hz)": frame_rate,
        "Number of Samples": num_frames
    }

# Example usage
filename = 'music.wav'
params = get_wave_params(filename)
print(params)
