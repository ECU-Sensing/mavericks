import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rtlsdr import RtlSdr

def get_signal_strength(sdr, freq):
    sdr.center_freq = freq
    # Increase the number of samples for better accuracy
    samples = sdr.read_samples(512*1024)  # Was 256*1024
    power = np.mean(np.abs(samples)**2)
    return 10 * np.log10(power)  # Convert to dB

def update_histogram(frame):
    global freqs, powers
    powers = [get_signal_strength(sdr, f) for f in freqs]
    plt.cla()
    freqs_mhz = freqs / 1e6  # Convert frequencies to MHz for plotting
    plt.bar(freqs_mhz, powers, width=step_size / 1e6)  # Also convert the width to MHz
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Signal strength (dB)')
    plt.title('Live Signal Strength Histogram')
    plt.ylim(-75, -55)  # Adjust the range to show weaker signals
    plt.xlim(freqs_mhz[0], freqs_mhz[-1])  

# SDR setup
sdr = RtlSdr()
sdr.sample_rate = 2.048e6  # You might want to experiment with this as well
sdr.freq_correction = 60
# Set a manual gain value that works best for your setup
sdr.gain = 10  # Replace with the gain value that you find optimal

# Narrowed frequency range around 467.7125 MHz with finer steps
start_freq = 467.712e6
end_freq = 467.713e6
step_size = 0.0001e6  # 100 Hz step for finer resolution
freqs = np.arange(start_freq, end_freq, step_size)

# Initialize plot
plt.ion()
fig, ax = plt.subplots()
powers = [0] * len(freqs)

# Create animation
global ani
ani = FuncAnimation(fig, update_histogram, frames=range(100), cache_frame_data=False, interval=1000)
input("Press Enter to exit...")

plt.show()
