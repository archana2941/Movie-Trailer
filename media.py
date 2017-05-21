# Often, the first argument of a method is called self.
# This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the
# convention your code may be less readable to other Python programmers, and it is also conceivable that
# a class browser program might be written that relies upon such a convention.

# file that uses this Media class-->file1.py

import webbrowser

class Media :
    """ init function is invoked automatically """
    def __init__(self, movie_title, movie_storyline, video_link, poster_link) :
        self.title=movie_title
        self.storyline=movie_storyline
        self.trailer_youtube_url=video_link   
        self.poster_image_url=poster_link

  
        #show_trailor()--> To show movie trailor 
    def show_trailor(self) : 
        webbrowser.open(self.trailer_youtube_url)
        
        
