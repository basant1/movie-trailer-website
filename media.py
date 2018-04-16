import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        title: A string that stores the title of the movie
        storyline: A string that stores a short description of the movie
        poster_image_url: A string that stores the url of the movie poster
        trailer_youtube_url: A string that stores the url of the movie's
        YouTube trailer

    """

    def __init__(
                self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
                    self.title = movie_title
                    self.storyline = movie_storyline
                    self.poster_image_url = poster_image
                    self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
