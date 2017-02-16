#!/usr/bin/env python
"""Define a list of movies and display them on a webpage."""

import fresh_tomatoes
from media import Movie


def main():
    # Create a list of the Best Picture Oscar winners of the 21st century.
    best_picture_winners = [
        Movie("A Beautiful Mind", 2001,
              "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=aS_d0Ayjw4o"),

        Movie("Chicago", 2002,
              "https://upload.wikimedia.org/wikipedia/en/e/e0/Chicagopostercast.jpg",  # NOQA
              "https://www.youtube.com/watch?v=8IxcfbldgBY"),

        Movie("The Lord of the Rings: The Return of the King", 2003,
              "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",  # NOQA
              "https://www.youtube.com/watch?v=r5X-hFf6Bwo"),

        Movie("Million Dollar Baby", 2004,
              "https://upload.wikimedia.org/wikipedia/en/d/d3/Million_Dollar_Baby_poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=OCDZLsqwH28"),

        Movie("Crash", 2005,
              "https://upload.wikimedia.org/wikipedia/en/d/d0/Crash_ver2.jpg",
              "https://www.youtube.com/watch?v=durNwe9pL0E"),

        Movie("The Departed", 2006,
              "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
              "https://www.youtube.com/watch?v=iojhqm0JTW4"),

        Movie("No Country for Old Men", 2007,
              "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=38A__WT3-o0"),

        Movie("Slumdog Millionaire", 2008,
              "https://upload.wikimedia.org/wikipedia/en/9/92/Slumdog_Millionaire_poster.png",  # NOQA
              "https://www.youtube.com/watch?v=AIzbwV7on6Q"),

        Movie("The Hurt Locker", 2009,
              "https://upload.wikimedia.org/wikipedia/en/6/6c/HLposterUSA2.jpg",  # NOQA
              "https://www.youtube.com/watch?v=lNIeToMeWxc"),

        Movie("The King's Speech", 2010,
              "https://upload.wikimedia.org/wikipedia/en/a/a0/Kings_speech_ver3.jpg",  # NOQA
              "https://www.youtube.com/watch?v=kYoSQkfrjfA"),

        Movie("The Artist", 2011,
              "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Artist_Poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=O8K9AZcSQJE"),

        Movie("Argo", 2012,
              "https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=w918Eh3fij0"),

        Movie("12 Years a Slave", 2013,
              "https://upload.wikimedia.org/wikipedia/en/5/5c/12_Years_a_Slave_film_poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=z02Ie8wKKRg"),

        Movie("Birdman or (The Unexpected Virtue of Ignorance)", 2014,
              "https://upload.wikimedia.org/wikipedia/en/6/63/Birdman_poster.png",  # NOQA
              "https://www.youtube.com/watch?v=uJfLoE6hanc"),

        Movie("Spotlight", 2015,
              "https://upload.wikimedia.org/wikipedia/en/f/f3/Spotlight_%28film%29_poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=Zg5zSVxx9JM")]

    # Using the (modified) starter code in fresh_tomatoes.py and the above
    # list, generate and open an HTML page that displays the movies in a
    # user-friendly form.
    fresh_tomatoes.open_movies_page(best_picture_winners)


if __name__ == '__main__':
    main()
