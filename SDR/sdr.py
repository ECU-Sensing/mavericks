import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Configure the RTL-SDR parameters
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 94.9e6
sdr.gain = 'auto'

# Capture a single spectrum sample
samples = sdr.read_samples(256*1024)

# Convert the samples to a complex numpy array
spectrum = np.fft.fft(samples)

# Plot the spectrum
plt.plot(np.abs(spectrum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Close the RTL-SDR device
sdr.close()
