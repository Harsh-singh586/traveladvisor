import pymongo
client = pymongo.MongoClient(MONGODB_URI)
from scrapper import New_York, New_delhi
newyork = New_York()
newdelhi = New_delhi()
db_newyork = client['New_York']
db_newdelhi = client['New_Delhi']
def add_new_york_hotels():
	table_newyork_hotels = db_newyork['Hotels']
	print('first check')
	detail = newyork.gethotels()
	print('second check')
	for i in detail:
		print(table_newyork_hotels.insert_one(i))

def add_new_york_restaurants():
	table_newyork_restaurants = db_newyork['Restaurants']
	print('first')
	detail = newyork.getrestaurants()
	print('second check')
	for i in detail:
		print(table_newyork_restaurants.insert_one(i))

def add_new_york_things_todo():
	table_newyork_thingstodo = db_newyork['Things_To_Do']
	print('first check')
	detail = newyork.getthingstodo()
	print('second check')
	for i in detail:
		print(table_newyork_thingstodo.insert_one(i))

def add_new_york_things_tosee():
	table_newyork_thingstosee = db_newyork['Things_To_See']
	print('First Check')
	detail = newyork.getthingstosee()
	print('second')
	for i in detail:
		print(table_newyork_thingstosee.insert_one(i))

def add_new_delhi_hotels():
	table_newdelhi_hotels = db_newdelhi['Hotels']
	print('first')
	detail = newdelhi.gethotels()
	for i in detail:
		print(table_newdelhi_hotels.insert_one(i))

def add_new_delhi_restaurants():
	table_newdelhi_restaurants = db_newdelhi['Restaurants']
	print('first')
	detail = newdelhi.getrestaurants()
	print('second')
	for i in detail:
		print(table_newdelhi_restaurants.insert_one(i))

def add_new_delhi_things_todo():
	table_newdelhi_things_tosee = db_newdelhi['Things_To_See']
	print('first')
	detail = newdelhi.getthingstosee()
	for i in detail:
		print(table_newdelhi_things_tosee.insert_one(i))

add_new_delhi_things_todo()