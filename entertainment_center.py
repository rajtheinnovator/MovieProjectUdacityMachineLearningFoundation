# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

def myFunctionForTakingUsersFavoriteMovieInput():
    movie_name = raw_input("Give the movies name")
    movie_story = raw_input("Give the movies storyline")
    movie_poster = raw_input("Give the movies thumbnail url")
    movie_trailer = raw_input("Give the movies trailer url")
    movie = media.Movie(movie_name, movie_story, movie_poster, movie_trailer)
    movies.append(movie)
    fresh_tomatoes.open_movies_page(movies)
    
acoustic = media.Movie("Acoustic",
                        "This is a playlist of beautiful songs collection",
                        "https://i.ytimg.com/vi/Utud1Rkc4Qw/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLA78VW6ZG1jNgIMEGszOoSkrfv0-g",
                        "https://www.youtube.com/watch?v=POLMg3GXfhk")
single_rehne_de = media.Movie("Single Rehne De",
                              "Song from the movie Simran",
                              "https://i.ytimg.com/an_webp/Ggtuoy6txTY/mqdefault_6s.webp?du=3000&sqp=CPCD0M0F&rs=AOn4CLDTfenAU7OrMvFh5uH-LByS5kzTDg",
                              "https://www.youtube.com/watch?v=Ggtuoy6txTY")

mile_ho = media.Movie("Mile ho tum humko",
                           "An aswesome song it is",
                           "https://i.ytimg.com/an_webp/N2-HsIYd0Go/mqdefault_6s.webp?du=3000&sqp=COKC0c0F&rs=AOn4CLAJx93TSlCwQ9OkNu6R6rLySYFV_Q",
                           "https://www.youtube.com/watch?v=N2-HsIYd0Go")
roar = media.Movie("Roar",
                   "Katy Perry - Roar (Official)",
                   "https://i.ytimg.com/an_webp/CevxZvSJLk8/mqdefault_6s.webp?du=3000&sqp=CKqY0M0F&rs=AOn4CLAl3iCf5kqFvxVRLPEzKlU-TUSmYg",
                   "https://www.youtube.com/watch?v=K-w2sYAqMKw")
kattey = media.Movie("'Kattey'",
                   "Ram Sampath, Bhanvari Devi, Hard Kaur",
                   "https://i.ytimg.com/an_webp/npKCgowu-Bk/mqdefault_6s.webp?du=3000&sqp=COKX0c0F&rs=AOn4CLDAmOkJcOfcYqs85yy6hyRj3ZcNAQ",
                   "https://www.youtube.com/watch?v=HWrVOxAdvdo")
right_now = media.Movie("Right Now",
                   "Akon - Right Now (Na Na Na)",
                   "https://i.ytimg.com/an_webp/vIaH35-MLsk/mqdefault_6s.webp?du=3000&sqp=CNWR0M0F&rs=AOn4CLBS11wU5tPLuvxrCDYqVDFLUHolvQ",
                   "https://www.youtube.com/watch?v=UCGV2G812VQ")
    
movies = [acoustic, single_rehne_de, mile_ho, roar, kattey, right_now]
# Code below taken from the link:
# http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
add_custom_movie = raw_input("Do you want to add movie of your interest Y/N ")
if(add_custom_movie == 'y' or add_custom_movie == 'Y' ):
    myFunctionForTakingUsersFavoriteMovieInput()
else:
    fresh_tomatoes.open_movies_page(movies)




