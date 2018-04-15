import fresh_tomatoes
import media

"""Create six Movie instances each with title, storyline, poster image, and YouTube trailer of the class Movie defined in media.py."""

thor_ragnarok = media.Movie("Thor: Ragnarok", 
                        "Thor is imprisoned on the other side of the universe without his mighty hammer and finds himself in a race against time to get Back to Asgard to stop Ragnarok", "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg", "https://www.youtube.com/watch?v=ue80QwXMRHg")

black_panther = media.Movie("Black Panther",
                     "After the death of his father, T'Challa returns home to the African nation of Wakanda to take his rightful place as king",
                     "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")

spiderman_homecoming = media.Movie("Spider-Man: Homecoming", 
                             "Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man. Peter must soon put his powers to the test when the evil Vulture emerges to threaten everything that he holds dear.",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                             "https://www.youtube.com/watch?v=U0D3AOldjMU")

doctor_strange = media.Movie("Doctor Strange",
                          "The story of world-famous neurosurgeon Dr. Stephen Strange whose life changes forever after a horrific car accident robs him of the use of his hands",
                          "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg","https://www.youtube.com/watch?v=HSzx-zryEgM")

captain_america_civil_war = media.Movie("Captain America: Civil War",
                                "The new status quo deeply divides members of the team. Captain America believes superheroes should remain free to defend humanity without government interference. Iron Man sharply disagrees and supports oversight.",
                                "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                                "https://www.youtube.com/watch?v=dKrVegVI0Us")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                           "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality.",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Add instances to a list
movies = [thor_ragnarok, black_panther, spiderman_homecoming, doctor_strange, captain_america_civil_war, avengers_infinity_war]
fresh_tomatoes.open_movies_page(movies)