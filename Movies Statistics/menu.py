from filter import load_movies
from statistics import plot_movies_per_genre, plot_rating_distribution, plot_budget_vs_revenue

# This module contains the main menu and user interaction logic for the movie dataset application.
def movie_filter(df):
    # This function provides a menu for filtering and sorting movies based on various criteria.
    while True:
        print('1. Ordonati filmele dupa gen')
        print('2. Ordonati filmele dupa an')
        print('3. Ordonati filmele dupa rating')
        print('4. Renuntare')

        search = input('\n=====Introduceti Optiunea Dorita=====\n')
        
        # Filter by genre
        if search == '1':
            print('1. Introduceti genul filmului')
            print('2. Renuntare')
            choice = input('\n=====Introduceti Optiunea Dorita=====\n')
            if choice == '1':
                subchoice = input('\n===Introduceti Genul Filmului===\n').strip().lower()
                    
                    # Function to check if the genre matches the user's input
                def has_genre(genres_list):
                    return any(g.get('name', '').strip().lower() == subchoice for g in genres_list)
                    
                result = df[df['genres'].apply(has_genre)]

                # Display the results
                for idx, row in result.iterrows():
                    genre_names = ', '.join(g.get('name', '') for g in row['genres'])
                        
                    print(f"{row['title']} - {genre_names}")


            elif choice == '2':
                print('Intoarcere in meniul anterior...')

            else:
                print('Va rugam sa alegeti o optiune valida')
        # Filter by year
        elif search == '2':
            print('1. Ordonare Ascendenta/Descendenta')
            print('2. Ordonare Doar Dupa An')
            print('3. Renuntare')
            year_choice =input('\n=====Introduceti Optiunea Dorita=====\n')
            # Sort by year
            if year_choice == '1':
                print('1. Ascendent')
                print('2. Descendent')
                print('3. Renuntare')
                sort1 = input('\n===Alegeti Optiunea Dorita===')
                # Sort the DataFrame based on the user's choice and display the results
                if sort1 == '1':
                    df_sorted = df.sort_values(by='year', ascending=True) 
                    for idx, row in df_sorted.iterrows():
                        print(f"{row['title']} - {row['year']}")
                elif sort1 == '2':
                    df_sorted = df.sort_values(by='year', ascending=False) 
                    for idx, row in df_sorted.iterrows():
                        print(f"{row['title']} - {row['year']}")
                elif sort1 == '3':
                    print ('Intoarcere in meniul anterior...')
            # Sort by year only
            elif year_choice == '2':
                chosed_year = int(input('\n=====Introduceti Anul Dorit=====\n'))
                sorted_year = df[df['year'] == chosed_year]
                # Display the results
                if not sorted_year.empty:
                    for idx, row in sorted_year.iterrows():
                        print(f"{row['title']} - {row['year']}")

                else:
                    print('Nu exista nici un film din acest an')
            
            elif year_choice == '3':
                print('Intoarcere la meniul anterior')

            else:
                print('Va rugam sa alegeti o optiune valida')
        # Filter by rating
        elif search == '3':
            print('1. Top 10 filme')
            print('2. Cele mai multe voturi')
            print('3. Renuntare')
            rating_choice = input('\n=====Alegeti Optiunea Dorita=====\n')

            rating = df.sort_values(by='vote_average', ascending=False).head(25)
            most_votes = df.sort_values(by='vote_count', ascending=False).head(25)
            # Display the results based on the user's choice
            if rating_choice == '1':
                for idx, row in rating.iterrows():
                    print(f'{row['title']} - {row['vote_average']}')
            elif rating_choice == '2':
                for idx, row in most_votes.iterrows():
                    print(f'{row['title']} - {row['vote_count']}')
            elif rating_choice == '3':
                print('Intoarcere la meniul anterior...')
            else:
                print('Va rugam sa alegeti o optiunea valida')
        
        if search == '4':
            print('Intoarcere la meniu anterior...')
            break
# Search engine for movies based on user input, allowing for partial matches and displaying relevant information about the found movies.
def search_engine(df):
    movie = input('\n=====Introduceti numele filmului=====\n').lower().strip()
    movie = " ".join(movie.split())
    found_movies = df[df['title'].str.lower().str.contains(movie)]

    if not found_movies.empty:
        for idx, row in found_movies.iterrows():
            print(f"{row['title']} | " 
                  f"{row['genres_name']} | "
                  f"{row['runtime']} min | "
                  f"{row['homepage']} | "
                  f"{row['status']} | "
                  f"{row['original_language']}")

    else:
        print('\n===Filmul nu a fost gasit. Incercati din nou===\n')
# This function provides a menu for displaying various statistics and visualizations related to the movies dataset, such as rating distribution, genre distribution, and budget vs revenue.
def best_movies(df):
    print('\n=====Alegeti actegoria dupa care doriti sa ordonati filmele=====\n')
    print('1. Rating')
    print('2. Numar de voturi')
    print('3. Popularitate')
    print('4. Producator')  
    print('5. Renuntare')

    best_movies_choice = input('\n===Alegeti Optiunea Dorita===\nOptiunea: ')
    
    if best_movies_choice == '1':
        top10_rating = df.sort_values(by='vote_average', ascending=False).head(10)
        for idx, row in top10_rating.iterrows():
            print(f"{row['title']} | {row['genres_name']} | {row['runtime']} min | {row['homepage']} | {row['original_language']}")
    if best_movies_choice == '2':
        top10_vote_count = df.sort_values(by='vote_count', ascending=False).head(10)
        for idx, row in top10_vote_count.iterrows():
            print(f"{row['title']} | {row['genres_name']} | {row['runtime']} min | {row['homepage']} | {row['original_language']}")
    if best_movies_choice == '3':
        top10_popularity = df.sort_values(by='popularity', ascending=False).head(10)
        for idx, row in top10_popularity.iterrows():
            print(f"{row['title']} | {row['genres_name']} | {row['runtime']} min | {row['homepage']} | {row['original_language']}")
    if best_movies_choice == '4':
        company_name = input('\n=Introduceti Numele Companiei=\n').strip().lower()
        company_name = ' '.join(company_name.split())

        found_company = df[df['production_company_name'].str.lower().str.contains(company_name)]
        if found_company.empty:
            print('Compania nu a fost gasita')

        movies_nr = len(found_company)
        company_name_display = found_company.iloc[0]['production_company_name']

        print((f"\n*****{company_name_display} - {movies_nr} filme*****\n"))
        for idx, row in found_company.iterrows():
            print(f"{row['title']} | " 
                  f"{row['genres_name']} | "
                  f"{row['runtime']} min | "
                  f"{row['homepage']} | "
                  f"{row['status']} | "
                  f"{row['original_language']}")
        print((f"\n*****{company_name_display} - {movies_nr} filme*****\n"))
# This function provides a menu for displaying various statistics and visualizations related to the movies dataset, such as rating distribution, genre distribution, and budget vs revenue.
def grafic_menu(df):
    print('\n=====Grafice=====\n')
    print('1. Rating Grafic')
    print('2. Numar Genuri Grafic')
    print('3. Budget vs Revenue')
    grafic_choice = input('Selectati Optiunea Dorita')

    if grafic_choice == '1':
        plot_rating_distribution(df)
    elif grafic_choice == '2':
        plot_movies_per_genre(df)
    elif grafic_choice == '3':
        plot_budget_vs_revenue(df)
    else:
        print('Introduceti o optiune valida')
    





