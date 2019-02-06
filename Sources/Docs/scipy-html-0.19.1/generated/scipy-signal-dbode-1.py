from scipy import signal
import matplotlib.pyplot as plt

# Transfer function: H(z) = 1 / (z^2 + 2z + 3)

sys = signal.TransferFunction([1], [1, 2, 3], dt=0.05)

# Equivalent: sys.bode()

w, mag, phase = signal.dbode(sys)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()
