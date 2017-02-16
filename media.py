"""Container for classes of media items."""


class Movie(object):
    """Stores some basic data about a film.

    Attributes:
        title (str): The movie's title.
        year (int): The year of release.
        poster_image_url (str): A URL for an image of the movie's poster.
        trailer_youtube_url (str): Location of the trailer on Youtube.
    """

    def __init__(self, title, year, poster_image_url, trailer_youtube_url):
        self.title = title
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
