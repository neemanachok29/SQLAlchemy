from .review import Review

# Define the Customer class
class Customer:
    all_customers = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews_list = []  # A list to store reviews associated with the customer
        Customer.all_customers.append(self)  # Add the current instance to the list of all customers

    # Getter methods for customer attributes
    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    # Concatenate given name and family name to get full name
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class method to get all customer instances
    def all(cls):
        return cls.all_customers

    # Get a list of restaurants reviewed by the customer
    def restaurants(self):
        
        return list(set([review.restaurant for review in self.reviews_list]))

    # Method to add a review associated with this customer
    def add_review(self, restaurant, rating):
        Review(self, restaurant, rating)  # Create a new Review instance