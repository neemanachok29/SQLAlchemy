# Define the Restaurant class
class Restaurant:
    all_restaurants = []  # A list to store all restaurant instances

    def __init__(self, name):
        self.name = name
        self.reviews_list = []  # A list to store reviews associated with the restaurant
        Restaurant.all_restaurants.append(self)  # Add the current instance to the list of all restaurants

    # Getter method for restaurant name
    def name(self):
        return self.name

    # Class method to get all restaurant instances
    @classmethod
    def all(cls):
        return cls.all_restaurants

    # Get a list of reviews for this restaurant
    def reviews(self):
        return self.reviews_list

    # Get a list of customers who reviewed this restaurant
    def customers(self):
        return list(set([review.customer for review in self.reviews_list]))

    # Calculate average star rating for this restaurant
    def average_star_rating(self):
        if len(self.reviews_list) == 0:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews_list])
        return total_ratings / len(self.reviews_list)

