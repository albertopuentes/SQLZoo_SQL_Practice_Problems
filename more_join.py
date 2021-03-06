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

# 9
# List the films where 'Harrison Ford' has appeared - but not in the starring role. [Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]

SELECT title
FROM movie
  Join casting on (movie.id=casting.movieid) 
  Join actor on (actor.id=casting.actorid)
WHERE name = 'Harrison Ford' AND ord !=1

10.
# List the films together with the leading star for all 1962 films.

SELECT title, name
FROM movie
  Join casting on (movie.id=casting.movieid) 
  Join actor on (actor.id=casting.actorid)
WHERE yr = 1962 AND ord = 1

# 11.
# Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.

SELECT yr,COUNT(title) FROM
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id
WHERE name='Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 1

# 12.
# List the film title and the leading actor for all of the films 'Julie Andrews' played in.

# Did you get "Little Miss Marker twice"?

SELECT title, name FROM casting 
JOIN actor on (casting.actorid=actor.id)
JOIN movie on (casting.movieid=movie.id)
WHERE actorid IN (
  SELECT id FROM actor
  WHERE name='Julie Andrews')