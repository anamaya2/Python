'''
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/custom_song_assignment.py
'''
def custom_song(vehicle, city, object, vehicle2, landmark, adjective, feeling, feeling2):
    print(f"I hopped off the {vehicle} at {city}")
    print(f"With a dream and my {object}")
    print(f"Welcome to the land of fame excess")
    print(f"Am I gonna fit in?")
    print(f"Jumped in the {vehicle2}, here I am for the first time")
    print(f"Look to my right, and I see the {landmark}")
    print(f"This is all so crazy, everybody seems so {adjective}")
    print(f"My tummy's turnin' and I'm feelin' kinda {feeling}")
    print(f"Too much pressure and I'm {feeling2}")
    
vehicle = input("Give me a vehicle: ")
city = input("Give me a city name: ")
object = input("Give me an object: ")
vehicle2 = input("Give me another vehicle: ")
landmark = input("Give me a landmark: ")
adjective = input("Give me an adjective: ")
feeling = input("Give me a feeling: ")
feeling2 = input("Give me another feeling: ")

custom_song(vehicle, city, object, vehicle2, landmark, adjective, feeling, feeling2)
