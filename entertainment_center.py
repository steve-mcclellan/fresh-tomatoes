import fresh_tomatoes
from media import Movie

rtt = Movie("Remember the Titans",
            "https://upload.wikimedia.org/wikipedia/en/d/d1/Remember_the_titansposter.jpg",
            "https://www.youtube.com/watch?v=nPhu9XsRl4M")

fresh_tomatoes.open_movies_page([rtt])
