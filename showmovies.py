#!/usr/bin/python

'''
showmovies.py
A simple application that displays a list of my favorite movies.
'''

import fresh_tomatoes
import json
import sys

class Movie(object):
    '''
    A simple class that stores information about a movie.
    '''
    def __init__(self, 
                 trailer_youtube_url="", 
                 poster_image_url="", 
                 title="",
                 release_date=""):
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.title = title
        self.release_date = release_date

def gen_movie_list(movie_src):
    '''
    Reads movie data from a JSON file.
    Parameters
    ----------
    movie_src: str
        The path to a JSON file containing movie data.

    Returns
    -------
    list
        A list of populated Movie objects.
    '''
    movies = []
    data = {}
    with open(movie_src) as fd:
        data = json.load(fd)

    for item in data["movies"]:
        movies.append(Movie(**item))
    return movies

if __name__ == "__main__":
    # open the site with the file provided on the command line
    if len(sys.argv) != 2:
        sys.exit("Usage: python showmovies.py <json_file>")
    json_file = sys.argv[1]
    movies = gen_movie_list("movies.json")
    fresh_tomatoes.open_movies_page(movies)