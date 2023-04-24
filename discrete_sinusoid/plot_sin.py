import matplotlib.pyplot as plt # For plotting
from math import sin, pi # => For generating input signals
import numpy as np

# Frequency of the generated sine function
f_c = 1000 # => 1KHz

# Sampling period
fs = 48000 # => Sampling frequency = 48KHz
T = 1/fs

# Number of samples in 1s
ns = fs*1

# Initializing arrays to collect 1s of data
input_data  = [0]*ns
t_axis = np.arange(0., ns)*T

# Sine function sampled up to 1s
for i in range(ns):
    input_data[i] = sin(2 * pi * f_c * i * T) 
    
# Select sine samples: #1/100 of 1s
n_plot=200
t_plot = t_axis[0:n_plot] 
input_section = input_data[0:n_plot] 

# Plot of the continuous sine function (plot function "simulates" a continuous function)
plt.figure(1)                
plt.ylabel('sin($2\pi f_c t$)')
plt.xlabel('t [s]') 
plt.title('Continuous sine wave')      
plt.plot(t_plot,input_section)
plt.show()

# Select sine samples
n_plot=50
t_plot = t_axis[0:n_plot] 
input_section = input_data[0:n_plot] 

# Plot of the sine function sampled with fs = 48KHz
plt.figure(2)                
plt.ylabel('sin($2\pi f_c n T$)')
plt.xlabel('n') 
plt.title('Discrete sine wave')      
plt.stem(input_section)
plt.show()