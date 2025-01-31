from faker import Faker
import random

# Initialize the Faker library to generate fake dates
fake = Faker()

# Set the number of entries to generate
num_entries = 1000

# Define user and movie lists (predefined user IDs and movie IDs ranging from 1 to 316)
users = [8585, 8156, 9879, 3889, 5065, 5105, 5657, 6682, 5397, 6894, 6473, 2524, 7052, 8213, 8077, 1969, 9169, 3507]
movies = list(range(1, 317))  # Movie IDs from 1 to 316

# Generate random data
rating_ids = random.sample(range(1000, 9999), num_entries)  # Generate unique rating IDs
user_ids = random.choices(users, k=num_entries)  # Select random users with repetition
movie_ids = random.choices(movies, k=num_entries)  # Select random movies with repetition
ratings = random.choices(range(1, 6), k=num_entries)  # Generate random ratings between 1 and 5
rating_dates = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_entries)]  # Generate random dates from the last 10 years

# Combine the generated data into a list of tuples
ratings_data = [
    (rating_ids[i], user_ids[i], movie_ids[i], ratings[i], rating_dates[i])
    for i in range(num_entries)
]

# Print the generated data in SQL INSERT format
print("INSERT INTO movie_recommendation.ratings (rating_id, user_id, movie_id, rating, rating_date) VALUES")
values = ",\n".join(
    [f"    ({r[0]}, {r[1]}, {r[2]}, {r[3]}, '{r[4]}')" for r in ratings_data]
)
print(values + ";")
