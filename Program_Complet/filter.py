# This module is responsible for loading and preprocessing the movies dataset.
import pandas as pd
import ast

# Dataframe reader and preprocessor
def load_movies(file_path='movies_metadata.csv'):
    df = pd.read_csv(file_path)
    print('Date Incarcate cu Succes')

# Removing null values
    df = df.dropna(subset=[
    'title',
    'release_date',
    'vote_average'
])
    # Removing duplicates
    df = df.drop_duplicates(keep='first')
    
    # Converting data types
    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')
    df['vote_count'] = pd.to_numeric(df['vote_count'], errors= 'coerce')
    df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = df['release_date'].dt.year
    df['year'] = pd.to_numeric(df['year'])

    # Parsing JSON-like strings in 'genres' and 'production_companies'
    df['genres'] = df['genres'].apply(ast.literal_eval)
    df['production_companies'] = df['production_companies'].apply(ast.literal_eval)

    # Extracting names from 'production_companies'
    def production_companie_name_extractor(production_companies):
        if not isinstance(production_companies, list):
            return ""
        
        return ", ".join(company_name.get('name', '') for company_name in production_companies)
    
    df['production_company_name'] = df['production_companies'].apply(production_companie_name_extractor)
    
    # Extracting names from 'genres'
    def genre_name_extractor(genres):
        if not isinstance(genres, list):
            return ""

        return ", ".join(genre.get('name', '') for genre in genres)
    
    # Adding a new column with genre names
    df['genres_name'] = df['genres'].apply(genre_name_extractor)
    
    return df





