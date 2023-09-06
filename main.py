from .customer import Customer
from .restaurant import Restaurant
from .review import Review

if __name__ == "__main__":
    # Create instances and perform operations
    customer1 = Customer("Mary", "Jane")
    customer2 = Customer("Bundotich", "Franklin")
    restaurant1 = Restaurant("Big Square")
    restaurant2 = Restaurant("CJ's")

    # Add reviews using the instances defined above
    customer1.add_review(restaurant1, 4)
    customer1.add_review(restaurant2, 5)
    customer2.add_review(restaurant1, 3)

    # Print restaurant names associated with customer1
    print([restaurant.name for restaurant in customer1.restaurants()])

    # Print customer names associated with restaurant1
    print([customer.full_name() for customer in restaurant1.customers()])

    # Print average star rating for restaurant1
    print(restaurant1.average_star_rating())

    # Finding customer by name and printing full name
    print(Review.find_by_name("Mary Jane").full_name())  
    
    # Finding all customers with given name
    print([customer.full_name() for customer in Review.find_all_by_given_name("Mary")])  
