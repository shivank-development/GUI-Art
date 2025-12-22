import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6*np.pi, 200)
y = np.sin(x)

plt.plot(x, y)
plt.title("Wavy")
plt.show()