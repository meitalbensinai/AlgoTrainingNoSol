from scipy import special
import matplotlib.pyplot as plt
x = np.linspace(-3, 3)
plt.plot(x, special.wofz(x))
plt.xlabel('$x$')
plt.ylabel('$wofz(x)$')
plt.show()
