SELECT countries.name, languages.language, languages.percentage
FROM countries join languages on countries.id=languages.country_id
WHERE languages.language= 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name ,COUNT(cities.id) as total_number_cities
FROM countries join cities on countries.id=cities.country_id
GROUP BY countries.name
ORDER BY total_number_cities DESC;
 
SELECT cities.name, cities.population
FROM cities join countries on countries.id=cities.country_id
WHERE countries.name='MEXICO' AND cities.population>500000
ORDER BY cities.population;

SELECT languages.language, countries.name, languages.percentage
FROM languages JOIN countries on countries.id=languages.country_id
WHERE languages.percentage>89
ORDER BY languages.percentage DESC;

SELECT countries.name
FROM countries
WHERE surface_area<501 AND (population>100000);

SELECT countries.name
FROM countries
WHERE countries.government_form='Constitutional Monarchy' 
AND capital>200
AND life_expectancy>75;

SELECT countries.name, cities.name, cities.population, cities.district
FROM cities join countries on countries.id=cities.country_id
WHERE countries.name='ARGENTINA' AND cities.district='BUENOS AIRES' AND cities.population>500000
ORDER BY cities.population;

SELECT countries.region,COUNT(countries.id) as number_ofcountries
FROM countries
GROUP BY countries.region
ORDER by number_ofcountries DESC;