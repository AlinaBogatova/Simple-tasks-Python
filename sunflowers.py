
import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflowers.csv')
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

print(f'Среднее - {sunflowers_mean:.3}, стандартное отклонение - {sunflowers_std:.3}')

plt.hist(sunflowers, range=(11, 15), histtype='step', linewidth=2, label='observed', density=True)
plt.legend()
plt.show()

sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)
plt.hist(sunflowers_normal, range=(11, 15), histtype='step', linewidth=2, label='normal', density=True)
plt.legend()
plt.show()

experiments = np.random.binomial(200, 0.1, 5000)
print(experiments)
prob = np.mean(experiments < 20)
print(prob)