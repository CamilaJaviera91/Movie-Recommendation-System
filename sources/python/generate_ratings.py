from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 1000

# Define user and movie lists
users = [8585, 8156, 9879, 3889, 5065, 5105, 5657, 6682, 5397, 6894, 6473, 2524, 7052, 8213, 8077, 1969, 9169, 3507]
movies = list(range(1, 317))  # Movie IDs from 1 to 316

# Generate data
rating_ids = random.sample(range(1000, 9999), num_entries)  # Unique IDs
user_ids = random.choices(users, k=num_entries)  # Allow repetitions
movie_ids = random.choices(movies, k=num_entries)  # Allow repetitions
ratings = random.choices(range(1, 11), k=num_entries)  # Ratings between 1 and 10
rating_dates = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_entries)]

# Combine the data into a list of tuples
ratings_data = [
    (rating_ids[i], user_ids[i], movie_ids[i], ratings[i], rating_dates[i])
    for i in range(num_entries)
]

# Print the data in SQL format
print("INSERT INTO movie_recommendation.ratings (rating_id, user_id, movie_id, rating, rating_date) VALUES")
values = ",\n".join(
    [f"    ({r[0]}, {r[1]}, {r[2]}, {r[3]}, '{r[4]}')" for r in ratings_data]
)
print(values + ";")
