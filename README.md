#Gowalla Python Client

This python-gowalla library is a thin layer that exposes Gowalla's API. Although the data structure is likely to be a moving target, it hasn't changed in the past couple weeks. For now, this client only supports Gowalla's read-only methods. As some available calls are undocumented, I've only tested the ones that have been explicitly mentioned in the documentation and API explorer.


##Usage

See **tests.py** for example usage. Create test_settings.py defining USERNAME, PASSWORD and API\_KEY to run tests.


##Documentation

View [Gowalla API documentation](http://gowalla.com/api/docs) and [API Explorer]() for details on connection and various calls. The [Gowalla Developers Group](http://groups.google.com/group/gowalla-dev) also has information (some heretofore undocumented) on other calls and details about the API.


##Requirements

- [Python](http://python.org/) (2.5 or greater, but not 3.x)


##Tested Methods

###Get User
Returns information on a Gowalla user. Excepts username or user id.

	/users/USERNAME
	/users/USER_ID


###List User's Friends
Returns a list of the user's friends. Excepts username or user id. **This currently returns an empty list.**

	/users/USER_ID/friends
	/users/USERNAME/friends


###Get User's Items
Returns a dictionary including a list of the user's items. 

	/users/USERNAME/items


###Get Spot
Returns information on a Gowalla spot.

	/spots/SPOT_ID


###List Spots Near Longitude/Latitude

	/spots?lat=LATITUDE&lng=LONGITUDE&radius=RADIUS


###Get Spot's Items
Returns a dictionary including a list of the items at a Gowalla spot.

	/spots/SPOT_ID/items


###List Trips
Returns a list of "official" Gowalla trips. This is likely to change as user contributed trips becomes live.

	/trips 


###Get Trip 
Returns information on a Gowalla trip.

	/trips/TRIP_ID


###Get Item
Returns information on a Gowalla item.

	/items/ITEM_ID


###List Item's Events
Returns a list of things that have "happened" to the item.

	/items/ITEM_ID/events