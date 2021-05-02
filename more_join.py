# 1.
# List the films where the yr is 1962 [Show id, title]

SELECT id, title
 FROM movie
 WHERE yr=1962

#  2.
# Give year of 'Citizen Kane'.

select yr
from movie
where title='Citizen Kane'

# 3.
# List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
select id, title, yr
from movie
where title like '%Star Trek%'
order by yr

# 4. 4.
# # What id number does the actor 'Glenn Close' have?
select actor.id
from movie join actor on (movie.id=actor.id)
where name = 'Glenn Close'

# 5.
# What is the id of the film 'Casablanca'

select id
from movie
where title='Casablanca'

# 6.
# Obtain the cast list for 'Casablanca'.
# what is a cast list?
# The cast list is the names of the actors who were in the movie.
# Use movieid=11768, (or whatever value you got from the previous question)

Select name 
From actor 
    Join casting on (actor.id=casting.actorid) 
    Join movie on (movie.id=casting.movieid)
Where title='Casablanca'

# 7.
# Obtain the cast list for the film 'Alien'

SELECT name 
FROM actor 
  Join casting on (actor.id=casting.actorid) 
  Join movie on (movie.id=casting.movieid)
WHERE title = 'Alien'

# 8.
# List the films in which 'Harrison Ford' has appeared

SELECT title 
FROM movie
  Join casting on (movie.id=casting.movieid) 
  Join actor on (actor.id=casting.actorid)
WHERE name = 'Harrison Ford'