import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
from scipy.stats import linregress

# X = np.linspace(-2*np.pi, 2*np.pi, 1024)
# C, S = np.cos(X) , np.sin(X)

# plt.plot(X, C)
# plt.plot(X, S)
# plt.show()

   
with open("fransarData.txt", "r") as data:
  xlist = []
  ylist = []
  lol = 0
  for line in data:
    ylist.append(int(line.strip()))
    # xlist.append(lol)
    # lol += 1




def AverageData():
  avList= []
  minimum_value = ylist.index(np.min(ylist))
  # print(ylist[:minimum_value+1])
  # print(ylist[minimum_value:])
  lower = ylist[:minimum_value+1]
  higher = ylist[minimum_value:]
  higher.reverse()
  for i in range(len(ylist[:minimum_value])):
    avdata =(lower[i]+ higher[i])/2
    avList.append(avdata)
  return avList

avList =AverageData()

def linRegression(x,y):
  print(linregress(x,y))




  

X = np.linspace(0,len(avList),len(avList))
linRegression(X,avList)
fig, ax = plt.subplots()
ax.plot(X,avList, "bo")

ax.set(xlabel='Antal fransar', ylabel='Tryck (Pa)',
       title='Antal fransar som passerar en punkt gentemot tryck')
plt.show()





  

