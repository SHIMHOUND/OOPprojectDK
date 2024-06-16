from Celebration import (Birthday, Wedding, Guest, CakeCutting,
                         Game, Music, Book, Phone, Drink)
import random

# Test Birthday celebration with many guests
# Read names from Names.txt
with open('Names.txt', 'r') as file:
    names = [line.strip() for line in file.readlines()]

# Shuffle the names
random.shuffle(names)

# Test Birthday celebration with many guests
many_guests_birthday = Birthday("Sam", 23, "2024-07-10")

# Add guests from the shuffled names, appending a number to each name
for i, name in enumerate(names):
    many_guests_birthday.add_guest(Guest(f"{i+1}.{name} "))

print("Many Guests Birthday Celebration Description:")
print(many_guests_birthday.describe_celebration())
print("\n" + "-"*50 + "\n")

# Create a Birthday celebration
birthday_celebration = Birthday("Daler", 18, "2024-02-14")

# Create guests for the birthday celebration
guest1 = Guest("Amal")
guest2 = Guest("Diana")
guest3 = Guest("Karina")

# Add guests to the birthday celebration
birthday_celebration.add_guest(guest1)
birthday_celebration.add_guest(guest2)
birthday_celebration.add_guest(guest3)

# Add activities to the birthday celebration
cake_cutting = CakeCutting("Cutting the Cake")
game = Game("Musical Chairs")
music = Music("Techno Rave mix")
birthday_celebration.add_activity(cake_cutting)
birthday_celebration.add_activity(game)
birthday_celebration.add_activity(music)

# Add gifts to the birthday celebration
book_gift = Book("The Financier")
phone_gift = Phone("iPhone 15 Pro Max")
drink_gift = Drink("Jagermeister")
birthday_celebration.add_gift(book_gift)
birthday_celebration.add_gift(phone_gift)
birthday_celebration.add_gift(drink_gift)

# Describe the birthday celebration
print("Birthday Celebration Description:")
print(birthday_celebration.describe_celebration())

print("\n" + "-"*50 + "\n")

# Create a Wedding celebration
wedding_celebration = Wedding("Azamat and Madina", "2024-06-15")

# Create guests for the wedding celebration
guest1 = Guest("Said")
guest2 = Guest("Daler")
guest3 = Guest("Diana")

# Add guests to the wedding celebration
wedding_celebration.add_guest(guest1)
wedding_celebration.add_guest(guest2)
wedding_celebration.add_guest(guest3)

# Add activities to the wedding celebration
wedding_music = Music("Wedding March")
wedding_game = Game("Wedding Dance-Off")
wedding_celebration.add_activity(wedding_music)
wedding_celebration.add_activity(wedding_game)

# Add vows to the wedding celebration
wedding_vows = ("To have and to hold, from this day forward, for better or worse,"
                " in sickness and in health, to love and to cherish, till death do us part.")
wedding_celebration.add_vows(wedding_vows)

# Describe the wedding celebration
print("Wedding Celebration Description:")
print(wedding_celebration.describe_celebration())

# Test Birthday celebration with no guests or activities
empty_birthday = Birthday("Sam", 23, "2024-07-10")
print("Empty Birthday Celebration Description:")
print(empty_birthday.describe_celebration())
print("\n" + "-"*50 + "\n")

# Test removing guests and activities from a celebration
removal_test_birthday = Birthday("Sam", 23, "2024-07-10")
guest1 = Guest("Alice")
guest2 = Guest("Bob")
activity1 = Game("Pin the Tail on the Donkey")
activity2 = Music("Classical Playlist")

removal_test_birthday.add_guest(guest1)
removal_test_birthday.add_guest(guest2)
removal_test_birthday.add_activity(activity1)
removal_test_birthday.add_activity(activity2)

# Assuming methods remove_guest and remove_activity exist
# removal_test_birthday.remove_guest(guest1)
# removal_test_birthday.remove_activity(activity1)

print("Removal Test Birthday Celebration Description:")
print(removal_test_birthday.describe_celebration())
print("\n" + "-"*50 + "\n")

# Test adding various activities to a celebration
activity_test_birthday = Birthday("Sam", 23, "2024-07-10")
activity_test_birthday.add_activity(CakeCutting("Cutting the Cake"))
activity_test_birthday.add_activity(Game("Treasure Hunt"))
activity_test_birthday.add_activity(Music("Jazz Playlist"))
print("Activity Test Birthday Celebration Description:")
print(activity_test_birthday.describe_celebration())
print("\n" + "-"*50 + "\n")
