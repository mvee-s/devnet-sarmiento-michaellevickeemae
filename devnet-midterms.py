#add, display, count, and search movies



"""
Midterm Practical Exam — Movie Collection Manager
Student: Michaelle Vickeemae G. Sarmiento
"""

movies = []
movie_list = [
    " - ".join(movies[i : i +3]) for i in range(0, len(movies), 3)
]

def display_menu():
    print("\n=== Movie Collection Manager")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    # print the menu
    # return the user's choice
    pass


def add_movie(movie_list):
    movie_title = input("\nEnter movie title: ")
    director_name = input("Enter director: ")
    status = input("Enter status (watched/unwatched): ")

    movies.append(movie_title)
    movies.append(director_name)
    movies.append(status)

    print("Movie added successfully.")

    pass


def view_movies(movie_list):
    
    if not movies:
        print("\nNo movies in the collection.")
    else:
        print("\n=== All Movies ===")
        print(movies)
    pass

#count = 0
#def count_watched_unwatched(movie_list):
#    for movie in movies:
#       if 
    # loop through the list
    # count Watched vs Unwatched
#   count +=1
    # return both counts
#    pass


def find_movie(movie_list):
    search = input("Enter movie title: ").lower()
    match_found = 0

    for movie in movies:
        if search in movie.lower():
            print(movie)
            match_found += 1

        if match_found == 0:
            print("Movie not found.")
    # search should be case-insensitive
    
    pass


def main():
    while True:
        display_menu()
        user_input = int(input("Choose an option: "))

        if user_input == 1:
            add_movie(movie_list)

        elif user_input == 2:
            view_movies(movies)

        elif user_input == 3:
            count_watched_unwatched()

        elif user_input == 4:
            find_movie(movies)

        elif user_input == 5:
            break
        else:
            print("Choose a valid option number.")
            continue
    pass


main()
