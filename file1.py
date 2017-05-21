# class media which is defined in other file named media.py is going to be like a blueprint
# we are going to import this media class and using its init(i.e constructor) initialise  the object defined in file1

import fresh_tomatoes
import media    

# object 1
avatar = media.Media("Avatar" ,
                     "Because the planet's environment is poisonous,human/Na'vi hybrids,called Avatars, must link to human minds "
                     "to allow for free movement on Pandora. ",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "images/avatar.jpg");


# object 2

minion = media.Media("Minion",
                     "Evolving from single-celled yellow organisms at the dawn of time,"
                     "Minions live to serve" ,
                     "https://www.youtube.com/watch?v=kkPfdh-XhWg",
                     "images/minions.jpg")

# object 3
lalaland = media.Media("La La Land",
                       "A jazz pianist falls for an aspiring actress in Los Angeles.",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8",
                       "images/lalaland.jpg")

# object 4
stars = media.Media("Fault In Our Stars",
                    "Two teenage cancer patients begin a life-affirming journey"
                    "to visit a reclusive author in Amsterdam.",
                    "https://www.youtube.com/watch?v=9ItBvH5J6ss",
                    "images/faultInOurStar.jpg")

butterfly = media.Media("Butterfly Effect",
                        "The Four Horsemen resurface and are forcibly recruited by a tech"
                        " genius to pull off their most impossible heist yet.",
                        "https://www.youtube.com/watch?v=B8_dgqfPXFg",
                        "images/butterflyEffect.jpg")

ff = media.Media("Fast and Furious 8",
                 "Fate is the first film in the series to be conceived after the death of Paul Walker",
                 "https://www.youtube.com/watch?v=uisBaTkQAEs",
                 "images/ff8.jpg")


#fresh_tomatoe file is imported: that contains html css javascript
#let's call its method

movies = [stars,lalaland,ff,minion,avatar,butterfly]
fresh_tomatoes.open_movies_page(movies)
