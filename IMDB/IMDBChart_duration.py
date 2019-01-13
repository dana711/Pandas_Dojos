import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('../data/imdb_1000.csv')

movies['duration'].hist(bins=80);

plt.title('Duration')
plt.savefig('./Plot_Output/duration_hist.png')
plt.show()
