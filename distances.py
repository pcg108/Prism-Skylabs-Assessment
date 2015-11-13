from urllib.request import urlopen
import simplejson
import fileinput
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

#read in lines from the text file given in input
lines = []
for line in fileinput.input():
	lines.append(eval(line))

#determine the mode of transportation and the measurement units from the first two lines
mode = lines[0]
measurement = lines[1]
if measurement == 'miles':
	factor = 0.000621371
else:
	factor = 1/1000

#discard the first two lines
lines = lines[2:]

#the following block prepares the input for use in the Google Maps distance matrix API
places = []
for line in lines:
	#split each line into each individual word by removing commas an splitting on basis of whitespace
	line = line.replace(",", '')
	line = line.split()
	places.append(line)

#format the strings for use in the API url request
strings_url = []
for place in places:
	origin = ""
	#the url request for each city takes the form of New+York+City
	for word in place:
		origin += word+"+"
	origin = origin[:-1]
	strings_url.append(origin)

#this is part of the geopy library, which is used to compute the straightline distance between two locations
geolocator = Nominatim()
total_distance = 0

#if we want "as the crow flies" distance:
if mode == "straightline":
	#here, we compute the latitude and longitude of a location and the subsequent location, and then print the distance
	for i in range(len(lines)):
		#we want to stay in the range of inputs (because you cannot go anywhere from the final location)
		if (i+1) in range(len(lines)):
			#compute current location
			location = geolocator.geocode(lines[i])
			#compute next location
			location2 = geolocator.geocode(lines[i+1])
			#use appropriate function from geopy's vincenty (distance calculating) library	
			if measurement == 'miles':
				distance = vincenty((location.latitude, location.longitude), (location2.latitude, location2.longitude)).miles
			else:
				distance = vincenty((location.latitude, location.longitude), (location2.latitude, location2.longitude)).kilometers
			#add to total_distance
			total_distance+=distance*factor
			print(lines[i]+"->"+lines[i+1]+': '+str(distance*factor)+" "+measurement)	
else:
	#google distance matrix API key
	#we use the distance matrix api to compute distances for different modes of travel, including driving, walking, bicycling, and transit (see README)
	key = 'AIzaSyDiCQ1CQWoXaYS7349jnXpn5PAYTPnw454'
	for i in range(len(strings_url)):
		if (i+1) in range(len(strings_url)):
			#format the API request string
			url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&key={2}&mode={3}'.format(strings_url[i], strings_url[i+1], key, mode)
			distances = urlopen(url)
			#convert from JSON
			result = simplejson.load(distances)
			#access the appropriate element from the dictionary that is returned
			distance = result['rows'][0]['elements'][0]['distance']['value']
			#adjust from meters to miles/km
			total_distance+= distance*factor
			print(lines[i]+"->"+lines[i+1]+': '+str(distance)+" "+measurement)

print("Total distance covered in your trip: "+str(total_distance)+" "+measurement)
