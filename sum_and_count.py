# Question 1

SELECT SUM(population)
FROM world

# Question 2

select DISTINCT continent
from world

# Question 3

Select sum(gdp)
from world
where continent = 'Africa'

# Question 4

select count(name)
from world
where area >= 1000000

# Question 5

select sum(population)
from world
where name in ('Estonia', 'Latvia', 'Lithuania')

# Question 6

select continent, count(name)
from world
group by continent

#Question 7

select continent, count(name)
from world
where population >= 10000000
group by continent

# Question 8
select continent
from world
group by continent
having sum(population) >= 100000000