#Test Wedding celebration with no guests or activities
#Test adding varius activities
#Test Removing Guests or activies

from Celebration import (Wedding, Guest, CakeCutting,
                         Game, Music)

# Test Wedding celebration with no guests or activities
empty_wedding = Wedding("John and Jane", "2024-05-20")
print("Empty Wedding Celebration Description:")
print(empty_wedding.describe_celebration())
print("\n" + "-"*50 + "\n")





