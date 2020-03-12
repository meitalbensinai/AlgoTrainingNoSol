# DBSCAN

Read about the DBSCAN algorithm:

https://www-users.cs.umn.edu/~kumar001/dmbook/ch8.pdf pages 526-555

You will implement a variation of this algorithm to detect outliers.

The given data contains lat, lon and owner:

1. Present the data with different colors for different owner

2. Apply dbscan algorithm on the data, present outliers in red and all other clusters in blue.

Read the next paper:

https://bib.dbvis.de/uploadedFiles/17.pdf

3. Implement the two algorithms presented and apply p-dbscan to find outliers now. Choose your parameters to present meaningful differences from the regular dbscan results.


# Flickr Dataset

Data fields:

photo_id

owner -> user id related to the owner of the photo

gender -> owner's gender

occupation -> occupation of owner

title -> title of photo

description -> description of photo


faves -> photo's favorite rate

lat -> photo's latitude

lon -> photo's longitude

u_city -> user's city

u_country -> user's country

taken -> the time of photo taken

weather -> weather condition related to the time that photo is taken

season -> season related to the time that photo is taken

daytime -> time of the day that photo is taken
---------------------
Data type:

photo_id -> numeric

owner -> character

gender -> numeric (0=others, 1=male, 2=female, 3=rather not say)

occupation -> character

title -> character

description -> character

faves -> numeric

lat -> decimal

lon -> decimal

u_city -> character

u_country -> character

taken -> timestamp (YYYY-MM-DD HH:MM:SS)

weather -> character (1=clear-day, 2=clear-night, 3=rain, 4=snow, 5=sleet, 6=wind, 7=fog, 8=cloudy, 9=partly-cloudy-day, 10=partly-cloudy-night)

season -> character (1=spring, 2=summer, 3=autumn, 4=winter)

daytime -> character (1=day, 2=night, 3=midnight)

---------------------
