# Note that the end of the resampled data rises to meet the first
# sample of the next cycle for the FFT method, and gets closer to zero
# for the polyphase method:

from scipy import signal

x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f_fft = signal.resample(y, 100)
f_poly = signal.resample_poly(y, 100, 20)
xnew = np.linspace(0, 10, 100, endpoint=False)

import matplotlib.pyplot as plt
plt.plot(xnew, f_fft, 'b.-', xnew, f_poly, 'r.-')
plt.plot(x, y, 'ko-')
plt.plot(10, y[0], 'bo', 10, 0., 'ro')  # boundaries
plt.legend(['resample', 'resamp_poly', 'data'], loc='best')
plt.show()
