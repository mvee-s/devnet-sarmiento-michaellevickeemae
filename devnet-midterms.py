#add, display, count, and search movies



"""
Midterm Practical Exam — Movie Collection Manager
Student: Michaelle Vickeemae G. Sarmiento
"""

movies = []

movie_title = input("Enter movie title: ")
director_name = input("Enter director: ")
status = input("Enter status (watched/unwatched): ")

# def display_menu():
#     # print the menu
#     # return the user's choice
#     pass


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


# def main():
#     # create the main menu loop
#     # call the appropriate function based on the user's choice
#     pass


main()
