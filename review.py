# Define the Review class
class Review:
    all_reviews = []  # A list to store all review instances

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)  # Add the current instance to the list of all reviews
        customer.reviews_list.append(self)  # Associate the review with the customer
        restaurant.reviews_list.append(self)  # Associate the review with the restaurant

    # Getter method for review rating
    def rating(self):
        return self.rating_value

    # Getter method for customer associated with this review
    def customer(self):
        return self.customer

    # Getter method for restaurant associated with this review
    def restaurant(self):
        return self.restaurant

    # Class method to get all review instances
    @classmethod
    def all(cls):
        return cls.all_reviews

    # Class method to get a list of unique customers who wrote reviews
    @classmethod
    def customers(cls):
        return list(set([review.customer for review in cls.all_reviews]))

    # Class method to get a list of unique restaurants that were reviewed
    @classmethod
    def restaurants(cls):
        return list(set([review.restaurant for review in cls.all_reviews]))

    # Class method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers():
            if customer.full_name() == name:
                return customer

    # Class method to find all customers with a given given_name
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.customers() if customer.given_name == name]