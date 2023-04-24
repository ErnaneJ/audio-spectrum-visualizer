import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.signal import welch
from scipy import fftpack

# Load audio file
samplerate, data = wavfile.read('./assets/581010__xcreenplay__smoking-in-the-angel-section2.wav')

# Loads the file in two channels (stereo audio)
print(f"number of channels = {data.shape[1]}")

# Total time = number of samples / fs
length = data.shape[0] / samplerate
print(f"duration = {length}s")

# Plot the figures over time

# Interpolate to determine time axis
time = np.linspace(0., length, data.shape[0])

# Plots the left and right channels
plt.figure(1)
plt.plot(time, data[:, 0], label="Left channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

plt.figure(2)
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# Estimates the signal spectrum using the welch function
x  = data[:, 0] # => left channel
fs = 2*np.pi
# fs = samplerate
f, Pxx_spec = welch(x, fs, 'flattop', 512, scaling='spectrum')

# Plots the signal spectrum for normalized frequencies between 0 1 pi (positive frequencies)

plt.figure(3)
plt.semilogy(f, Pxx_spec)
plt.xlabel('Frequency [rad]')
plt.ylabel('Spectrum')
plt.show()

# Frequency of the generated cosine function
f_c = 10000 #10KHz
T = 1/f_c

# Number of input file samples
ns = data.shape[0]

# Initializing arrays to collect 1s of data
cosseno  = [0]*ns
t_axis = np.arange(0., ns)*T

# Cosine function that will be used in the modulation
for i in range(ns):
    cosseno[i] = np.cos(2 * np.pi * f_c * i * T) 

#Estimates the signal spectrum using the welch function
x  = data[:, 0]*cosseno # => left channel
fs = 2*np.pi
f, Pxx_spec = welch(x, fs, 'flattop', 512, scaling='spectrum')

plt.figure(4)
plt.plot(f, Pxx_spec)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Spectrum')
plt.show()

# Plot spectrum using FFT function
nfft=4096
freq = np.linspace(0., samplerate, nfft) # Interpolate to determine frequency axis
sig_fft = fftpack.fft(x,nfft)
plt.figure(4)
plt.plot(freq, np.abs(sig_fft))
plt.xlabel('frequencia [Hz]')
plt.ylabel('Esoectro de amplitudes')
# plt.plot(freq, np.abs(fftpack.fftshift(sig_fft)))
plt.show()