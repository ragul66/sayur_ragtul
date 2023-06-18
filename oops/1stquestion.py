class Hotel:
    def __init__(self, name, rooms, rating):
        self.name = name
        self.rooms = rooms
        self.rating = rating

noOfhotels = int(input("Enter the number of hotels: "))
hotels = []

for i in range(noOfhotels):
    name = input("Enter the name of hotel {}: ".format(i + 1))
    rooms = int(input("Enter the number of rooms in {}: ".format(name)))
    rating = float(input("Enter the rating of {}: ".format(name)))
    hotel = Hotel(name, rooms, rating)
    hotels.append(hotel)

# Find the hotel with the most rooms
max_rooms_hotel = None
max_rooms = 0

for hotel in hotels:
    if hotel.rooms > max_rooms:
        max_rooms = hotel.rooms
        max_rooms_hotel = hotel.name

# Find the hotel with the highest rating
max_rating_hotel = None
max_rating = 0

for hotel in hotels:
    if hotel.rating > max_rating:
        max_rating = hotel.rating
        max_rating_hotel = hotel.name

print("Hotel with the most rooms: {}".format(max_rooms_hotel))
print("Hotel with the highest rating: {}".format(max_rating_hotel))
