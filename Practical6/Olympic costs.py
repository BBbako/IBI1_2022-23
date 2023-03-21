import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()
#set two objects called "fig" and "ax"
fig, ax = plt.subplots()
OlympicGames = ('Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney	2000','Athens 2003','Beijing 2008','London 2012')
y_pos = np.arange(len(OlympicGames))
#make a list "costs"
costs=[1,8,15,7,5,14,43,40]
print(sorted(costs))
ax.barh(y_pos, costs, align='center')
ax.set_yticks(y_pos, labels=OlympicGames)
# labels read top-to-botto
ax.invert_yaxis()
ax.set_xlabel('costs')
ax.set_title('The cost of hosting the Summer Oltmpic Games')
plt.show()
