from tablet import Tablet


class Battery:
    """A simple attempt to represent the battery of an ereader."""
    
    def __init__(self, battery_size = 1500):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a message describing the size of the battery."""
        print(f"This ereader has a battery size of {self.battery_size} mAh.")
        
    def display_batttery_charge(self):
        """Print a statement informing a user how much charge is left in the current battery"""
        if self.battery_size == 1500:
            life = 10
        elif self.battery_size ==1000:
            life = 8
            
        print(f"There are {life} hours of battery remaining.")
        
class Ereader(Tablet):
    """Represent aspects of a tablet specific to an ereading device."""
    
    def __init__(self, make, model, screen_size):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ereader.
        """
        
        super().__init__(make, model, screen_size)
        self.library_size = 1000
        self.battery = Battery()
        
    def describe_library(self):
        """Print a message describing the library size."""
        print(f"This ereader can hold {self.library_size} books.")