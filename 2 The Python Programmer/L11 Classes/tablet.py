class Tablet:
    """A simple representation of a tablet, such as an iPad."""
    
    def __init__(self, make, model, screen_size):
        """Initialize attributes to describe a tablet."""
        self.make = make
        self.model = model
        self.screen_size = screen_size
        self.total_storage = 256
        
    def get_tablet_description(self):
        """Return a description of a tablet."""
        tablet_description = f"{self.make}, {self.model}, {self.screen_size}"
        return tablet_description
    
    def available_storage(self):
        """Print a message to display a tablets available storage."""
        print(f"This tablet has a storage capacity of {self.total_storage} GB.")
        
    def update_storage(self, storage):
        """
        Set the available storage to the value given.
        Reject the change if storage amount is less than total storage.
        """
        if storage < self.total_storage:
            self.total_storage = self.total_storage - storage
        else:
            print("There is not enough storage available.")
            
    def increment_total_storage(self, application):
        """Add the amount removed to total storage available."""
        self.total_storage += application