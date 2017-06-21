import webbrowser

class Video():
    """Class to represent video format media"""
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
class Movie(Video):
    """Class to represent Movies - child of Video"""
    
    def __init__(self, title, duration, story_line, poster_image_url, trailer_youtube_url):
        print ("Movie constructor called with title: "+title)
        Video.__init__(self, title, duration)
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self. trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        