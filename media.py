# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information
    # Provide other arguments for the Movie object which will help in creating the movie website
    def __init__(self, title, story_line, movie_poster, movie_trailer):
        # initialize instance of class Movie
        self.title = title
        self.movie_storyline = story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
