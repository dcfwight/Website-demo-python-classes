import media
import fresh_tomatoes as ft

# Set up 8 different movies - args are title, duration, story_line, poster_image, and trailer_url
glengarry = media.Movie('Glengarry GlenRoss', 100, 'the harsh lives of salesmen', \
                        'https://upload.wikimedia.org/wikipedia/en/6/65/Glengarrymovie.jpg', \
                        'https://www.youtube.com/watch?v=QgAU2RJHfvE')

alien = media.Movie ("Alien", 117, "a mining spacecraft stumbles across an alien parasite on an unknown planet", \
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",\
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

big_blue = media.Movie ("The Big Blue", 168, "free-diving epic", \
                    "https://upload.wikimedia.org/wikipedia/en/c/c5/Big_Blue_poster_200px.jpg",\
                    "https://www.youtube.com/watch?v=S6DEqKteBWk")

raising_arizona = media.Movie("Raising Arizona", 94, "comedy crime combined with children", \
                    "https://upload.wikimedia.org/wikipedia/en/3/31/Raising-Arizona-Poster.jpg",\
                    "https://www.youtube.com/watch?v=2AIfVoGUs6c")

chasing_great = media.Movie("Chasing Great", 101, "inside the mind of an All Black", \
                    "http://www.impawards.com/intl/new_zealand/2016/posters/chasing_great.jpg",\
                    "https://www.youtube.com/watch?v=HZ0MmhGQ4d8")

matrix = media.Movie("the Matrix", 136, "Dystopian future mixing mind and machine", \
                    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",\
                    "https://www.youtube.com/watch?v=tGgCqGm_6Hs")

movies = [glengarry, alien, big_blue, raising_arizona, chasing_great, matrix]

def main():
   ft.open_movies_page(movies)
   
main()