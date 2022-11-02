import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy


with open("polarisation.txt", "r") as data:
  angles = []
  intensities = []

  for i in data:
    i= i.split(",")

    angles.append(int(i[0].strip()))
    intensities.append(float(i[1].strip()))

  
print(angles)
print(intensities)

I = 100
lol = []

for j in range(len(angles)):

  expectedIntensity = I*(np.cos(angles[j]))**2
  lol.append(expectedIntensity)





plt.plot(angles, intensities)
plt.plot(angles, lol)
plt.show()