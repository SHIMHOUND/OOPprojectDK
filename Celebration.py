# Base class representing any celebration
class Celebration:
    def __init__(self, name, date):
        # Initialize celebration with a name and date
        self.name = name
        self.date = date
        self.guests = []  # List to store guests
        self.activities = []  # List to store activities

    # Method to add a guest to the celebration
    def add_guest(self, guest):
        """Add a guest to the celebration."""
        self.guests.append(guest)

    # Method to add an activity to the celebration
    def add_activity(self, activity):
        """Add an activity to the celebration."""
        self.activities.append(activity)

    # Method to describe the celebration
    def describe_celebration(self):
        """Describe the celebration, including guests and activities."""
        description = f"Today we are celebrating {self.name} on {self.date}.\n"
        description += "Guests:\n"
        for guest in self.guests:
            description += f"- {guest.name}\n"
        description += "Activities:\n"
        for activity in self.activities:
            description += f"- {activity.describe()}\n"
        return description


# Subclass for birthday celebrations
class Birthday(Celebration):
    def __init__(self, celebrant_name, age, date):
        # Initialize birthday celebration with celebrant's name, age, and date
        super().__init__("Birthday", date)
        self.celebrant_name = celebrant_name
        self.age = age
        self.gifts = []  # List to store gifts

    # Method to add a gift to the celebration
    def add_gift(self, gift):
        """Add a gift to the birthday celebration."""
        self.gifts.append(gift)

    # Method to describe the birthday celebration
    def describe_celebration(self):
        """Describe the birthday celebration, including gifts."""
        description = f"Happy {self.age}th Birthday to {self.celebrant_name}!\n"
        description += super().describe_celebration()  # Call the base class method
        description += "Gifts:\n"
        for gift in self.gifts:
            description += f"- {gift.describe()}\n"
        return description


# Subclass for wedding celebrations
class Wedding(Celebration):
    def __init__(self, couple_names, date):
        # Initialize wedding celebration with couple's names and date
        super().__init__("Wedding", date)
        self.couple_names = couple_names
        self.vows = ""  # To store wedding vows

    # Method to add vows to the wedding
    def add_vows(self, vows):
        """Add vows to the wedding celebration."""
        self.vows = vows

    # Method to describe the wedding celebration
    def describe_celebration(self):
        """Describe the wedding celebration, including vows."""
        description = f"Congratulations to {self.couple_names} on their wedding day!\n"
        description += super().describe_celebration()  # Call the base class method
        description += f"Vows:\n{self.vows}\n"
        return description


# Class representing a guest
class Guest:
    def __init__(self, name):
        # Initialize guest with a name
        self.name = name


# Base class for activities
class Activity:
    def __init__(self, name):
        # Initialize activity with a name
        self.name = name

    # Method to describe the activity
    def describe(self):
        """Describe the activity."""
        return f"Activity: {self.name}"


# Subclasses for specific activities
class CakeCutting(Activity):
    def describe(self):
        """Describe the cake cutting activity."""
        return f"Cake Cutting: {self.name}"


class Game(Activity):
    def describe(self):
        """Describe the game activity."""
        return f"Game: {self.name}"


class Music(Activity):
    def describe(self):
        """Describe the music activity."""
        return f"Music: {self.name}"


# Base class for gifts
class Gift:
    def __init__(self, name):
        # Initialize gift with a name
        self.name = name

    # Method to describe the gift
    def describe(self):
        """Describe the gift."""
        return f"Gift: {self.name}"


# Subclasses for specific gifts
class Book(Gift):
    def describe(self):
        """Describe the book gift."""
        return f"Book: {self.name}"


class Phone(Gift):
    def describe(self):
        """Describe the Phone gift."""
        return f"Phone: {self.name}"


class Drink(Gift):
    def describe(self):
        """Describe the Drink gift."""
        return f"Drink: {self.name}"


# Create a Birthday celebration
birthday_celebration = Birthday("Daler", 18, "2024-02-14")

# Create guests
guest1 = Guest("Amal")
guest2 = Guest("Diana")
guest3 = Guest("Karina")

# Add guests to the celebration
birthday_celebration.add_guest(guest1)
birthday_celebration.add_guest(guest2)
birthday_celebration.add_guest(guest3)

# Add activities to the celebration
cake_cutting = CakeCutting("Cutting the Cake")
game = Game("Musical Chairs")
music = Music("Techno Rave mix")
birthday_celebration.add_activity(cake_cutting)
birthday_celebration.add_activity(game)
birthday_celebration.add_activity(music)

# Add gifts to the celebration
book_gift = Book("The Financier")
phone_gift = Phone("Iphone 15 Pro Max")
drink_gift = Drink("Jagermeister")
birthday_celebration.add_gift(book_gift)
birthday_celebration.add_gift(phone_gift)
birthday_celebration.add_gift(drink_gift)

# Describe the first birthday celebration
celebration_description = birthday_celebration.describe_celebration()
print(celebration_description)

print("\n" + "-"*50 + "\n")

# Create a Wedding celebration
wedding_celebration = Wedding("Azamat and Madina", "2024-06-15")

# Create guests
guest1 = Guest("Said")
guest2 = Guest("Daler")
guest3 = Guest("Diana")

# Add guests to the celebration
wedding_celebration.add_guest(guest1)
wedding_celebration.add_guest(guest2)
wedding_celebration.add_guest(guest3)

# Add activities to the celebration
music_activity = Music("Wedding March")
game_activity = Game("Wedding Dance-Off")
wedding_celebration.add_activity(music_activity)
wedding_celebration.add_activity(game_activity)

# Add vows to the celebration
wedding_vows = ("To have and to hold, from this day forward, for better or worse,"
                " in sickness and in health, to love and to cherish, till death do us part.")
wedding_celebration.add_vows(wedding_vows)

# Describe the wedding celebration
wedding_description = wedding_celebration.describe_celebration()
print(wedding_description)