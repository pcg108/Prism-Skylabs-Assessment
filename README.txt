VACATIONING SALESMAN:

SETUP:
To run this program, the geopy library is required to be installed. To do so, please type the following on the
command line (assuming pip is installed):

pip install geopy

Otherwise, I have included the geopy folder in the folder I have sent, so in that case geopy need not be installed.
However, I have not tested this method, so if installing geopy through pip is possible, please do so.

HOW TO USE:
Construct a text file with a list of cities and their states/countries (I have provided a test file here).
The first two lines of the file must specify the MODE OF TRANSPORTATION and the UNIT OF MEASUREMENT:
	-the mode can be "straightline", "driving", "walking", "bicycling", and "transit"
		-note, if a certain mode of transport is not available, AN ERROR WILL RESULT. "straightline" will 
		always work, and "driving" will work for anywhere in North America
	-the measurement units can be "miles" and "kilometers"

TO RUN:
In the terminal, type the following:

py distances.py < cities.txt

and it will run. PLEASE NOTE: SOMETIMES THE GEOPY LIBRARY DOES NOT ESTABLISH A PROPER CONNECTION, SO IF AN ERROR 
OCCURS, PLEASE RUN IT AGAIN. It will work on the 2nd or 3rd try if it does not work the first time.

LANGUAGE CHOICE:
I decided to use python to implement this tool, as it was very conducive to using the Google Distance Matrix and
Geopy APIs. 
To implement the tool, I began by parsing the input from the cities.txt file. Input had to parsed in two ways:
one for the geopy library (straighline distance) and one for the Google Distance Matrix API (other forms of 
transportation). I detailed and commented my method in the code. Next, based on the user's preference of 
transportation, I used either made requests to the Geopy or Google Distance Matrix APIs to compute the distance. 
I initially began by only using the Distance Matrix API, but I realized that it would not allow for straightline 
distances. Therefore, I also incorporated the geopy library to take that into account. I then gave the user the 
option to choose, increasing functionality. Finally, results are printed as suggested in the assignment sheet. 

I would love to work at Prism Skylabs this summer, as I believe that I can best apply my knowledge and abilities
to Prism's exciting technology. Thank you for this opportunity!
	