import numpy as np
import matplotlib.pyplot as plt
from filter import load_movies

# Load the movies dataset using the function from the filter module
df = load_movies()

# This module contains functions for calculating and displaying various statistics and visualizations related to the movies dataset, such as rating distribution, genre distribution, and budget vs revenue.
def vote_average_statistics(df):
    valid_df = df[df['vote_average'] > 0]

    max_idx = valid_df['vote_average'].idxmax()
    min_idx = valid_df['vote_average'].idxmin()

    max_vote = df.loc[max_idx, 'vote_average']
    min_vote = df.loc[min_idx, 'vote_average']

    max_title = df.loc[max_idx, 'title']
    min_title = df.loc[min_idx, 'title']

    mean_vote = np.mean(df['vote_average'])
    std_vote = np.std(df['vote_average'])

    print('\n==========Statistici Filme==========\n')
    print(f'Ce-l mai bine cotat film este : {max_title} cu cota de {max_vote}')
    print(f'Ce-l mai slab cotat film este : {min_title} cu cota de {min_vote}')
    print(f'Media filmelor este de {mean_vote:.2f}')
    print(f'Asta nu stiu ce e {std_vote:.2f}')

# Graphic for rating distribution
def plot_rating_distribution(df):
    ratings = df['vote_average'].dropna()
    
    plt.figure()
    plt.hist(ratings, bins=20)
    plt.title('Distributia ratingurilor filmelor')
    plt.xlabel('Rating')
    plt.ylabel('Nr. Filme')
    plt.show()

# Graphic for genre distribution
def plot_movies_per_genre(df):
    genres_series = df['genres_name'].str.split(', ')
    all_genres = genres_series.explode()
    genres_counts = all_genres.value_counts().head(10)

    plt.figure()
    plt.bar(genres_counts.index, genres_counts.values)
    plt.title('Top 10 genuri dupa nr de filme')
    plt.xlabel('Gen')
    plt.ylabel('Nr filme')
    plt.xticks(rotation=45)
    plt.show()

# Graphic for budget vs revenue
def plot_budget_vs_revenue(df):
    valid_df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

    plt.figure()
    plt.plot(valid_df['budget'], valid_df['revenue'])
    plt.title('Buget vs Venit')
    plt.xlabel('Buget')
    plt.ylabel('Venit')
    plt.show()
