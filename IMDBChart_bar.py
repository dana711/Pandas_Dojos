import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('../data/imdb_1000.csv')

#standardize the content rating before creating plots:
movies['content_rating'] = movies['content_rating'].apply(lambda x: 'UNRATED'
                                                           if x in ('NOT RATED',
                                                           'APPROVED',
                                                           'PASSED',
                                                           'GP')
                                                           else x)

movies['content_rating'] = movies['content_rating'].apply(lambda x: 'NC-17'
                                                           if x in ('X','TV-MA')
                                                           else x)

movies['content_rating'] = movies['content_rating'].fillna('UNRATED')


ax1 = movies['content_rating'].value_counts().plot(kind='bar', figsize=(18,6));

ax1.set_title('Movie Content Rating Bar Chart', fontsize=30, y=1.01);
ax1.set_xlabel('Movie Content Rating', fontsize=15);
ax1.set_ylabel('Count of Movies per Rating', fontsize=15);
plt.savefig('./Plot_Output/rating_box.png')
plt.show()
