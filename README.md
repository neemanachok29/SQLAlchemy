# SQLAlchemy
Restaurant Reviews System
This is a simple Python-based Restaurant Reviews System that demonstrates Object-Oriented Programming (OOP) principles and relationships. The system consists of three main classes: Customer, Restaurant, and Review, which are organized in separate files for better modularity.

Classes
Customer Class
The Customer class represents a customer and has the following attributes and methods:

given_name: First name of the customer
family_name: Last name of the customer
reviews_list: List of reviews associated with the customer
full_name(): Method to get the full name of the customer
restaurants(): Method to get a list of restaurants reviewed by the customer
add_review(restaurant, rating): Method to add a review for a restaurant
Restaurant Class
The Restaurant class represents a restaurant and includes:

name: Name of the restaurant
reviews_list: List of reviews associated with the restaurant
reviews(): Method to get a list of reviews for the restaurant
customers(): Method to get a list of customers who reviewed the restaurant
average_star_rating(): Method to calculate the average star rating for the restaurant
Review Class
The Review class represents a review and includes:

customer: Customer who wrote the review
restaurant: Restaurant being reviewed
rating_value: Rating given in the review
rating(): Method to get the rating value
customer(): Method to get the customer associated with the review
restaurant(): Method to get the restaurant associated with the review
Usage



Run the main file restaurants.py to see sample usage and outputs: python3 restaurants.py

The program will demonstrate creating customers, restaurants, and reviews, as well as associating them and performing various operations.

Folder Structure
The project is organized into the following folders and files:

lib/: Contains the class definitions.
customer.py: Defines the Customer class.
restaurant.py: Defines the Restaurant class.
review.py: Defines the Review class.
main.py: The main file to run the program, showcasing usage of the classes.
