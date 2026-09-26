#add, display, count, and search movies



"""
Midterm Practical Exam — Movie Collection Manager
Student: Michaelle Vickeemae G. Sarmiento
"""

movies = []

movie_title = input("Enter movie title: ")
director_name = input("Enter director: ")
status = input("Enter status (watched/unwatched): ")

def display_menu():
    print("=== Movie Collection Manager")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    # print the menu
    # return the user's choice
    pass


def add_movie(movie_list):
    print(movie_title)
    print(director_name)
    print(status)

    print("Movie added successfully.")
    
    movies.append(f"{movie_title} - {director_name} - {status}")
    pass


def view_movies(movie_list):
    for movie in movies:
        # if
        print("=== All Movies ===")
        print(movies)
    
    # handle empty list
    #no movies in the collection
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


# def find_movie(movie_list):
#     # ask for a movie title
#     # search the list
#     # search should be case-insensitive
#     # print the result or "Movie not found."
#     pass


def main():
    while True:
        display_menu()
        user_input = int(input("Choose an option: "))

        if user_input == 1:
            add_movie()

        elif user_input == 2:
            view_movies()

        elif user_input == 3:
            count_watched_unwatched()

        elif user_input == 4:
            find_movie()

        elif user_input == 5:
            break
        else:
            print("Choose a valid option number.")
            continue

    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
