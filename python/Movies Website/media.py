import webbrowser
class Movie():
    #this is documentation comments    
    """This class provides the structure of Movies and its attributes"""
    #self is the obj which we are going to create 
    def __init__(self,movieTitle,movieStoryLine,
                 moviePoster,trailerYoutube):
        self.title=movieTitle
        self.storyline=movieStoryLine
        self.poster_image_url=moviePoster
        self.trailer_youtube_url=trailerYoutube
    #its first arg is self because it is accessed through obj
    def showTrailer(self):
        webbrowser.open(self.trailerVideo)
        
