import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy


with open("BrewstervinkelData.txt", "r") as data:
  xlist = []
  ylist = []
  for line in data: 
    line = line.split(",")
    xlist.append(int(line[0].strip())) 
    ylist.append(float(line[1].strip()))




# comparison data
n1= float(1.0003)
n2 = float(1.43)
intensList= []
for i in range(len(xlist)):
  v1 = np.deg2rad(xlist[i])
  thetaT = np.arcsin((n1/n2)*np.sin(v1))

  
  intensity = ((np.tan(v1-thetaT))/(np.tan(v1+thetaT)))**2 
  intens2 = (((n1*np.cos(v1)-n1*np.cos(thetaT))/(n2*np.cos(v1)+n2*np.cos(thetaT)))**2)

  intensList.append(round(intens2,3))
  print(xlist[i],round(intens2,3), ylist[i])
plt.plot(xlist, ylist)
plt.plot(xlist, intensList)
plt.show()


