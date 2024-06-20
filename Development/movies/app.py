
from movie import add_movies, show_movies, find_movies

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


user_options = {
    "a" : add_movies,
    'l': show_movies,
    'f': find_movies
}

selection= input(MENU_PROMPT)
while selection != 'q':
    if selection in user_options:
         selected_option = user_options[selection]
         selected_option()
    else:
        print("Unknown command. Please try again.")
    selection= input(MENU_PROMPT)
    