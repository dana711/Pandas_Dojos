import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('../data/imdb_1000.csv')

movies['duration'].plot(kind='box');

plt.title('Duration')
plt.savefig('./Plot_Output/duration_box.png')
plt.show()
