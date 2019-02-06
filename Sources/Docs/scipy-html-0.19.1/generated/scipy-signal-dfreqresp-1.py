# Generating the Nyquist plot of a transfer function

from scipy import signal
import matplotlib.pyplot as plt

# Transfer function: H(z) = 1 / (z^2 + 2z + 3)

sys = signal.TransferFunction([1], [1, 2, 3], dt=0.05)

w, H = signal.dfreqresp(sys)

plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")
plt.show()
