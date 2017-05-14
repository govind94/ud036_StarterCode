import media
import fresh_tomatoes

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

godfather = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                        "http://static.metacritic.com/images/products/movies/3/47c2b1f35087fc23c5ce261bbc3ad9e0.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

godfather_part_two = media.Movie("The Godfather: Part II",
                                 "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                                 "http://vignette3.wikia.nocookie.net/filmguide/images/a/ac/The-godfather-part-ii-1974-3e490.jpg/revision/latest?cb=20120327061641",
                                 "https://www.youtube.com/watch?v=qJr92K_hKl0")

dark_knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the Dark Knight must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                          "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

twelve_angry_men = media.Movie("12 Angry Men",
                               "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
                               "http://t1.gstatic.com/images?q=tbn:ANd9GcQuhFZT3lQfr0vDy4XWMHQ8X93FWuamEuw_5iB4dmOTxc_w79rA",
                               "https://www.youtube.com/watch?v=A7CBKT0PWFA")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

movies = [shawshank_redemption, godfather, godfather_part_two, dark_knight, twelve_angry_men, pulp_fiction]
fresh_tomatoes.open_movies_page(movies)
