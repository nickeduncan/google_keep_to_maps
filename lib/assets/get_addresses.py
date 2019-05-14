import gkeepapi
import googlemaps

keep = gkeepapi.Keep()
success = keep.login('')

gnotes = keep.all()
for note in gnotes:
    if note.title == 'Restaurants':
        restaurants = note.unchecked

gmaps = googlemaps.Client(key='AIzaSyDrTeYDosQiqr1AgtPYRAF1uzc0CcnZdKc')
addresses = []
for restaurant in restaurants:
    addresses.append(gmaps.find_place(restaurant.text,
                                      'textquery',
                                      fields=['name', 'formatted_address'],
                                      location_bias='point:25.837940,-80.120338')['candidates'][0]['formatted_address'])

addresses
