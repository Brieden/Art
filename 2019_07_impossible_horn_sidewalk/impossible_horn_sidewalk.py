import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = (40.0, 20.0)
plt.rcParams['figure.dpi'] = 400

rand_normal = np.random.rand

for _ in range(150):
    angle = rand_normal()*2*np.pi
    startpoint = np.cos(angle) / (4 + rand_normal()**2)
    endpoint = np.cos(angle) * (1.9 - .9*rand_normal())
    moon = np.tan(angle)
    blood = [rand_normal() * moon**2 / (i+1) * (i*2-2) for i in range(int(rand_normal() *moon**2))]
    light = np.linspace(startpoint, endpoint,100)
    analogy = np.polyval([*blood, rand_normal()*moon, moon, 0], light)
    plt.plot(light, analogy, '-w', lw = 0.6*rand_normal(), alpha = rand_normal())

plt.axis('off'), plt.xlim(-2,2), plt.ylim(-1,1), plt.show()
