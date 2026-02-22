import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

now = dt.datetime.now()
h = now.hour % 12
m = now.minute
s = now.second

fig = plt.figure(figsize=(5, 5))
ax = plt.subplot(111, polar=True)

# Draw radial bars
ax.barh(3, 2*np.pi*(h/12), color="purple")
ax.barh(2, 2*np.pi*(m/60), color="orange")
ax.barh(1, 2*np.pi*(s/60), color="cyan")

ax.set_yticks([])
ax.set_xticks([])

ax.set_title(now.strftime("%H:%M:%S"), fontsize=16)

plt.tight_layout()
plt.show()
