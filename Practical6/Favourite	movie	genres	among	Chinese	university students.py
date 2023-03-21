import matplotlib.pyplot as plt
labels = 'Comedy', 'Action', 'Romance', 'Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
#the dictionary I make
movies = {'Comedy':73,'Action':42,'Romance':38, 'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
