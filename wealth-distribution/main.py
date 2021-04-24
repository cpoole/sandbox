import csv
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import queue

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title('income distribution since 1970')

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
 
#x axis is grouping
#y axis is value
with open('data.csv') as csvfile:
  reader = csv.DictReader(csvfile, delimiter = ' ')
  for row in reader:
    vals = list(map(lambda x: int(x), list(row.values())))
    keys = list(map(lambda x: float(x), list(row.keys())[1:]))
    y = vals[1:]
    x = keys
    line, = ax.plot(x, y, label=vals[0], color = colors.pop())


ax.legend()
plt.savefig("mygraph.png")
