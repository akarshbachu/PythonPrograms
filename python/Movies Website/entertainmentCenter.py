import media
import webbrowser
import fresh_tomatoes
toystory=media.Movie("Toy Story","A boy and his toys story",
                     "https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")
bahubali=media.Movie("Bahubali","A story of kingdom",
                     "https://upload.wikimedia.org/wikipedia/hi/7/7e/Baahubali_poster.jpg",
                     "https://www.youtube.com/watch?v=sOEg_YZQsTI")
ghazi=media.Movie("Ghazi","Based on Real story",
                     "http://pressks.com/wp-content/uploads/2016/12/Ghazi-Movie-First-Look-Poster.jpg",
                     "https://www.youtube.com/watch?v=1gKddowLVo0")

#print(toystory.story_line)
#toystory.showTrailer()
#webbrowser.open(toystory.trailer_youtube_url)

#to print documentation of file:
print(media.Movie.__doc__)
movies=[toystory,bahubali,ghazi]
fresh_tomatoes.open_movies_page(movies)
