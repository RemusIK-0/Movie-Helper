from menu import *
from filter import load_movies
from statistics import vote_average_statistics

# load the movies dataset using the function from the filter module
df = load_movies()
# This is the main entry point of the application, which initializes the dataset and starts the main menu loop for user interaction.
def main_menu():
    while True:
        print('==========Meniu Principal==========')
        print('1. Filtrare Filme')
        print('2. Cautare Filme')
        print('3. Top 10 Filme dupa:')
        print('4. Statistici')
        print('5. Grafice')
        print('6. Iesire')

        choice = input('\nIntroduceti Optiunea Dorita: ')

        if choice == '1':
            movie_filter(df)

        elif choice == '2':
            search_engine(df)
            
        elif choice == '3':
            best_movies(df)

        elif choice == '4':
            vote_average_statistics(df)

        elif choice == '5':
            grafic_menu(df)
            
        elif choice == '6':
            print('La Revedere.')
            break

        else:
            print('Optiunea aleasa nu se afla in meniu, incercati din nou.')
            pass

if __name__ == '__main__':
    main_menu()





